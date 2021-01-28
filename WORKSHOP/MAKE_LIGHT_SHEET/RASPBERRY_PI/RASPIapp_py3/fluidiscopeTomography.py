'''
Module that contains the tomography code.
'''
from fluidiscopeLogging import logger_createChild
import fluidiscopeGlobVar as fg
import fluidiscopeToolbox as toolbox
import fluidiscopeIO as fio


logger = logger_createChild('tomography','UC2')


# ----------------------------------------------------------------
#                      Tomographic-Functions


def tomography_callback(self):
    '''
    Real image acquisition-routine for tomographd mode. 
    '''
    # parameters
    nbr_steps = fg.config['tomo']['steps']+1
    fg.config['tomo']['done'] = False

    # get update (motor-movement direction)
    fg.config['tomo']['direction'] = -1 if fg.config['tomo']['posSTART'] >= fg.config['tomo']['posEND'] else 1
    if  fg.config['tomo']['posSTART'] ==  fg.config['tomo']['posEND']:
        logger.warning("Start and END-Pos are the same hence the system will take {} images at the same position.".format(nbr_steps))

    # iterate through tomography stack
    for imnbr in range(fg.config['tomo']['steps']+1):
        # actualize global number
        fg.config['tomo']['step_number'] = imnbr

        # to update measurement numbers indirectly
        if imnbr == fg.config['tomo']['steps']:
            fg.config['tomo']['done'] = True

        # take image with selected method
        toolbox.take_image(self)

        # move to next position 
        toolbox.move_motor(self, instance=None, motor_sel=fg.config['tomo']['motor'],
                motor_stepsize=fg.config['tomo']['stepsize'])

    

def tomography_btn_logic(self, instance):
    '''
    Additional Click-logic of the tomography-page is contained here.
    '''

    # lists of different button-logic-elements
    btns_motor = [self.ids['tomo_btn_mot_sel_' + str(m)].uid for m in range(3)]
    btns_pos = [self.ids['tomography_btn_set_pos_start'].uid,self.ids['tomography_btn_set_pos_end'].uid]
    btns_stepTime = [self.ids['tomo_btn_steps'].uid,self.ids['tomo_btn_time'].uid]
    btns_setpos = [self.ids['tomo_btn_set_' + str(m)].uid for m in range(4)]

    # logic-selector-------------------
    # change selected motor
    if instance.uid in btns_motor:
        fg.config['tomo']['motor'] = fg.config['motor']['motor_dict'][btns_motor.index(instance.uid)]

    # set start/end-position for tomo-stack
    elif instance.uid in btns_pos:
        motor_letter = {"DRVX":'x',"DRVY":'y',"DRVZ":'z'}[fg.config['tomo']['motor']]
        if btns_pos.index(instance.uid) == 0: 
            fg.config['tomo']['posSTART'] = fg.config['motor']['calibration_'+ motor_letter +'_pos']
        else: 
            fg.config['tomo']['posEND'] = fg.config['motor']['calibration_'+ motor_letter + '_pos']
        
        # update total distance on change of start and end
        fg.config['tomo']['total_dist'] = fg.config['tomo']['posEND'] - fg.config['tomo']['posSTART']
        
    # select whether time or step-number shall be changed
    elif instance.uid in btns_stepTime:
        #if self.ids['tomo_toggleGroup_stepTime'].current_active == 0:
        fg.config['tomo']['steptime_active'] = btns_stepTime.index(instance.uid)

    # change value of step-number or time per step
    elif instance.uid in btns_setpos:
        if fg.config['tomo']['steptime_active'] == 0:
            # update step value
            update_val = int(instance.value)
            fg.config['tomo']['steps'] += update_val 
            
            # update distance per step
            fg.config['tomo']['stepsize'] = int(fg.config['tomo']['total_dist'] / fg.config['tomo']['steps'])
        else: 
            update_val = int(instance.value)/10
            fg.config['tomo']['steptime'] = round(fg.config['tomo']['steptime'] + update_val,1)
        
    # (de-)activate TOMO-measurement (as individual option to each measurement)
    elif instance.uid == self.ids['btn_imaging_technique_tomography'].uid:
        fg.config['experiment']['tomo_active'] = False if instance.fl_active else True
        logger.debug('Tomo_mode active? {}.'.format(fg.config['experiment']['tomo_active']))
        toolbox.change_activation_status(instance)
    
    # update labels
    tomography_update_labels(self)
    

def tomography_update_labels(self):
    '''
    Updates label-entries below
    '''
    config_base = fg.config['tomo']
    update_base = 'tomography_lbl_'
    update_dict = ['motor','posSTART','posEND','steps','stepsize','steptime']

    for m in update_dict:
        self.ids[update_base + m].text = str(config_base[m])

    

