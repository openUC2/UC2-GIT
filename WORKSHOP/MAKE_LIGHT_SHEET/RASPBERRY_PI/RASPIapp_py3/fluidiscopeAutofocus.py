'''
    Autofocus of UC2-GUI.
'''
# %% imports

# own
import fluidiscopeGlobVar as fg
import fluidiscopeToolbox as toolbox
import fluidiscopeIO as fio
from fluidiscopeLogging import logger_createChild
import fluidiscopeCalculate as fc

# general imports
import unipath as uni
from datetime import datetime
from os import listdir, path
from glob import glob
from time import sleep, time
from fractions import Fraction

import logging
import tifffile as tif
# math
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter


if not fg.my_dev_flag:
    from picamera.array import PiRGBArray
else:
    import imageio as imo

# %% parameters and pre starts
logger = logger_createChild('autofocus','UC2')
#
# %%
# ----------------------------------- #
# @       interface toolbox         @ #
# ----------------------------------- #


def autofocus_callback(self, instance, key, *rargs):
    '''
        Tests whether autofocus is already running or anything else is blocking. If not: blocks all measurements (and further autofocus-calls) and resets autofocus-count if scheduled.
        To block running autofocus, click "AF now" as implemented in Toolbox.run_autofocus-function.
    '''
    # skip if AF already running
    if fg.config['experiment']['autofocus_busy']:
        pass
    else:
        # wait 1s before checking again
        while fg.config['experiment']['imaging_active']:
            Clock.schedule_once(
                partial(toolbox.run_autofocus, self, instance, key), 1)
        logger.debug('Autofocus started.')
        fg.config['experiment']['autofocus_busy'] = True
        autofocus_routine(self)
        fg.config['experiment']['autofocus_busy'] = False
        logger.debug('Autofocus finished.')
        if instance.uid == self.ids['btn_autofocus_now'].uid:
            autofocus_afterclean(self=self,instance=instance,camdict='cam_af')
            toolbox.change_activation_status(instance)
#
#
# %%
# ----------------------------------- #
# @            Parameters           @ #
# ----------------------------------- #

def convert_Fraction_array(a):
    '''
    Tests and converts an array if fraction.
    '''
    return_tuple = False
    #logger.debug(a)

    # run on each element if is of list/tuple
    if isinstance(a,(tuple,list)):

        # make tuple changeable
        if isinstance(a,tuple):
            a = list(a)
            return_tuple = True
        
        # convert entries to floats
        for m in range(len(a)):
            a[m] = convert_Fraction_atom(a[m])
        
        # format back
        if return_tuple:
            a = tuple(a)

    else:
        a = convert_Fraction_atom(a)

    # done?
    return a

def convert_Fraction_atom(a):
    '''
    Tests if entry is Fraction and converts.
    '''
    if isinstance(a,Fraction):
        a = a.numerator / a.denominator
        #logger.debug("Converted atom.")
    
    # done?
    return a


def get_camstats(camera,printme=False):
    '''
    Retrieves all available camera-properties and stores them into a dictionary.

    :PARAMS:
    ========
    :camera:    pointing to PiCamera() instance
    :printme:   Whether the dict should be printed nicely

    :OUTPUTS:
    =========
    :camProp:   (DICT) with available camera properties

    '''
    # retrieve all existing get_functions
    all_getter =  [s for s in dir(camera) if "_get_" in s]
    camProp = {}
    for m in all_getter:
        try: 
            camProp[m[5:]] = eval('camera.' + m + '()')
            camProp[m[5:]] = convert_Fraction_array(camProp[m[5:]])
        except:
            pass

    if printme:
        print("\nlen(all_getter)={}\nlen(camProp)={}\n".format(len(all_getter),len(camProp)))
        for m in camProp:
            print(m + " = \t\t{}".format(camProp[m]))

    return camProp

def get_camstatsSorted(camStats, sel=None, just_subset=False, printme=False):
    '''
    Sorts resulting measurements so it can be used as a table.
    if just_subset==True, returns a list, else a dictionary.

    Example: 
    sel=['awb_gains','iso','shutter_speed','analog_gain']
    get_camstatsSorted(camStats,sel)

    '''
    if just_subset and sel is not None:
        camStats_sorted = [[[s,a[s]] for s in a if s in sel] for a in camStats]
    else: 
    
        # fill selection to all entries if not chosen
        sel = [m for m in camStats[0]] if sel is None else sel
        camStats_sorted = {}

        # traverse time-points and collect datasets
        for m in sel:
            camStats_sorted[m] = [a[m] for a in camStats]
    
        # print formatted
        if printme:
            for m in camStats_sorted:
                print(m+"=\t {}".format(camStats_sorted[m]))

    return camStats_sorted

def autofocus_afterclean(self, instance, camdict):
    '''
    After ending AF resets global values.
    '''
    fg.config[camdict]['camProp_defined'] = False

