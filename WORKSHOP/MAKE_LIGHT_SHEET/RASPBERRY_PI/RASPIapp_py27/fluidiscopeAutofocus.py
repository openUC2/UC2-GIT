# implements the autofocus based on paper: ...

# own imports
import fluidiscopeGlobVar as fg
import fluidiscopeToolbox as toolbox
# general imports
import unipath as uni
from datetime import datetime
#import cv2
from os import listdir
from glob import glob
# math toolboxes
import numpy as np
#import scipy.fftpack as ftp
#from scipy.optimize import curve_fit
#import matplotlib.pyplot as plt
from PIL import Image
from time import sleep


if not fg.my_dev_flag:
    from picamera.array import PiRGBArray
else:
    import imageio as imo

#
#
# %%
# ----------------------------------- #
# @       interface toolbox         @ #
# ----------------------------------- #
def autofocus_callback(self,instance,*rargs):
    # flags
    # set autofocus busy! -> calls from measurement-callback will be skipped until set to false again
    fg.config['experiment']['is_autofocus_busy'] = True
    print("Autofocus-03a- config->experiment->is_autofocus_busy={}".format(fg.config['experiment']['is_autofocus_busy']))
    # run autofocus routine
    print("Autofocus-03b- autofocus_callback in fluidiscopeAutofocus.py started.")
    fg.config['experiment']['imaging_method']='AF'
    autofocus_routine(self)
    # simulation datastack
    # x_positions, calc_im_qual = simulate_data_stack()
    fg.config['experiment']['is_autofocus_busy'] = False
    print("Autofocus-03c- config->experiment->is_autofocus_busy={}".format(fg.config['experiment']['is_autofocus_busy']))
#
#
# %%
# ----------------------------------- #
# @       algorithm toolbox          @ #
# ----------------------------------- #
def autofocus_routine(self):
    # parameters
    method = 'Tenengrad'
    #generate image name
    image_name_template = autofocus_imagename_gen()
    # now take images with alternating step sizes and distances -> calc res image-metric -> interpolate
    fg.config['experiment']['autofocus_iteration'] = 0
    print("Autofocus-04- autofocus_routine reached.")
    imqual_stack = autofocus_scan(self,names=image_name_template,method='Tenengrad',scan_method=0,fine_range=fg.config['autofocus']['fine_range'],fine_steps=fg.config['autofocus']['fine_steps'],iter_max=fg.config['autofocus']['iter_max'],corr_test=fg.config['autofocus']['corr_test'])


def autofocus_scan(self,names='nonamegiven',method='Tenengrad',scan_method=0,fine_range=0,fine_steps=9,iter_max=2,corr_test=0):
    '''
    Implements modules of how to scan through the object and how to use/ check for backlash!
    :param fine_range: marks range into 1 movement-direction (e.g. towards minus)
    :return:
    '''
    print("Autofocus-05a- autofocus_scan reached.")
    # set parameters and variables
    imqual_stack = []
    imqual_zpos = []
    found_focus = False
    myc = 0
    scan_offset = 0
    if scan_method==0: # default method -> just some steps
        # 1. take image at start position
        # 2. go to minimum position -> scan stepwise to maximum (taking an image at the start position again)
        # 3. at each step calculate metric (and correlation if corr_test is 1)
        # 4. repeat if not best position was found
        # 5. save resulting graphs
        # ------------------------------------------------
        # find range
        fine_range = autofocus_getRange(fine_range,fg.config['motor']['calibration_z_pos'])
        fine_steps_size = autofocus_getSteps(fine_range,fine_steps, step_method=0)
        image_ref, imqual_ref = autofocus_take_image(self, image_name_template=names, method=method) #==1.
        upd_val = 100/(fine_steps*iter_max)
        while not (found_focus or myc >= iter_max or fine_range == 0):
            autofocus_move_motor(-fine_range + scan_offset)
            _, imqualh = autofocus_take_image(self, image_name_template=names, method=method)
            imqual_zpos, imqual_stack = autofocus_update_stacks(imqual_zpos, imqual_stack, imqualh)
            for myd in range(1,fine_steps):
                print("Autofocus-05b- autofocus_scan- step {} / {} in routine {} / {}.".format(myd,fine_steps,myc,iter_max))
                autofocus_move_motor(fine_steps_size)
                _, imqualh = autofocus_take_image(self, image_name_template=names, method=method)
                if myd == fine_steps/2: # information gain not yet used in code -> later: use to correct for backlash
                    refcomp_res = autofocus_compare_refs(image_ref,_)
                imqual_zpos, imqual_stack = autofocus_update_stacks(imqual_zpos, imqual_stack, imqualh)
                autofocus_display_update(self, upd_val, myd, fine_steps, myc, iter_max)
            imqual_max_zpos, imqual_max_val,imqual_fit_maxAmplitude,imqual_fit_centerZpos,found_focus = find_focus(imqual_zpos,imqual_stack)
            # move to max position
            autofocus_move_motor(imqual_fit_centerZpos - fg.config['motor']['calibration_z_pos'])
        autofocus_update_dict(found_focus,method,fine_range,fine_steps,fine_steps_size)
    else:
        print("Not implemented method for Autofocus chosen. Hence: Idly waiting.")