def autofocus_setupCAM(camStats=None, camdict=None,rawCapture=None):
    '''
        Prepares camera. 
        Make sure that Autofocus-config entries are updated before running this. 
        Does not do anything if global camera-properties are already active OR if Autofocus already configured camera.
    '''
    # record existing configuration
    if camStats is None:
        camStats = []
    else:
        camStats.append(get_camstats(fg.camera,printme=False))

    if camdict==None:
        camdict = 'cam'
        logger.warn('No camdict was given to Autofocus_setupCAM routine! For stability set to: {}.'.format(camdict))

    # test conditions
    update_condition = not (fg.config[camdict]['camProp_defined'] or ([fg.camera.resolution[0],fg.camera.resolution[1]]==fg.config[camdict]['resolution'] and fg.camera.sensor_mode == fg.config[camdict]['sensor_mode']))

    # if autofocus -> maybe measurement is running?
    if camdict == 'cam_af' and fg.config['experiment']['active']: 
        update_condition = False

    # if parameters not globally fixed OR not yet fixed by Autofocus-routine
    if not fg.config[camdict]['camProp_use_global']:
        if update_condition:

            # light a candle -> for now: no illumination if Ext is in methods
            if not 'Ext' in fg.config['experiment']['active_methods']:
                fg.ledarr.send("RECT+3+3+2+2+1", 200,200,200)
                sleep(fg.config['imaging']['speed'])

            # set basic modes 
            fg.camera.image_denoise = fg.config[camdict]['image_denoise']
            fg.camera.iso = fg.config[camdict]['iso']
            fg.camera.meter_mode = fg.config[camdict]['meter_mode']   
            fg.camera.sensor_mode = fg.config[camdict]['sensor_mode']
            fg.camera.resolution = fg.config[camdict]['resolution']
            fg.camera.video_denoise = fg.config[camdict]['video_denoise']
            fg.camera.video_stabilization = fg.config[camdict]['video_stabilization']     

            # Bayer-mode not possible with video-port => catch-error
            if fg.config[camdict]['use_video_port']:
                fg.config[camdict]['bayer'] = False

            # wait for camera to settle on new setup
            sleep(0.5)
            
            # prepare Buffer
            rawCapture = PiRGBArray(fg.camera, fg.camera.resolution)

            # take an image to use auto-functions for parameter estimation
            toolbox.take_image_atom(rawCapture=rawCapture,rawFormat='rgb',camdict=camdict)
            rawCapture.truncate(0)
            camStats.append(get_camstats(fg.camera,printme=False))

            # refresh autofocus-dictionary
            fg.config[camdict]['analog_gain'] = camStats[-1]['analog_gain']
            fg.config[camdict]['awb_gains'] = camStats[-1]['awb_gains']
            fg.config[camdict]['digital_gain'] = camStats[-1]['digital_gain']
            fg.config[camdict]['framerate'] = camStats[-1]['framerate']
            fg.config[camdict]['shutter_speed'] = camStats[-1]['exposure_speed']
            
            # overwrite camera parameters AND (therwith) FIX -> exposure_mode  must be last to be able to change shutter_speed properly
            fg.camera.awb_mode = fg.config[camdict]['awb_mode']
            fg.camera.awb_gains = fg.config[camdict]['awb_gains']
            fg.camera.exposure_compensation = fg.config[camdict]['exposure_compensation']
            fg.camera.framerate = fg.config[camdict]['framerate']
            fg.camera.shutter_speed = fg.config[camdict]['shutter_speed']
            sleep(1)
            fg.camera.exposure_mode = fg.config[camdict]['exposure_mode']
            logger.debug('analog_gain={}, digital_gain={}, shutter_speed={}.'.format(fg.camera.analog_gain,fg.camera.digital_gain, fg.camera.shutter_speed))

            # set True to use setting for future 
            fg.config[camdict]['camProp_defined'] = True
            fg.config['experiment']['active_camProp'] = camdict
            logger.debug("Camera preparation done for {}.".format(camdict))
    
            # turn the candle out
            fg.ledarr.send("CLEAR")
            fg.ledarr.send("CLEAR")

        # not measure all parameters, but just set new sensor_mode and resolution
        else:
            fg.camera.sensor_mode = fg.config[camdict]['sensor_mode']
            fg.camera.resolution = fg.config[camdict]['resolution']

    if rawCapture is None:
        logger.debug("Camprop_Use_Global=={} and update_condition=={}, but rawCapture didn't exist. Something odd is going on...".format(fg.config[camdict]['camProp_use_global'],update_condition))
        rawCapture = PiRGBArray(fg.camera, fg.config[camdict]['resolution'])
        logger.debug("Camera_Resolution=={}, rawCapture_resolution=={}, camera_sensor_mode=={}. Is this ok?".format(fg.camera.resolution,fg.config[camdict]['resolution'],fg.camera.sensor_mode))

    return camStats, rawCapture




# %%
# ----------------------------------- #
# @           algorithms            @ #
# ----------------------------------- #


def autofocus_routine(self, camStats=None):
    '''
    Prepares parameters for scanning, sets everything up and calls scanning and calculation routines. 
    Note:
        > scan_range: half of the total (symmetric) scanning distance
    '''
    # turn on light (so that Photon-flux can already be passively evaluated by Sensor)
    fg.ledarr.send("RECT+3+3+2+2+1", 200,200,200)
    #fio.update_matrix(self, ignore_NA=False, sync_only=False, pattern='CUS')
    sleep(fg.config['experiment']['i2c_send_delay'])

    # get parameters
    image_name_template, steps_coarse_dist, steps_coarse_nbr, scanrange_coarse, steps_fine_dist, steps_fine_nbr, scanrange_fine, pos_start, pos_max, pos_min, smethod, max_steps, imres, motor, save_im, NIterTotal, channel, use_scipy = autofocus_getParameters(self)

    # sanity-check Scanrange
    scanrange_coarse = autofocus_getRange(scanrange_coarse, pos_start, pos_min, pos_max)
    scanrange_fine = autofocus_getRange(scanrange_fine, pos_start, pos_min, pos_max)

    # initialize camera-properties and create Image-Buffer
    camStats = [] if camStats is None else camStats
    if fg.config['experiment']['active']:
        camera_bak = [fg.camera.sensor_mode, fg.camera.resolution]
    camStats, rawCapture = autofocus_setupCAM(camStats,camdict='cam_af')

    # leave light on
    #fg.ledarr.send("CLEAR")
    #fg.ledarr.send("CLEAR")
    #fg.ledarr.send("RECT", [1, 1, 6, 6], 1, [120,120,120])
    fg.ledarr.send("RECT+3+3+2+2+1", 200,200,200)
    sleep(fg.config['experiment']['i2c_send_delay'])

    # Coarse scan -> get coarse-sharpness measures + new position of motor
    sharpness_coarse, poslist, pos_coarse, tim, tproc, ttotal, wait_time = autofocus_scan(self, names=image_name_template, rawCapture=rawCapture, smethod=smethod, pos_start=pos_start, pos_min=pos_min, pos_max=pos_max, max_steps=max_steps, steps_nbr=steps_coarse_nbr, steps_dist=steps_coarse_dist, direction = 1, NIterTotal=NIterTotal,motor=motor, status='coarse', save_im=save_im, save_name=image_name_template)

    # Fit Gauss to graph and find new position of highest sharpness
    coarse_posOptimum, coarse_coeff, coarse_succs = autofocus_findOptimum(s=sharpness_coarse, offset=1, smethod=smethod, NIterTotal=NIterTotal, steps=steps_coarse_nbr , poslist=poslist, save_name=image_name_template, status='coarse', plotme=True, storeme=True, channel=channel, use_scipy=use_scipy)
    step_2opt_coarse = get_distvec(pos_coarse, coarse_posOptimum)

    # move to new center with z motor
    wait_time, pos_now  = autofocus_move_motor(self,stepsize=step_2opt_coarse,motor=motor,pos_now=pos_coarse,wait_time=wait_time)
    
    if not fg.config['autofocus']['use_coarse_only']:

        # fine scan around new position ->
        sharpness_fine, pos_fine = autofocus_scan(self, names=image_name_template, rawCapture=rawCapture, smethod=smethod, scan_range=scan_range_fine, pos_start=pos_optimum_coarse, pos_min=pos_min, pos_max=pos_max, max_steps=max_steps, save_im=save_im)

        sharpness, poslist, pos_fine, tim, tproc, ttotal = autofocus_scan(self, names=image_name_template, rawCapture=rawCapture, smethod=smethod, pos_start=pos_fine, pos_min=pos_min, pos_max=pos_max, max_steps=max_steps, steps_nbr=steps_coarse_nbr, steps_dist=steps_, direction = 1, NIterTotal=NIterTotal,motor=motor, status='coarse', save_im=save_im, save_name=image_name_template)

        # Fit Gauss to graph and find new position of highest sharpness
        fine_posOptimum, fine_coeff, fine_succs = autofocus_findOptimum(s=sharpness_coarse, offset=1, smethod=smethod, NIterTotal=NIterTotal, steps=steps_coarse_nbr , poslist=poslist, save_name=image_name_template, status='fine', plotme=True, storeme=True, channel=channel, use_scipy=use_scipy)
        step_2opt_fine = get_distvec(pos_fine, pos_optimum_coarse)

        # move to new center with z motor AND clear LED-array
        wait_time, pos_now  = autofocus_move_motor(self,stepsize=step_2opt_fine,motor=motor,pos_now=pos_fine,wait_time=wait_time)
    
    fg.ledarr.send("CLEAR")
    fg.ledarr.send("CLEAR")

    # clear camera to former properties
    if fg.config['experiment']['active']:
        fg.camera.sensor_mode = camera_bak[0]
        fg.camera.resolution = camera_bak[1]

    # done?
    return True


def get_distvec(a, b):
    '''
    Calculates signed distance two positions, where direction points from a to b. 
    '''
    return b - a