def autofocus_update_dict(found_focus,method,fine_range,fine_steps,fine_steps_size):
    fg.config['autofocus']['success'] = found_focus
    fg.config['autofocus']['method'] = method
    fg.config['autofocus']['fine_range'] = fine_range
    fg.config['autofocus']['fine_steps'] = fine_steps
    fg.config['autofocus']['fine_steps_size'] = fine_steps_size


def autofocus_compare_refs(self,image_ref,_):
    # correlate
    # roughly same?
    pass


def autofocus_update_stacks(imqual_zpos,imqual_stack,imqualh):
    imqual_zpos = [imqual_zpos, fg.config['motor']['calibration_z_pos']]
    imqual_stack = [imqual_stack, imqualh]
    return imqual_zpos, imqual_stack


def autofocus_move_motor(stepsize):
    wait_time = fg.config['motor']['standard_move_time_z'] * stepsize / fg.config['motor']['standard_move_dist_z']
    fg.motors.send("DRVZ", stepsize)
    fg.config['motor']['calibration_z_pos'] += stepsize
    # wait for movement to finish
    sleep(wait_time)


def autofocus_display_update(self,upd_val,myd,fine_steps,myc,iter_max,*largs):
    if (self.ids['pb_autofocus'].value < 100):
        # update toolbar
        self.ids['pb_autofocus'].value += upd_val
        print("Updated autofocus progressbar to {}".format(self.ids['pb_autofocus'].value))
        # update message-display
        msg = "Autofocus: Step {}/{} in iteration {}/{}.".format(myd, fine_steps, myc, iter_max)
        self.ids['lbl_warning'].text = msg
        self.ids['user_notify_expt'].text = msg
    else:
        self.ids['pb_autofocus'].value = 0
        self.ids['lbl_warning'].text = ""
        self.ids['user_notify_expt'].text = ""


def autofocus_getRange(fine_range,scan_startpos):
    if fine_range == 0:
        scan_limits = [scan_startpos - fg.config['motor']['calibration_z_min'],
                       fg.config['motor']['calibration_z_min'] - scan_startpos]
        fine_range = scan_limits[1] if (scan_limits[0]) > (scan_limits[1]) else scan_limits[0]
        fine_range /= 2  # only half it and
    else:
        if (scan_startpos + fine_range > fg.config['motor']['calibration_z_max']):
            fine_range = fg.config['motor']['calibration_z_max'] - scan_startpos
        if (scan_startpos - fine_range < fg.config['motor']['calibration_z_min']):
            fine_range = scan_startpos - fg.config['motor']['calibration_z_min']
    return fine_range


def autofocus_getSteps(fine_range,fine_steps,step_method=0):
    if step_method == 0:
        scan_steps = fine_range / fine_steps
    return scan_steps