def autofocus_getParameters(self):
    '''
    Assignes variables to dict-entries for easier readability. 
    '''
    # generate image name
    image_name_template = autofocus_imagename_gen(self)

    # set correct number of iteration
    fg.config['experiment']['autofocus_num'] = 1 if fg.config['experiment']['autofocus_new'] else fg.config['experiment']['autofocus_num'] + 1

    # set parameters
    steps_coarse_dist = fg.config['autofocus']['step_dist_coarse']
    steps_coarse_nbr = fg.config['autofocus']['steps_coarse'] 
    steps_fine_dist = fg.config['autofocus']['step_dist_fine']
    steps_fine_nbr = fg.config['autofocus']['steps_fine']
    pos_start = fg.config['motor']['calibration_z_pos']
    pos_max = fg.config['motor']['calibration_z_max']
    pos_min = fg.config['motor']['calibration_z_min']
    smethod = fg.config['autofocus']['technique']
    max_steps = fg.config['autofocus']['max_steps'] 
    fg.config['cam_af']['resolution'] = fg.config['cam']['sensor_mode_size'][fg.config['cam_af']['sensor_mode']]
    imres = fg.config['cam_af']['resolution']
    motor = fg.config['autofocus']['motor']
    save_im = fg.config['autofocus']['save_images']
    NIterTotal = fg.config['autofocus']['scan_iterations']
    channel = fg.config['autofocus']['use_channel']
    use_scipy = fg.config['autofocus']['use_scipy']

    # calculate
    scanrange_coarse = steps_coarse_dist * steps_coarse_nbr
    scanrange_fine = steps_fine_dist * steps_fine_nbr

    return image_name_template, steps_coarse_dist, steps_coarse_nbr, scanrange_coarse, steps_fine_dist, steps_fine_nbr, scanrange_fine, pos_start, pos_max, pos_min, smethod, max_steps, imres, motor, save_im, NIterTotal, channel, use_scipy

def autofocus_scan(self, names, rawCapture, smethod, pos_start, pos_min, pos_max, max_steps, steps_nbr, steps_dist, direction, NIterTotal, motor, status='coarse', save_im=False, save_name=None):
    '''
    Implements modules of how to scan through the object and how to use/ check for backlash!

    :scan_methods:      0=slow Filter-based (DEFAULT), 1=fast Filter-based, 2=fast stream-size reading, 3=simulation

    TODO: 
        1) provide iteration limit NIter
    '''
    logger.debug("Autofocus ---> {} - Scanning.".format(status))

    # set parameters and variables
    m = 0
    scan_range = steps_dist * steps_nbr
    poslist = [pos_start,]
    pos_now = pos_start
    upd_val = 100 / (steps_nbr*NIterTotal)

    # prepare containers
    tim = []
    tproc = []
    sharpness = []
    timstart = time()
    ttotal = time()
    pos_now = pos_start
    wait_time = None

    # faster way to acquire images and especially ensure same illumination properties etc per image as opposed to long-warm ups for single captures
    for n in range(NIterTotal):

        # the loop
        sharpness, tproc, tim, pos_now, poslist, wait_time, m,rawCapture  = autofocus_image(self=self,rawCapture=rawCapture,sharpness=sharpness,smethod=smethod,motor=motor,direction=direction,pos_now=pos_now,poslist=poslist,scan_range=scan_range,steps_dist=steps_dist,steps_nbr=steps_nbr,m=m,n=n,NIterTotal=NIterTotal,wait_time=wait_time,timstart=timstart,tim=tim,tproc=tproc,save_name=save_name,status=status,save_im=save_im,upd_val=upd_val)

        # iterate the stack inversely 
        m=1
        direction *= -1
    ttotal = time() - ttotal

    # done?
    return sharpness, poslist, pos_now, tim, tproc, ttotal, wait_time

def fix_rawCapture():
    '''
    Decorator that fixes potential errors in call structure with PiRGBArray (eg rawCapture).
    Assumes that applied function provided kwargs via keyword.
    '''
    def decorate_me(func):
        def rawCapture_silencer(*args,**kwargs):
            try:
                return func(*args,**kwargs)
            except Exception as e:
                logger.debug(e)
                logger.warn("Continue image-acquisition, but with non-intended default setting of raspicam")
                rawCaptureNew = PiRGBArray(fg.camera, fg.camera.resolution)
                kwargs['rawCapture'] = rawCaptureNew
                return func(*args,**kwargs)
            return rawCapture_silencer
    return decorate_me