def autofocus_curveFit(imqual_zpos,imqual_stack,p0,type):
    xr = [np.min(imqual_zpos), np.max(imqual_zpos), len(imqual_zpos)]
    if type==0:
        if 0:
            coeff, var_matrix = curve_fit(fitf_gauss, imqual_zpos, imqual_stack, p0=p0)  # coeff=[A, mu, sigma]
        else:
            coeff=p0
        a_fit = fitf_gauss(imqual_zpos, *coeff)  # Get the fitted curve
        xn = np.linspace(xr[0], xr[1], num=xr[2])
        xrss = np.linspace(xr[0], xr[1], num=xr[2]*4)
        yn = fitf_gauss(xn, *coeff)  # Get the fitted curve
        yrss = fitf_gauss(xrss, *coeff)  # Get the fitted curve
    elif type==1:
        #using numpy and lstsq
        #coeff, var_matrix = np.linalg.lstsq(fitf_gauss, imqual_zpos, imqual_stack, p0=p0)  # coeff=[A, mu, sigma]
        #a = np.vstack([imqual_zpos, np.ones(len(imqual_zpos))]).T
        a = np.random.randn(100)
        fitp = np.polyfit(imqual_zpos, fitf_gauss, 2)
        xn = np.linspace(xr[0], xr[1], num=xr[2])
        xrss = np.linspace(xr[0], xr[1], num=xr[2] * 4)
        yn = np.polyval(fitp, xn)
        yn = np.polyval(fitp, xrss)
        coeff = [fitp[0],np.argmax(yn),fitp[2]] #max-pos
    else:
        pass
    return coeff,xr,xn,xrss,yn,yrss #format for gauss (type=0): A,mu,sigma

def find_focus(names,method,imqual_zpos,imqual_stack,myc=0,max_iter=2):
    xunit = 'pix'
    method = 'Tenengrad'
    # test gaussian -> from: https://stackoverflow.com/a/11507723
    from timeit import default_timer as timer
    tstart = timer()
    # -------
    try:
        p0 = [1., 0., 1.]
        # coeff, var_matrix = curve_fit(fitf_gauss, bin_centres, hist, p0=p0)
        coeff,xr,xn,xrss,a_fit,a_fit_rss=autofocus_curveFit(imqual_zpos, imqual_stack, p0, 1)
        if all(coeff == p0):
            p0l = [1., 0.]
            #coeff, var_matrixl = curve_fit(fitf_lin, imqual_zpos, imqual_stack, p0=p0l)
            #a_fitl = fitf_lin(imqual_zpos, *coeff)  # Get the fitted curve
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
        #plt.legend()
        #plt.show()
        #plt.savefig(names+'Autofocus-{0}-myc_{1}'.format(names, myc))
    except RuntimeError as err:
        print("intercepted")
        print(err)
        # try linear fit again
        p0l = [1., 0.]
        coeff, var_matrixl = curve_fit(fitf_lin, imqual_zpos, imqual_stack, p0=p0l)
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
                     'fine_steps_dist': xr[1]-xr[0],
                     'backlash': fg.config['autofocus_properties']['backlash'],
                     'im_taken_before': fg.config['experiment']['images_taken'],
                     'total_time': tstart - tend,
                     'A,mu,sigma': coeff,
                     'success': succs,
                     }
    np.save('{}-iter_{}-results.npy'.format(myc,names), autofocus_res)
    #d2 = np.load('autofocus_res-20190327_0917.npy')
    return imqual_zpos[np.argmax(imqual_stack)],np.max(imqual_stack),coeff[0],coeff[1],succs
#
#
# %%
# ----------------------------------- #
# @       function toolbox          @ #
# ----------------------------------- #
def imqual_metric(image,method='Tenengrad'):
    if method == 'Tenengrad':
        offsets = [2,image.shape[0],2,image.shape[1]]
        # calculate shifted subsets of images
        I_xp1_ym1 = image[offsets[0]-2:offsets[1]-2,offsets[2]:offsets[3]]
        I_xp1_y0 = image[offsets[0] - 1:offsets[1] - 1, offsets[2] :offsets[3]]
        I_xp1_yp1 = image[ offsets[0] :offsets[1] , offsets[2] :offsets[3]]
        I_x0_ym1 = image[offsets[0] - 2:offsets[1] - 2, offsets[2] - 1:offsets[3] - 1]
        I_x0_y0 = image[offsets[0] - 1:offsets[1] - 1, offsets[2] - 1:offsets[3] - 1]
        I_x0_yp1 = image[offsets[0]:offsets[1], offsets[2] - 1:offsets[3] - 1]
        I_xm1_ym1 = image[offsets[0]-2:offsets[1]-2,offsets[2]-2:offsets[3]-2]
        I_xm1_y0 = image[offsets[0] - 1:offsets[1] - 1, offsets[2] - 2:offsets[3] - 2]
        I_xm1_yp1 = image[offsets[0]:offsets[1], offsets[2] - 2:offsets[3] - 2]
        # sobel-filter to implement crossed derivatives
        Sobel_h = I_xp1_ym1 + 2 * I_xp1_y0 + I_xp1_yp1 - I_xm1_ym1 - 2 * I_xm1_y0  - I_xm1_yp1
        Sobel_v =I_xm1_yp1 + 2 * I_x0_yp1 + I_xp1_yp1 - I_xm1_ym1 - 2 * I_x0_ym1  - I_xp1_ym1
        # normalize image
        imqual_result = 1.0 / np.prod(np.shape(I_xp1_ym1)) * np.sum(np.square(Sobel_h)+np.square(Sobel_v),axis=(0,1))
    else:
        pass
    return imqual_result

def read_stack(file_names):
    rstack = np.array(imo.imread(file_names[0]))[np.newaxis]
    for myc in range(1, len(file_names)):
        rstack = np.concatenate((rstack,np.array(imo.imread(file_names[myc]))[np.newaxis]),axis=0)
    return rstack

def fitf_gauss(x, *parameters):
    A, mu, sigma = parameters
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

def fitf_lin(x,*parameters):
    m,b = parameters
    return m*x+b

def get_slope(x, y):
    # determine the slope of the current focus values
    # x is given by the steps
    # y is given by the measured contrast
    # x = np.array([0, 1, , 3])
    # y = np.array([-1, 0.2, 0.9, 2.1])
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    print(m, c)
    return m

#
def gauss_residual(updated_parameter,x,data):
    resid = fitf_gauss(x,updated_parameter) - data
    res = np.sum(np.square(resid))
    return res


def residual_derivative(updated_data,static_data,data):
    pass


def autofocus_imagename_gen():
    now = str(datetime.now().strftime("%Y%m%d_%H%M%S"))
    image_name_template = '{}-Autofocus_it_{}-'.format(now, fg.config['experiment']['autofocus_iteration'])
    return image_name_template


def autofocus_take_image(self, image_name_template,method):
    imvar = 0
    mythresh = 0.005 #has to be adjusted again
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
        help_image[help_image==0] = eps
        help_image /= np.max(help_image)
        imvar = np.var(help_image)
        myc+=1
    image_stack = [image_stack,image,]
    imvar_stack = [imvar_stack,imvar,]
    # calc_image_quality -> TENENGRAD for now
    print("autofocus_take_image -> myc={}".format(myc))
    if myc == 4:
        image = image_stack[np.argmax(imvar_stack)] #note: stack was created as list of arrays! -> so: access array
    imqual_res = imqual_metric(image, method=method)
    return image, imqual_res

def simulate_data_stack():
    open_dir = 'C:/Users/rene/Documents/Programming/matlab/Fluidi/swen/data/noise-data-01/'
    open_file = glob(open_dir + '*.tif')
    data_stack = read_stack(open_file)
    imqual_res = [imqual_metric(data_stack[0, :, :], method='Tenengrad')]
    for myc in range(1, data_stack.shape[0]):
        imqual_res = np.concatenate((imqual_res, [imqual_metric(data_stack[myc, :, :], method='Tenengrad')]), axis=0)
    step_sizes = np.arange(41) / 8.0
    return step_sizes, imqual_res