#@fix_rawCapture()
def autofocus_image(self,rawCapture,sharpness,smethod,motor,direction,pos_now,poslist,scan_range,steps_dist,steps_nbr,m,n,NIterTotal,wait_time,timstart,tim,tproc,save_name,status,save_im,upd_val):
    '''
    Calculations on image acquired.
    '''
    # to account for 3 steps we need  4 images ;)
    steps_nbr = steps_nbr + 1

    for frame in fg.camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
        image = frame.array

        # calculation
        tim.append(time() - timstart)
        logger.debug('Calculating image-sharpness with measure={} for image {}/{} in round {}/{} at MOTOR_POS={}.'.format(smethod,m,steps_nbr,n+1,NIterTotal,pos_now))
        sharpness, tproc = autofocus_getMeasure(image, sharpness, tproc)

        # if save
        if save_im:
            saven = "{}Image_{}-{}of{}.tif".format(save_name,status,str(n),str(m))
            tif.imwrite(saven, image, photometric='rgb')
            logger.debug("Store Autofocus-Image {}".format(saven))
        if m==0:
            # move motor to start
            step_2_start = get_distvec(pos_now, pos_now - direction* scan_range//2)
            wait_time, pos_now = autofocus_move_motor(self,stepsize=step_2_start,motor=motor,pos_now=pos_now, wait_time=None)
            poslist.append(poslist[-1]+step_2_start)
            logger.debug("Starting-image and measure taken for m==0 in first iteration.")
        elif m == steps_nbr:
            poslist.append(pos_now)
        else: 
            # move motor 1 step up
            wait_time, pos_now  = autofocus_move_motor(self,stepsize=direction*steps_dist,motor=motor,pos_now=pos_now,wait_time=wait_time)
            poslist.append(pos_now)
        # clear the stream in preparation for the next frame
        timstart = time()
        rawCapture.truncate(0)
        # update display
        autofocus_display_update(self, upd_val, m, steps_nbr, n, NIterTotal*(steps_nbr+1))

        # set counter
        m += 1
        if m > steps_nbr:
            break
    
    return sharpness, tproc, tim, pos_now, poslist, wait_time, m, rawCapture


def autofocus_getMeasure(im, sharpness, tproc):
    '''
    Calculates sharpness measure and returns value
    '''
    # calculate sharpness measure
    tprocstart = time()

    # pre-filter with a (coarse) Gauss-kernel to get rid of high-freq-noise
    im = gaussian_filter(im, 5) #convolve(image, mykernel)

    if fg.config['autofocus']['scan_method'] == 1:
         # (fast) sharpness Filter-based on canny
        #from skimage import filters
        #edges = filters.sobel(im)
        # Get x-gradient in "sx"
        #sx = ndimage.sobel(im,axis=0,mode='constant')
        # Get y-gradient in "sy"
        #sy = ndimage.sobel(im,axis=1,mode='constant')
        # Get square root of sum of squares
        #edges=np.hypot(sx,sy)
        mysharpness = np.std(im)
        sharpness.append(mysharpness)
    elif fg.config['autofocus']['scan_method'] == 2:
        # (fast) byte-stream reading based
        pass
    elif fg.config['autofocus']['scan_method'] == 3:
        # simulates sharpness stack and tests performance
        pass
    else:
        sharpness.append(fc.diff_tenengrad(np.reshape(im, [im.shape[-1], im.shape[-2], im.shape[-3]])))    
    tproc.append(time() - tprocstart)

    return sharpness, tproc

def autofocus_update_dict(found_focus, method, fine_range, fine_steps, fine_steps_size):
    fg.config['experiment']['autofocus_success'] = found_focus
    fg.config['autofocus']['method'] = method
    fg.config['autofocus']['fine_range'] = fine_range
    fg.config['autofocus']['fine_steps'] = fine_steps
    fg.config['autofocus']['fine_steps_size'] = fine_steps_size

'''
def autofocus_compare_refs(self, image_ref, _):
    # correlate
    # roughly same?
    pass


def autofocus_update_stacks(imqual_zpos, imqual_stack, imqualh):
    imqual_zpos = [imqual_zpos, fg.config['motor']['calibration_z_pos']]
    imqual_stack = [imqual_stack, imqualh]
    return imqual_zpos, imqual_stack
'''

def autofocus_move_motor(self,stepsize,motor,pos_now,wait_time=None):
    '''
    Moves motor accordingly. 
    '''
    
    # dict
    letter = ['x','y','z']
    name = ['DRVX','DRVY','DRVZ']

    # calculate proper waiting time
    if wait_time is None: 
        wait_time = fg.config['motor']['standard_move_time_'+letter[motor]] * \
            abs(stepsize) / fg.config['motor']['standard_move_dist_'+letter[motor]]

    # move and update config
    toolbox.move_motor(self=self, instance=None, motor_sel=motor, motor_stepsize=stepsize)
    #fg.config['motor']['calibration_'+letter[motor]+'_pos'] += stepsize
    pos_now +=stepsize

    # wait for movement to finish
    sleep(wait_time)

    return wait_time, pos_now


def autofocus_display_update(self, upd_val, myd, fine_steps, myc, iter_max, *largs):
    if (self.ids['pb_autofocus'].value < 100):
        # update toolbar
        self.ids['pb_autofocus'].value += upd_val
        logger.debug("Updated autofocus progressbar to {}".format(
            self.ids['pb_autofocus'].value))
        # update message-display
        #msg = "Autofocus: Step {}/{} in iteration {}/{}.".format(myd, fine_steps, myc, iter_max)
        #self.ids['lbl_warning'].text = msg
        #self.ids['user_notify_expt'].text = msg
    else:
        self.ids['pb_autofocus'].value = 0
        #self.ids['lbl_warning'].text = ""
        #self.ids['user_notify_expt'].text = ""


def autofocus_getRange(scanrange, pos_start, pos_min, pos_max):
    '''
    Checks for boundary violations with respect to the motor position, movement and limits. Scanrange is interpreted as full-range AND calculation tests from actual pos as center-position with respect to both-sided limits.

    :PARAM:
    =======
    :scanrange:     2 * of the scanning range that will symmetrically be stepped about
    :pos_start:      start-position of scan (=center)

    '''

    if scanrange == 0:
        # calculate maximum symmetric distance to borders from actual position
        scan_limits = [abs(get_distvec(pos_start, pos_min)), abs(get_distvec(pos_start, pos_max))]

        # select smaller distance
        scanrange = scan_limits[1] if (scan_limits[0] >
                                       scan_limits[1]) else scan_limits[0]
        scanrange = np.array(scanrange, dtype=int) 
    else:
        # check limits to not go over boundaries for motors
        if (pos_start + scanrange//2 > pos_max):
            scanrange = pos_max - pos_start
        if (pos_start - scanrange//2 < pos_min):
            scanrange = abs(get_distvec(pos_start, pos_min))

    return scanrange


def autofocus_getSteps(scan_range, steps, step_method=0):
    if step_method == 0:
        scan_steps = scan_range / steps
    return scan_steps


def autofocus_plotOptSearch(x,y,yfit,xrss,yfit_rss,smethod,name_im,nbr_dir,nbr_iter,status):
    '''
    Plots fit for optimum search. 
    
    '''
    import matplotlib.pyplot as plt
    fig1 = plt.figure()
    plt.plot(x, y, label='Meas.Data')
    plt.plot(x, yfit, label='Gauss-Fit.')
    plt.plot(xrss, yfit_rss, label='supersampled Gauss-Fit.')
    plt.xlabel('Absolut Motor Position')
    plt.ylabel('Sharpness Value normed StartingPos in [a.U.]')
    plt.title('Autofocus-Results using\nmetric={} at step={}/{}'.format(smethod, nbr_dir, nbr_iter))
    plt.legend()
    saven = "{}SharpnessFIT_{}_dir{}_iter{}.tif".format(name_im,status,str(nbr_dir),str(nbr_iter))
    plt.savefig(saven,dpi=300)
    logger.debug("Store Autofocus-Sharpness-Fit to {}".format(saven))


def autofocus_findOptimum(s, offset, smethod, NIterTotal, steps, poslist, save_name, status='coarse', plotme=True, storeme=True, channel=1, use_scipy=False): 
    '''
    Calculates optimum position given input parameters.
    Structure of s=Sharpness_list: 
        s[0] = reference image
        s[1:steps] = 1st direction scan
        s[steps:2*steps] = 2nd direction scan etc for amount of NIterTotal 
    poslist only provided for printme-option to actually evaluate positions.
    '''
    xlabel = 'motor-Pos'
    ylabel = 'sharpness'

    s1 = np.array(s)[:,channel]
    res = []
    xrssl = []
    yrssl = []

    for m in range(NIterTotal):
        ttotal = time()
        y = s1[offset+m*steps:offset+(m+1)*steps]
        x = poslist[offset+m*steps:offset+(m+1)*steps]

        try:
            try:
                p0 = None #[1., 0., 1.]
                coeff, xr, xn, xrss, yfit, yfit_rss = autofocus_curveFit(
                    x, y, p0, use_scipy)
                if all(coeff == p0):
                    p0l = [1., 0.]
                    succs = False
                else:
                    succs = True

            except RuntimeError as err:
                logger.debug("intercepted")
                logger.debug(err)
                # try linear fit again
                p0l = [1., 0.]
                if use_scipy:
                    from scipy.optimize import curve_fit
                    coeff, var_matrixl = curve_fit(
                    fitf_lin, x, y, p0=p0l)
                xr = [np.min(x), np.max(x), len(x)]
                xrss = x
                yrss = y
                yfit = y
                succs = False

            res.append(coeff)

            # save out dictionary:
            if storeme:    
                autofocus_res = {'z_Pos': x,
                                'sharpness': y,
                                'iteration': m,
                                'iteration_limit': NIterTotal,
                                'steps_nbr': xr[2],
                                'steps_dist': xr[1] - xr[0],
                                'backlash': fg.config['autofocus']['backlash'],
                                'im_taken_before': fg.config['experiment']['images_taken'],
                                'total_time': ttotal - time(),
                                'A,mu,sigma': coeff,
                                'success': succs,
                                }
                saven = "{}SharpnessFIT_{}_dir{}_of{}.npy".format(save_name,status,str(m),str(NIterTotal))
                np.save(saven, autofocus_res)
            if plotme:
                autofocus_plotOptSearch(x=x,y=y,yfit=yfit,xrss=xrss,yfit_rss=yfit_rss,smethod=smethod,name_im=save_name,nbr_dir=m+1,nbr_iter=NIterTotal,status=status)

            xrssl.append(xrss)
            yrssl.append(yfit_rss)
        except:
            logger.warn('FindOptimum broke -> was skipped and no output was produced for iteration {} of {}.'.format(m+1,NIterTotal))
            xrssl.append([])
            yrssl.append([])

    # position of highest contrast -> assure that its INT
    if fg.config['autofocus']['result_averaging']:
        res = np.array(res)
        try:
            pos_max = int(np.mean(res[:,1]))
        except Exception as e:
            logger.warn(e)
            resh = []
            for m in range(res.shape[0]):
                if len(res[m]) == 3:
                    resh.append(res[m][1])
                else:
                    if not yrssl[m] == []: 
                        resh.append(xrssl[m][np.argmax(yrssl[m])])
            
            # exclude values with too big difference
            try:
                mymask = [(abs(m / resh[0] - 1) < 0.05) for m in resh]
                pos_max = int(np.mean(resh[m]))
            except Exception as e: 
                logger.warn(e)
                pos_max = int(resh[0])
    else: 
        try:
            pos_max = int(res[1,1])
        except:
            pos_max = xlrss[np.argmax(ylrss)]
    #pos_max = xr[np.argmax(yfit)]
    #max_val = np.max(yfit)

    # done?
    return pos_max, coeff, succs

def autofocus_curveFit(x, y, p0, use_scipy):
    '''
    Actually courve-fitting routine for finding the maximum-position of sharpness-calculations.
    Calculates a normal fitted and a sub-sampled fit.

    :PARAMS:
    ========
    :x:     (LIST) Scan-positions
    :y:     (LIST) calculated sharpness measures


    :OUTPUT:
    ========
    :coeff: (LIST) of calculated coefficients (depending on fitting function)
    :xr:    xrange-parameters from input list
    :xn:    x-positions used for fitting
    :xrss:  sub-sampled x-positions for fitting
    :yn:    y-fitted values
    :yrss:  sub-sampled y-fitted values

    '''
    # we better normalize it to have one parameter fixed
    y-=np.min(y)
    y/=np.max(y)
    xr = [np.min(x), np.max(x), len(x)]

    # estimate the parameters according to a likely set
    if p0 is None:
        p0 = (1., np.mean(x), 3.) # A, mu, sigma
        print(p0)
    
    # whether to use scipy
    if use_scipy:
        from scipy.optimize import curve_fit
        coeff, var_matrix = curve_fit(fitf_gauss, x, y, p0=p0)  # coeff=[A, mu, sigma]
        logger.debug('Fitting for Focus-Stack found parameters {}'.format(coeff))
        a_fit = fitf_gauss(x, *coeff)  # Get the fitted curve
        xn = np.linspace(xr[0], xr[1], num=xr[2])
        xrss = np.linspace(xr[0], xr[1], num=xr[2] * 4)
        yn = fitf_gauss(xn, *coeff)  # Get the fitted curve
        yrss = fitf_gauss(xrss, *coeff)  # Get the fitted curve
    else:
        # using numpy and lstsq
        # coeff, var_matrix = np.linalg.lstsq(fitf_gauss, x, imqual_stack, p0=p0)  # coeff=[A, mu, sigma]
        #a = np.vstack([x, np.ones(len(x))]).T
        a = np.random.randn(100)
        fitp = np.polyfit(x, y, 2)
        xn = np.linspace(xr[0], xr[1], num=xr[2])
        xrss = np.linspace(xr[0], xr[1], num=xr[2] * 4)
        yn = np.polyval(fitp, xn)
        ynrss = np.polyval(fitp, xrss)
        coeff = [fitp[0], np.argmax(yn), fitp[2]]  # max-pos

    # format for gauss (type=0): A,mu,sigma
    return coeff, xr, xn, xrss, yn, yrss


#
#
# %%
# ----------------------------------- #
# @       function toolbox          @ #
# ----------------------------------- #


def fitf_gauss(x, *parameters):
    A, mu, sigma = parameters
    return A * np.exp(-(x - mu)**2 / (2. * sigma**2))


def fitf_lin(x, *parameters):
    m, b = parameters
    return m * x + b


def get_slope(x, y):
    # determine the slope of the current focus values
    # x is given by the steps
    # y is given by the measured contrast
    # x = np.array([0, 1, , 3])
    # y = np.array([-1, 0.2, 0.9, 2.1])
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    logger.debug(m, c)
    return m

def gauss_residual(updated_parameter, x, data):
    resid = fitf_gauss(x, updated_parameter) - data
    res = np.sum(np.square(resid))
    return res


def read_stack(file_names):
    rstack = np.array(imo.imread(file_names[0]))[np.newaxis]
    for myc in range(1, len(file_names)):
        rstack = np.concatenate(
            (rstack, np.array(imo.imread(file_names[myc]))[np.newaxis]), axis=0)
    return rstack


def autofocus_imagename_gen(self):
    '''
    Creates names for autofocus routine. 
    '''

    # CLONE from main.py "start_experiment"
    if not fg.started_first_exp:
        toolbox.scr_switch(self,self.ids['btn_start_expt'])
        fio.prepareFolder()
        fg.config['experiment']['active'] = 0

    # create name
    prename = 'Autofocus--{}--iter_{}--'.format(
        datetime.now().strftime("%Y%m%d_%H%M%S"), fg.config['experiment']['autofocus_num'])
    prename = path.join(fg.expt_path, prename)

    # done?
    return prename


def simulate_data_stack():
    open_dir = 'C:/Users/rene/Documents/Programming/matlab/Fluidi/swen/data/noise-data-01/'
    open_file = glob(open_dir + '*.tif')
    data_stack = read_stack(open_file)
    imqual_res = [imqual_metric(data_stack[0, :, :], method='Tenengrad')]
    for myc in range(1, data_stack.shape[0]):
        imqual_res = np.concatenate((imqual_res, [imqual_metric(
            data_stack[myc, :, :], method='Tenengrad')]), axis=0)
    step_sizes = np.arange(41) / 8.0
    return step_sizes, imqual_res

# %% Deprecated

def notify_deprecation_decorator(func):
    def func_wrapper(*args,**kwargs):
        logger.debug('<DEPRECATED> Function: {} called.'.format(func.__name__))    
        return func(*args,**kwargs)
    return func_wrapper

@notify_deprecation_decorator
def find_focus(names, method, imqual_zpos, imqual_stack, myc=0, max_iter=2):
    
    xunit = 'pix'
    method = 'Tenengrad'
    # test gaussian -> from: https://stackoverflow.com/a/11507723
    from timeit import default_timer as timer
    tstart = timer()
    # -------
    try:
        p0 = [1., 0., 1.]
        # coeff, var_matrix = curve_fit(fitf_gauss, bin_centres, hist, p0=p0)
        coeff, xr, xn, xrss, a_fit, a_fit_rss = autofocus_curveFit(
            imqual_zpos, imqual_stack, p0, 1)
        if all(coeff == p0):
            p0l = [1., 0.]
            #coeff, var_matrixl = curve_fit(fitf_lin, imqual_zpos, imqual_stack, p0=p0l)
            # a_fitl = fitf_lin(imqual_zpos, *coeff)  # Get the fitted curve
            #plt.plot(imqual_zpos, a_fitl, label='Lin. Fitted data')
            succs = False
        else:
            succs = True
        #plt.plot(imqual_zpos, imqual_stack, label='Meas.Data')
        #plt.plot(imqual_zpos, a_fit, label='Gauss-Fit.')
        #plt.plot(xrss, a_fit_rss, label='supersampled Gauss-Fit.')
        #plt.xlabel('Absolut Motor Position in [{0}]'.format(xunit))
        #plt.ylabel('Sharpness Value normed StartingPos in [a.U.]')
        #plt.title('Autofocus-Results using\nmetric={0} at step={1}/{2}'.format(method, myc, max_iter))
        # plt.legend()
        # plt.show()
        #plt.savefig(names+'Autofocus-{0}-myc_{1}'.format(names, myc))
    except RuntimeError as err:
        logger.debug("intercepted")
        logger.debug(err)
        # try linear fit again
        p0l = [1., 0.]
        coeff, var_matrixl = curve_fit(
            fitf_lin, imqual_zpos, imqual_stack, p0=p0l)
        succs = False
        # try modifications on input data-set
        # but cut autofocus for now
    tend = timer()
    # save out dictionary:
    autofocus_res = {'z_Pos': imqual_zpos,
                     'sharpness': imqual_stack,
                     'iteration': myc,
                     'iteration_limit': max_iter,
                     'fine_steps': xr[2],
                     'fine_steps_dist': xr[1] - xr[0],
                     'backlash': fg.config['autofocus_properties']['backlash'],
                     'im_taken_before': fg.config['experiment']['images_taken'],
                     'total_time': tstart - tend,
                     'A,mu,sigma': coeff,
                     'success': succs,
                     }
    np.save('{}-iter_{}-results.npy'.format(myc, names), autofocus_res)
    #d2 = np.load('autofocus_res-20190327_0917.npy')
    return imqual_zpos[np.argmax(imqual_stack)], np.max(imqual_stack), coeff[0], coeff[1], succs

@notify_deprecation_decorator
def autofocus_take_image(self, image_name_template, method):
    imvar = 0
    mythresh = 0.005  # has to be adjusted again
    myc = 0
    eps = 0.00001
    image_stack = []
    imvar_stack = []
    # neutralize with prior image to have more averaging? -> NOT IMPLEMENTED
    # take again if variance is too small until limit
    while (imvar < mythresh or myc == 4):
        image = toolbox.take_image(self, 'autofocus', image_name_template)
        # normalize image to reside in [0,1]
        help_image = image - np.min(image)
        help_image[help_image == 0] = eps
        help_image /= np.max(help_image)
        imvar = np.var(help_image)
        myc += 1
    image_stack = [image_stack, image, ]
    imvar_stack = [imvar_stack, imvar, ]
    # calc_image_quality -> TENENGRAD for now
    logger.debug("autofocus_take_image -> myc={}".format(myc))
    if myc == 4:
        # note: stack was created as list of arrays! -> so: access array
        image = image_stack[np.argmax(imvar_stack)]
    imqual_res = imqual_metric(image, method=method)
    return image, imqual_res