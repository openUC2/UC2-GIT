# Fluidiscope Toolbox
import fluidiscopeGlobVar as fg
import fluidiscopeIO
import fluidiscopeInit
import fluidiscopeAutofocus as af
# python packages
import warnings
from datetime import datetime
import time
import re
import glob
import os
import io
import sys
import unipath as uni
from distutils.dir_util import copy_tree
import shutil
if os.name == 'nt':
    pass
else:
    import usb
    #import cv2 as cv
    from PIL import Image
import numpy as np
from fractions import Fraction
from kivy.clock import Clock
from functools import partial
from math import floor
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.utils import platform
from kivy.uix.listview import ListView
from kivy.uix.listview import ListItemButton
from kivy.adapters.listadapter import ListAdapter

if not (fg.my_dev_flag):
    from I2CDevice import I2CDevice
    from picamera.array import PiRGBArray
    from picamera import PiCamera

# define color variables
button_color_active = [0.0, 4.0, 0.0, 1.0]
button_color_inactive = [0.5, 0.5, 0.5, 1.0] #, [1.0, 1.0, 1.0, 1.0]]
button_color_disabled = [0.1, 0.1, 0.1, 1.0]
button_color_caution = [0.6, 0.0, 0.0, 1.0]
button_fontcolor_inactive = [1.0, 1.0, 1.0, 1.0]
button_fontcolor_active = [0.0, 0.0, 0.0, 1.0]

# TODO: FIX IT!
fg.expt_num = 1


##########################
#                        #
# == SCREEN BEHAVIOUR == #
#                        #
##########################

# Switch Screen behaviour
def scr_switch(self, instance):
    # switch to Screen_Imaging
    if self.ids["btn_start_expt"].uid == instance.uid:
        self.ids["sm"].current = 'scr_imaging'
        self.ids["btn_scr_name"].text = 'IMA\nGING'
        fg.started_first_exp = 1
    elif self.ids["btn_new_expt"].uid == instance.uid:
        self.ids["sm"].current = 'scr_start'
        self.ids["btn_scr_name"].text = 'STA\nRT'
    # switch to Screen_Options
    elif self.ids["btn_menu_opt"].uid == instance.uid:
        #jumped over, because unnecessary extra click (!!)
        self.ids["sm"].current =  'scr_opt' #'scr_opt_check'
        self.ids["btn_scr_name"].text = 'OPT\nIONS\n:D' # 'OPT\nIONS\n?'
    elif self.ids["btn_menu_opt_checked"].uid == instance.uid:
        self.ids["sm"].current = 'scr_opt'
        self.ids["btn_scr_name"].text = 'OPT\nIONS\n:D'
        self.ids["btn_menu_opt_checked"].disabled = True
        self.ids['btn_menu_opt_enable'].disabled = False
        self.ids['btn_menu_opt_back_to_main'].disabled = False
    # switch to Screen_Imaging
    elif (self.ids["btn_menu_main"].uid == instance.uid or self.ids["btn_menu_opt_back_to_main"].uid == instance.uid or
          self.ids['scr_copy_2_back_main'].uid == instance.uid):
        if fg.started_first_exp:
            self.ids["sm"].current = 'scr_imaging'
            self.ids["btn_scr_name"].text = 'IMA\nGING'
        else:
            self.ids["sm"].current = 'scr_start'
            self.ids["btn_scr_name"].text = 'STA\nRT'
    elif self.ids["btn_menu_help"].uid == instance.uid:
        self.ids["sm"].current = 'scr_help'
        self.ids["btn_scr_name"].text = 'HE\nLP'
    # menu-buttons
    ##
    ###
    elif self.ids["btn_light_set_1"].uid == instance.uid:
        self.ids["sm"].current = 'scr_light_set_1'
        self.ids["btn_scr_name"].text = 'LI\nGHT\nOPT\n1'
    elif self.ids["btn_light_set_2"].uid == instance.uid:
        self.ids["sm"].current = 'scr_light_set_2'
        self.ids["btn_scr_name"].text = 'LI\nGHT\nOPT\n2'
        fluidiscopeIO.settings_save_restore(self, instance, True)
    elif self.ids["btn_cam_set_1"].uid == instance.uid:
        self.ids["sm"].current = 'scr_cam_set_1'
        self.ids["btn_scr_name"].text = 'CAM\nERA\nOPT\n1'
        fluidiscopeIO.settings_save_restore(self, instance, True)
    elif self.ids["btn_cam_set_2"].uid == instance.uid:
        self.ids["sm"].current = 'scr_cam_set_2'
        self.ids["btn_scr_name"].text = 'CAM\nERA\nOPT\n2'
        fluidiscopeIO.settings_save_restore(self, instance, True)
    elif self.ids["btn_imaging_set"].uid == instance.uid:
        self.ids["sm"].current = 'scr_imaging_set'
        self.ids["btn_scr_name"].text = 'IMA\nGIN\nG\nOPT'
        fluidiscopeIO.settings_save_restore(self, instance, True)
    elif self.ids["btn_motor_set"].uid == instance.uid:
        self.ids["sm"].current = 'scr_motor_set'
        self.ids["btn_scr_name"].text = 'MO\nTOR\nOPT'
        fluidiscopeIO.settings_save_restore(self, instance, True)
    elif self.ids["btn_autofocus_set"].uid == instance.uid or self.ids["btn_autofocus_opt"].uid == instance.uid:
        if self.ids["sm"].current == 'scr_autofocus_set':
            self.ids["sm"].current = 'scr_autofocus_set'
        else:
            self.ids["sm"].current = 'scr_autofocus_set'
            self.ids["btn_scr_name"].text = 'AUT\nOFO\nCUS'
        fluidiscopeIO.settings_save_restore(self, instance, True)
    # special buttons
    ##
    ###
    elif self.ids["btn_copy"].uid == instance.uid:
        #self.ids["sm"].current = 'scr_copy_1'
        #self.ids["btn_scr_name"].text = 'COPY\nDATA\n1'
        pass
    elif self.ids["btn_copy_1"].uid == instance.uid:
        #self.ids["sm"].current = 'scr_copy_2'
        #self.ids['scr_copy_2_progressbar'].value = 0
        #self.ids['scr_copy_2_status_lbl'].text = ''
        #self.ids["btn_scr_name"].text = 'COPY\nDATA\n2'
        #self.ids['scr_copy_2_delete_check'].active = False

        # print(self.ids['show_selected_path'].text)
        #if len(self.ids['scr_copy_1_filechooser'].selection) > 0:
        #    fg.copy_path = self.ids['scr_copy_1_filechooser'].selection[0]
        #else:
        #    pass
        pass

    elif self.ids["scr_copy_2_back_copy"].uid == instance.uid:
        #self.ids["sm"].current = 'scr_copy_1'
        #self.ids["btn_scr_name"].text = 'COPY\nDATA\n1'
        pass


def unlock_options(self, instance):
    if self.ids['btn_menu_opt_enable'].uid == instance.uid:
        self.ids['btn_menu_opt_checked'].disabled = False
        self.ids['btn_menu_opt_enable'].disabled = True
        self.ids['btn_menu_opt_back_to_main'].disabled = True


def settings_back(self):
    self.ids["sm"].current = 'scr_opt'
    self.ids["btn_scr_name"].text = 'OPT\nIONS\n:D'


##########################
#                        #
# ==   SCREEN BUILD   == #
#                        #
##########################


##########################
#                        #
# == BUTTON MANAGEMENT == #
#                        #
##########################

# checks, whether actual button is active
def check_active(instance):
    try:
        if instance.fl_active:
            return True
        else:
            return False
    except:
        print("{0} has no fl_active".format(instance.uid))

# activates [1] and deactivates [0] an element
def change_activation_status(instance):
    if check_active(instance):
        change_color(instance,status=instance.fl_active)
        instance.fl_active = False
    else:
        change_color(instance, status=instance.fl_active)
        instance.fl_active = True

def change_color(instance,status=True):
    # define color
    if status:
        instance.background_color = button_color_inactive
        instance.color = button_fontcolor_inactive
    else:
        if sum(instance.fl_value) > 0:
            instance.background_color = instance.fl_value
        else:
            instance.background_color = button_color_active
        instance.color = button_fontcolor_active

def activate(instance):
    if not check_active(instance):
        change_activation_status(instance)


def deactivate(instance):
    if check_active(instance):
        try:
            print("Is active. Deactivating Button: {0}".format.instance.text)
        except Exception as e:
            pass
        change_activation_status(instance)


# chain of activation commands
def change_activation_status_chain(self, *args):
    for myC in range(len(args)):
        change_activation_status(self.ids[args[myC]])


def warn_dev_mode(self):
    msg = "APP IS RUNNING IN DEV-MODE!"
    self.ids['lbl_warning'].text = msg
    self.ids['user_notify_expt'].text = msg


# enable [1] / disable [0] button
def change_enable_status(instance, enable):
    # try:
    #     if enable is True and instance.disabled is False:
    #         msg = "Button: {0} forced to be enabled although already enabled.".format(instance.text)
    #         warnings.warn(msg)
    #     elif enable is False and instance.disabled is True:
    #             msg = "Button: {0} forced to be disabled although already disabled.".format(instance.text)
    #             warnings.warn(msg)
    # except Exception as e:
    #     pass

    if enable is True:
        instance.disabled = False
    else:
        instance.disabled = True


def change_enable_status_chain(self, activate, change_elements):  # *args
    # for myC in range(len(args)):
    for fluidElement in change_elements:
        change_enable_status(self.ids[fluidElement], activate)


##########################
#                        #
# == BUTTON FUNCTIONS == #
#                        #
##########################
def end_fluidiscope(app):
    # save data to config
    # gather_last_state(app)
    fluidiscopeIO.write_config()
    try:
        if not fg.my_dev_flag:
            fg.ledarr.send("CLEAR")
            fg.camera.close()
    finally:
        print("Closed camera")

    app.get_running_app().stop()


def select_method(self, instance, aimed_component_group):
    if aimed_component_group == "light_buttons":
        method_dictionary = {'FULL': 0, 'PRE': 1, 'CUS': 2, 'FLUO': 3} #instance.text: 0,
        switch_entries = ["btn_light_full", "btn_light_preset_pattern", "btn_light_custom_pattern", "btn_light_fluo"]
        [active_method, inactive_methods] = select_method_switches(instance, method_dictionary, switch_entries)
        if instance.uid == self.ids['btn_light_preset_pattern'].uid:
            counter_active_methods = ['btn_light_set_2_clear','btn_light_set_2_fill','slider_light_set_2_NA','btn_light_set_2_pattern_run','btn_light_set_2_pattern_1','btn_light_set_2_pattern_2','btn_light_set_2_pattern_3','btn_light_set_2_pattern_4']
            for idx in range(1, 5):
                if fg.config['light_patterns']['active_p'+str(idx)] == 1:
                    active_pattern = str(idx)
                    break
            print("Select_method: active_pattern={0}".format(active_pattern))
            active_method = [active_method, 'btn_light_set_2_pattern_' + active_pattern]
        elif instance.uid == self.ids['btn_light_custom_pattern'].uid:
            counter_active_methods = ['btn_light_set_2_clear', 'btn_light_set_2_fill','slider_light_set_2_NA']
            inactive_methods.append('btn_light_set_2_pattern_off')
            inactive_methods.append('btn_light_set_2_pattern_run')
            inactive_methods.append('btn_light_set_2_pattern_1')
            inactive_methods.append('btn_light_set_2_pattern_2')
            inactive_methods.append('btn_light_set_2_pattern_3')
            inactive_methods.append('btn_light_set_2_pattern_4')
        else:
            counter_active_methods = []
    elif aimed_component_group == "light_patterns":
        method_dictionary = {'P1': 0, 'P2': 1, 'P3': 2, 'P4': 3, 'RUN': 4} #instance.text: 0,
        switch_entries = ["btn_light_set_2_pattern_1","btn_light_set_2_pattern_2", "btn_light_set_2_pattern_3", "btn_light_set_2_pattern_4",'btn_light_set_2_pattern_run']
        [active_method, inactive_methods] = select_method_switches(instance, method_dictionary, switch_entries)
        counter_active_methods = []
    elif aimed_component_group == "motor_buttons":
        method_dictionary = {"x": 0, "y": 1, "z": 2}
        fg.config["motor"]["active_motor"] = method_dictionary[instance.text]
        switch_entries = ["btn_motor_dir_x", "btn_motor_dir_y", "btn_motor_dir_z"]
        [active_method, inactive_methods] = select_method_switches(instance, method_dictionary, switch_entries)
        counter_active_methods = ["btn_motor_up", "btn_motor_down", "btn_motor_stepsize_plus", "lbl_motor_stepsize",
                                  "btn_motor_stepsize_minus"]
    elif aimed_component_group == "motor_mov_buttons":
        method_dictionary = {"<<": 0, ">>": 1}
        switch_entries = ["btn_motor_down", "btn_motor_up"]
        [active_method, inactive_methods] = select_method_switches(instance, method_dictionary, switch_entries)
        counter_active_methods = []
    elif aimed_component_group == "motor_calibration_buttons":
        method_dictionary = {"Cal.": 0}
        switch_entries = ["scr_motor_set_cal_min", "scr_motor_set_cal_zero","scr_motor_set_cal_max"]
        [active_method, inactive_methods] = select_method_switches(instance, method_dictionary, switch_entries)
        counter_active_methods = ["scr_motor_set_cal_min", "scr_motor_set_cal_zero","scr_motor_set_cal_max"]
    elif aimed_component_group == "imaging_method":
        method_dictionary = {"Bright": 0, "qDPC": 1, "Custom": 2, "Fluor": 3}
        #hswitch_entries = ["btn_imaging_technique_1", "btn_imaging_technique_2", "btn_imaging_technique_3", "btn_imaging_technique_fluor"]
        switch_entries = ["btn_imaging_technique_1", "btn_imaging_technique_2", "btn_imaging_technique_3", "btn_imaging_technique_fluor"]
        [active_method, inactive_methods] = select_method_switches(instance, method_dictionary, switch_entries)
        inactive_methods = [] # implemented to allow for multiple selection
        if len(fg.config['experiment']['active_methods']) == 0:            
            inactive_methods.extend(["btn_imaging_measiter", "btn_imaging_totaldurat","btn_imaging_dplus", "btn_imaging_dminus","btn_imaging_hplus", "btn_imaging_hminus",
                                    "btn_imaging_mplus", "btn_imaging_mminus","btn_imaging_splus", "btn_imaging_sminus",])
            counter_active_methods = ["btn_take_image", "btn_snap", "btn_take_foreground", "btn_take_background"]
        elif len(fg.config['experiment']['active_methods']) == 1 and check_active(instance):
            inactive_methods.extend(["btn_imaging_measiter", "btn_imaging_totaldurat","btn_imaging_dplus", "btn_imaging_dminus","btn_imaging_hplus", "btn_imaging_hminus",
                                    "btn_imaging_mplus", "btn_imaging_mminus","btn_imaging_splus", "btn_imaging_sminus",])
            counter_active_methods = ["btn_take_image", "btn_snap", "btn_take_foreground", "btn_take_background"]
        imaging_methods_change(self, instance)
    #elif aimed_component_group == "imaging_method_fluo":
    #    active_method = "btn_imaging_technique_fluo"
    #    switch_entries = ["btn_imaging_technique_1", "btn_imaging_technique_2", "btn_imaging_technique_3"]
    #    if not any([self.ids[x].fl_active for x in switch_entries]):
    #        inactive_methods =["btn_imaging_measiter", "btn_imaging_totaldurat","btn_imaging_dplus", "btn_imaging_dminus","btn_imaging_hplus", "btn_imaging_hminus",
    #                                "btn_imaging_mplus", "btn_imaging_mminus","btn_imaging_splus", "btn_imaging_sminus",]
    #        counter_active_methods = ["btn_take_image", "btn_snap", "btn_take_foreground", "btn_take_background"]
    #    else:
    #        inactive_methods = None
    #        counter_active_methods = None
    elif aimed_component_group == "select_imaging_time_entry":
        method_dictionary = {"MEAS\nITER": 0, "TOTAL\nDURAT": 1}
        switch_entries = ["btn_imaging_measiter", "btn_imaging_totaldurat"]
        [active_method, inactive_methods] = select_method_switches(instance, method_dictionary, switch_entries)
        counter_active_methods = ["btn_imaging_dplus", "btn_imaging_dminus","btn_imaging_hplus", "btn_imaging_hminus",
                                  "btn_imaging_mplus", "btn_imaging_mminus","btn_imaging_splus", "btn_imaging_sminus",]
    elif aimed_component_group == "take_image":
        if fg.config['experiment']['active']:
            method_dictionary = {"SNAP": 0, "Stop Measurement": 1, "BG": 2, "FG": 3}
        else:
            method_dictionary = {"SNAP": 0, "Start Measurement": 1, "BG": 2, "FG": 3}
        switch_entries = ["btn_snap", "btn_take_image", "btn_take_foreground", "btn_take_background", "btn_copy"]
        [active_method, inactive_methods] = select_method_switches(instance, method_dictionary, switch_entries)
        counter_active_methods = []
    else:
        pass
    # if list inactive_methods is not empty
    try:
        if inactive_methods:
            change_enable_status_chain(self, check_active(instance), inactive_methods[:])
    # if list counter_active_methods is not empty
        if counter_active_methods:
            change_enable_status_chain(self, not check_active(instance), counter_active_methods[:])
    except Exception as exc:
        print("Had exception: __{}__, but continued".format(exc))
    # change activation status of clicked instance (button)
    change_activation_status(instance)
    clear_notification_labels(self)
    if isinstance(active_method, list):
        if active_method[1] == 'btn_light_set_2_pattern_1':
            light_set_patterns(self,self.ids[active_method[1]])

    if fg.my_dev_flag:
        warn_dev_mode(self)
    print('Selected methods: {}.'.format(fg.config['experiment']['active_methods']))
    print('this time selected method: {}.'.format(active_method))
    return active_method

def imaging_methods_change(self, instance):
    if instance.text in fg.config['experiment']['active_methods']:
        fg.config['experiment']['active_methods'].remove(instance.text)
    else:
        fg.config['experiment']['active_methods'].append(instance.text)

def show_notification_labels(self, instance):
    is_snapshot = instance.text in ['SNAP', 'BG', 'FG']

    if is_snapshot:
        if instance.text == "BG":
            msg = "Background image taken ({0})".format(fg.config['experiment']['imaging_method'])
        elif instance.text == "FG":
            msg = "Foreground image taken ({0})".format(fg.config['experiment']['imaging_method'])
        else:
            msg = "Snapshot image taken ({0})".format(fg.config['experiment']['imaging_method'])
    else:
        if fg.config['experiment']['success']:
            print("Notification: " + str(fg.expt_num))
            switch_notify_color(self, button_color_active)
            msg = "Experiment #{0} completed successfully.".format(fg.expt_num)
        else:
            switch_notify_color(self, button_color_caution)
            msg = "Experiment #{0} aborted by user.".format(fg.expt_num)

    self.ids['user_notify_expt'].text = msg


def clear_notification_labels(self):
    switch_notify_color(self, button_fontcolor_inactive)
    self.ids['user_notify_expt'].text = ""
    self.ids['status_images_left'].text = ""
    self.ids['status_time_left'].text = ""
    self.ids['status_images_taken'].text = ""
    self.ids['status_time_passed'].text = ""
    self.ids['lbl_warning'].text = ""


def select_method_switches(instance, method_dictionary, switch_entries):
    popped_entry = switch_entries.pop(method_dictionary[instance.text])
    return [popped_entry, switch_entries]


def get_imaging_method(self):
    if check_active(self.ids['btn_imaging_technique_1']):
        imaging_technique = self.ids['btn_imaging_technique_1'].text
    elif check_active(self.ids['btn_imaging_technique_2']):
        imaging_technique = self.ids['btn_imaging_technique_2'].text
    elif check_active(self.ids['btn_imaging_technique_3']):
        imaging_technique = self.ids['btn_imaging_technique_3'].text
    elif check_active(self.ids['btn_imaging_technique_fluor']):
        imaging_technique = self.ids['btn_imaging_technique_fluor'].text
    elif check_active(self.ids['btn_take_background']):
        imaging_technique = self.ids['btn_take_background'].text
    elif check_active(self.ids['btn_take_foreground']):
        imaging_technique = self.ids['btn_imaging_technique_3'].text
    else:
        imaging_technique = None
    return imaging_technique


def experiment_duration_format(value,direction):
    # format time values -> biggest: d
    if direction == 'forward':
        result = [0,0,0,0]
        result[0] = int(value/86400)
        producth = result[0]*86400
        result[1] = int((value-producth)/3600)
        producth += result[1]*3600
        result[2] = int((value-producth)/60)
        producth += result[2] * 60
        result[3] = value - producth
    else:
        result = sum(a*b for a,b in zip(value, [86400,3600,60,1]))
    return result


def imaging_set_time(self,instance,value):
    if check_active(self.ids['btn_imaging_measiter']):
        p_lbl = self.ids['lbl_imaging_measiter']
        p_supp = imaging_set_time_chkbound_and_update(fg.config['experiment']['interval'], value)
        if (p_supp <= fg.config['experiment']['duration'] ):
            fg.config['experiment']['interval'] = p_supp
        else:
            fg.config['experiment']['interval'] = fg.config['experiment']['duration']
        p_op = fg.config['experiment']['interval']
    else:
        p_lbl = self.ids['lbl_imaging_totaldurat']
        fg.config['experiment']['duration'] = imaging_set_time_chkbound_and_update(fg.config['experiment']['duration'], value)
        p_op = fg.config['experiment']['duration']
        if (fg.config['experiment']['duration'] < fg.config['experiment']['interval'] ):
            fg.config['experiment']['interval'] = fg.config['experiment']['duration']
            self.ids['lbl_imaging_measiter'].text = imaging_set_time_write(p_op)

    p_lbl.text = imaging_set_time_write(p_op)


def imaging_set_time_chkbound_and_update(p_op,value):
    if value[1] > 0 or (p_op + value[1] * [86400, 3600, 60, 1][value[0]] >= 0):
        p_op += value[1]*[86400,3600,60,1][value[0]]

    return p_op


def imaging_set_time_write(p_op):
    val = experiment_duration_format(p_op,'forward')
    return str(val[0]) + "d " + str(val[1]) + "h " + str(val[2]) + "m " + str(val[3]) + "s"


def imaging_set_time_init(self):
    self.ids['lbl_imaging_measiter'].text = imaging_set_time_write(fg.config['experiment']['interval'])
    self.ids['lbl_imaging_totaldurat'].text = imaging_set_time_write(fg.config['experiment']['duration'])
    self.ids['lbl_imaging_totaldurat'].canvas.ask_update()
    self.ids['lbl_imaging_measiter'].canvas.ask_update()


def slider_change(self,instance):
    print('%s value has changed to %s' % (instance.name, str(instance.value)))
    #fg.ledarr.send("RECT+0+0+8+8+1", int(instance.value), int(instance.value), int(instance.value))
    if check_active(self.ids['btn_light_fluo']):
        fg.fluo.send("FLUO", int(instance.value))
        print('Fluo active, sent FLUO+{}.'.format(int(instance.value)))
    fg.config['light']['intensity'] = int(instance.value)

def buttons_light(self,instance):
    if fg.my_dev_flag:
        print 'I am delivering data to the arduino by pidgeon. Takes a while...'
    light_change_status(self, instance)
    select_method(self, instance, "light_buttons")
   

#############################
#                           #
# ==   Imaging Methods   == #
#                           #
#############################


def chk_experiment_created(self,instance,name):
    if instance.text == name:
        if fg.started_first_exp:
            self.ids["sm"].current = 'scr_imaging'
            self.ids["btn_scr_name"].text = 'IMA\nGING'
        else:
            self.ids["sm"].current = 'scr_start'
            self.ids["btn_scr_name"].text = 'STA\nRT'

def run_measurement(self, instance):
    # prepare folder
    fluidiscopeIO.prepareFolder()

    # put data into config-dictionary
    set_measurement_parameter(self)

    # clear arduino and set to flyby (= do not save patterns)
    if not fg.my_dev_flag:
        fg.ledarr.send("CLEAR")
        time.sleep(0.04)
        fg.ledarr.send("FLYBY", 1)
    # set status of autofocus to False
    #fg.config['experiment']['is_autofocus_request'] = False
    #fg.config['experiment']['is_autofocus_busy'] = False
    if instance.uid == self.ids['btn_snap'].uid:
        select_method(self, instance, "take_image")
        activate(instance)
        take_image(self)
        abort_measurement(self, instance)
    else: 
        # rewrite button-text if necessary
        if instance.text == "Start Measurement":
            instance.text = "Stop Measurement"

        # put values into display:
        update_measurement_status_display(self)

        # activate and deactivate according buttons
        select_method(self, instance, "take_image")
        activate(instance)

        # let the device settle for a bit
        time.sleep(0.2)
        # schedule callback-function

        #if imaging_callback(self, instance):
        if 'meas' in fg.EVENT:
            pass
            event_delete(fg.EVENT['meas'])
            event_delete(fg.EVENT['meas_disp'])
        else:
            # fg.EVENT = Clock.schedule_interval(partial(autofocus_callback, self, instance), fg.config['experiment']['interval_autofocus'])
            update_interval = 1 # for timer display refresh
            fg.EVENT['meas'] = Clock.schedule_interval(partial(imaging_callback, self, instance),fg.config['experiment']['interval'])# in seconds
            fg.EVENT['meas_disp'] = Clock.schedule_interval(partial(update_measurement_status_display_timer, self, update_interval),update_interval) # in seconds
            #if 'autofocus' in fg.EVENT:
            #    print("autofocus_measure angelegt mit time {}".format(fg.config['autofocus']['time_interval_min']*60))
            #    fg.EVENT['autofocus_measure'] = Clock.schedule_interval(partial(run_autofocus,instance),fg.config['autofocus']['time_interval_min']*60) # in seconds
            #if 'autofocus' in fg.EVENT:
            #   fg.EVENT['autofocus_measure'].cancel()
            #    Clock.unschedule(fg.EVENT['autofocus_measure'])
            #print("not implemented yet")

def set_measurement_parameter(self):
    fg.config['light']['intensity_expt'] = fg.config['light']['intensity']
    if fg.config['experiment']['imaging_cause'] == 'SNAP':
        fg.config['experiment']['snap_num'] += 1
    else:
        fg.config['experiment']['imaging_method'] = get_imaging_method(self)
        fg.config['experiment']['imaging_num'] = 0
        fg.config['experiment']['time_left'] = fg.config['experiment']['duration']
        fg.config['experiment']['time_passed'] = 0
        fg.config['experiment']['images_total'] = int(
            fg.config['experiment']['duration'] / fg.config['experiment']['interval'] + 1)  # 1 image directly taken on start
        fg.config['experiment']['images_left'] = fg.config['experiment']['images_total']
        fg.config['experiment']['images_taken'] = 0
        fg.config['experiment']['success'] = False

def update_measurement_parameters(self):
    fg.config['experiment']['images_left'] -= 1
    #if (fg.config['experiment']['images_taken'] > 0):
    #    fg.config['experiment']['time_left'] -= fg.config['experiment']['interval']
    #    fg.config['experiment']['time_passed'] += fg.config['experiment']['interval']
    fg.config['experiment']['images_taken'] += 1

    if fg.config['experiment']['images_left'] == 0:
        fg.config['experiment']['time_left'] = 0
        fg.config['experiment']['time_passed'] = fg.config['experiment']['duration']


def update_measurement_status_display(self):
    self.ids['status_images_left'].text = str(fg.config['experiment']['images_left'])
    self.ids['status_time_left'].text = imaging_set_time_write(
        fg.config['experiment']['time_left'])  # str(int(fg.config['experiment']['time_left'] / 60)) + 'm'
    self.ids['status_images_taken'].text = str(fg.config['experiment']['images_taken'])
    self.ids['status_time_passed'].text = imaging_set_time_write(
        fg.config['experiment']['time_passed'])  # str(int(fg.config['experiment']['time_passed'] / 60)) + 'm'
    #if 'meas' in fg.EVENT:
    #   print(fg.EVENT['meas'])

def update_measurement_status_display_timer(self, interval, *rargs):
    if not fg.config['experiment']['is_autofocus_busy']:
        fg.config['experiment']['time_left'] -= interval
        fg.config['experiment']['time_passed'] += interval
    update_measurement_status_display(self)


def abort_measurement(self, instance):
    deactivate(instance)
    imaging_method_dic = {"Bright": 'btn_imaging_technique_1', "qDPC": "btn_imaging_technique_2",
                          "Custom": "btn_imaging_technique_3", "Fluor": "btn_imaging_technique_fluor"}
    change_enable_status(instance, False)
    while not fg.config['experiment']['active_methods'] == []:
        key = fg.config['experiment']['active_methods'].pop(0)
        deactivate(self.ids[imaging_method_dic[key]])
    for key in imaging_method_dic:
        change_enable_status(self.ids[imaging_method_dic[key]], True)

    activate_methods = ["btn_imaging_measiter", "btn_imaging_totaldurat","btn_imaging_dplus", "btn_imaging_dminus","btn_imaging_hplus", "btn_imaging_hminus",
                                "btn_imaging_mplus", "btn_imaging_mminus","btn_imaging_splus", "btn_imaging_sminus",]
    change_enable_status_chain(self, True, activate_methods)
    if not instance.uid == self.ids['btn_snap'].uid:
        event_delete('meas')
        event_delete('meas_disp')

        fg.config['experiment']['last_expt_num'] = fg.expt_num
        show_notification_labels(self, instance)


def event_delete(event_name):
    fg.EVENT[event_name].cancel()
    Clock.unschedule(fg.EVENT[event_name])
    fg.EVENT.pop(event_name,None)
    print("Event: ~{0}~ was canceled and safely deleted.".format(event_name))

# not used anymore?? ---------------------------------------
#def take_snapshot(self, instance):
#    take_image(self, instance.text)
#
#    if instance.text in ["SNAP", "BG", "FG"]:  # switch color
#        imaging_method_dic = {"Bright": 'btn_imaging_technique_1', "qDPC": "btn_imaging_technique_2",
#                              "Custom": "btn_imaging_technique_3"}
#        select_method(self, instance, "take_image")
#        change_enable_status(self.ids[imaging_method_dic[fg.config['experiment']['imaging_method']]], True)
#
#    fg.ledarr.send("CLEAR")
# ----------------------------------------------------------

def filename_take_image_now_refine(filename='',imaging_cause='MEAS', file_format='.jpg'):
    if imaging_cause == 'MEAS':
        filename += '-' + str(fg.config['experiment']['imaging_num'])
    elif imaging_cause == 'SNAP':
        filename += '-' + str(fg.config['experiment']['snap_num'])
    else: 
        filename += '-' + str(fg.config['experiment']['autofocus_num'])
    return filename + file_format
    
#really just takes an image
def take_image_now(self,imaging_cause='MEAS', filename='', method='CUS'):
    # get correct filename
    filename = filename_take_image_now_refine(filename=filename,imaging_cause=imaging_cause, file_format='.jpg')
    # start 
    print("This is _take_image_now_-Func saving to: {}".format(filename))
    if fg.my_dev_flag:
        print("Image taken -- DEV-MODE --.")
    else: 
        # prepare camera
        camera_set_parameter(method=method)
        # select for imaging cause -> 
        if imaging_cause == 'AF':
            fg.camera.capture(rawCapture,'rgb')
            image=rawCapture.array[:,:,fg.config['autofocus']['use_channel']]
            return image
        else:
            fg.camera.capture(filename)
            return True

def take_image(self, *args): 
    '''
    Method that switches through different imaging modalities. Does hold the respective algorithms.
    '''
    set_active_again = False
    active_modes = [] 
    if fg.config['experiment']['imaging_cause'] == 'AF': # case of autofocus
        image_name = set_image_name(im_cause='AF',method='CUS')
        file_name_write = uni.Path(fg.expt_path, image_name) 
        time.sleep(0.1)
        fluidiscopeIO.update_matrix(self, ignore_NA=True, sync_only=False)
        time.sleep(fg.config['imaging']['speed'])
        tin_returnval = take_image_now(self, 'AF', file_name_write)
        fg.ledarr.send("CLEAR")
    else: 
        for myl in range(0,len(fg.config['experiment']['active_methods'])):
            active_method = fg.config['experiment']['active_methods'][myl] # active method
            print("Using method {} of {}: {}.".format(myl,len(fg.config['experiment']['active_methods'])-1,active_method))
            image_name = set_image_name(im_cause=fg.config['experiment']['imaging_cause'],method=active_method)
            file_name_write = uni.Path(fg.expt_path, image_name) 
            #print("file_name_write = " + file_name_write)
            # make sure preview is off
            set_active_again = False
            if check_active(self.ids['btn_preview']):
                camera_preview(False)
                set_active_again = True
            for x in ['btn_light_full','btn_light_preset_pattern','btn_light_custom_pattern','btn_light_fluo']:
                if check_active(self.ids[x]):
                    buttons_light(self, self.ids[x])
                    active_modes.append(x)
            try:
                if active_method == 'Fluor':
                    # swith to customized LED field
                    fg.fluo.send("FLUO",fg.config['light']['intensity_expt'])
                    file_name_write_fluo = file_name_write + '-INT_' + str(fg.config['light']['intensity_expt'])
                    time.sleep(fg.config['experiment']['i2c_send_delay'])
                    #time.sleep(fg.config['imaging']['speed'])
                    tin_returnval = take_image_now(self,fg.config['experiment']['imaging_cause'], file_name_write_fluo)
                    fg.fluo.send("FLUO",0)
                    time.sleep(fg.config['experiment']['i2c_send_delay'])
                else:
                    fg.ledarr.send("CLEAR")
                    # 2) Decide what images to take
                    col = int(fg.config['light']['intensity_expt'])
                    #print("Color: " + str(col))
                    if active_method in ["BG", "FG"]:
                        # imaging
                        if active_method == "BG":
                            tin_returnval = take_image_now(self,fg.config['experiment']['imaging_cause'], file_name_write)
                        else:
                            fg.ledarr.send("NA+2")
                            fg.ledarr.send("RECT+0+0+8+8+1", col, col, col)
                            time.sleep(fg.config['imaging']['speed'])
                            tin_returnval = take_image_now(self,fg.config['experiment']['imaging_cause'], file_name_write)
                    else:
                        if active_method == 'Bright':
                            fg.ledarr.send("NA+3")
                            fg.ledarr.send("RECT+0+0+8+8+1", col, col, col)
                            time.sleep(fg.config['imaging']['speed'])
                            tin_returnval = take_image_now(self,fg.config['experiment']['imaging_cause'], file_name_write)
                        elif active_method == "qDPC":
                            pattern_list = prepare_illu_pattern_list()
                            #Clock.schedule_once(partial(
                            tin_returnval = pattern_disp_func(self,pattern_list,True,file_name_write,fg.config['imaging']['speed'])
                        elif active_method== "Custom":
                            # swith to customized LED field
                            time.sleep(0.1)
                            fluidiscopeIO.update_matrix(self, ignore_NA=True, sync_only=False)
                            time.sleep(fg.config['imaging']['speed'])
                            tin_returnval = take_image_now(self,fg.config['experiment']['imaging_cause'], file_name_write)
                            fg.ledarr.send("CLEAR")
                        else:
                            # set now with small NA image
                            file_name_write = uni.Path(fg.expt_path, image_name)
                            # fluidiscopeIO.update_matrix(self, instance, ignoreNA=True, sync_only=False)
                            # time.sleep(0.5)
                            fg.ledarr.send("RECT+3+3+2+2+1", col, col, col)
                            time.sleep(fg.config['imaging']['speed'])
                            tin_returnval = take_image_now(self,fg.config['experiment']['imaging_cause'], file_name_write)
                            fg.ledarr.send("RECT+3+3+2+2+1+0+0+0")
            finally:
                pass
        if active_method in ['Bright','qDPC','Custom','Fluor']:
            fg.config['experiment']['imaging_num'] += 1
        fg.config['experiment']['expt_last_image'] = file_name_write + fg.config['imaging']['extension']
        fg.ledarr.send("CLEAR")
    if set_active_again:
        camera_preview(True)
        for x in active_modes:
            buttons_light(self, self.ids[x])
        
    # True -> normal images taken;
    # image -> case of autofocus
    return tin_returnval

    #print("fg.config['experiment']['expt_last_image']" + fg.config['experiment']['expt_last_image'])


def set_image_name(im_cause=None,method=None,mytime=None): 
    '''
    Creating the image_name for the used method. 
    :param:
    -------
    :im_cause: <STRING> defines the reason for the image
    -> AF, SNAP, MEAS, BG
    :method: <STRING> that sets the input method
    -> FULL, PRE, CUS, FLUO
    :mytime: <STRING> that gives the time of start of the experiment
    -> hhmmss
    '''
    now = str(datetime.now().strftime("%H%M%S"))
    image_name = "{}-".format(fg.today)
    if not im_cause == None:
        image_name += "{}-".format(im_cause)
    if not method == None: 
        image_name += "{}-".format(method)
    if not mytime == None: 
        image_name += "{}-".format(now)
    return image_name


def resizeImage(infile, resize_factor=5): # used to show image in preview
    if not fg.my_dev_flag:
        #path = uni.Path(infile).parent()
        im = cv.LoadImage(infile)
        thumbnail = cv.CreateMat(im.rows / resize_factor, im.cols / resize_factor, cv.CV_8UC3) #inherently rounds
        cv.Resize(im, thumbnail)
        fname = infile + "_thumbnail.jpg" #path
        cv.imwrite(fname, thumbnail)
        # fg.config['experiment']['expt_last_image'] = fname
        return fname


def camera_set_parameter(method='CUS'):
    if not fg.my_dev_flag:
        print("Autofocus is set to False!")

        if method in ['CUS','qDPC','Bright','BG','FG']:
            method_key = 'cam'
            fg.camera.resolution = tuple(fg.config[method_key]['resolution'])
            fg.camera.contrast = fg.config[method_key]['contrast']
            fg.camera.sharpness = fg.config[method_key]['sharpness']
            fg.camera.brightness = fg.config[method_key]['brightness']
            fg.camera.saturation = fg.config[method_key]['saturation']
            fg.camera.ISO = fg.config[method_key]['iso']
            fg.camera.video_stabilization = fg.config[method_key]['videoStabilization']
            fg.camera.exposure_compensation = fg.config[method_key]['exposureCompensation']
            fg.camera.exposure_mode = fg.config[method_key]['exposureMode']
            fg.camera.meter_mode = fg.config[method_key]['meterMode']
            fg.camera.awb_mode = fg.config[method_key]['awbMode']
            if fg.config[method_key]['awbMode'] == 'off':
                fg.camera.awb_gains = (Fraction(200, 128), Fraction(200, 128)) # (red, blue)  [0..8] TODO: Get values from YAML, Only some randomly chosen values!  fg.config[method_key]['awbGain']
            fg.camera.image_effect = fg.config[method_key]['imageEffects']
            fg.camera.color_effects = fg.config[method_key]['colorEffects']
            fg.camera.rotation = fg.config[method_key]['rotation']
            fg.camera.hflip = fg.config[method_key]['hflip']
            fg.camera.vflip = fg.config[method_key]['vflip']
            fg.camera.crop = tuple(fg.config[method_key]['crop'])
            fg.camera.shutter_speed = fg.config[method_key]['shutterSpeed']
        elif method == 'Fluor':
            method_key = 'cam_fluo'
            fg.camera.resolution = tuple(fg.config[method_key]['resolution'])
            fg.camera.contrast = fg.config[method_key]['contrast']
            fg.camera.sharpness = fg.config[method_key]['sharpness']
            fg.camera.brightness = fg.config[method_key]['brightness']
            fg.camera.saturation = fg.config[method_key]['saturation']
            fg.camera.ISO = fg.config[method_key]['iso']
            fg.camera.video_stabilization = fg.config[method_key]['videoStabilization']
            fg.camera.exposure_compensation = fg.config[method_key]['exposureCompensation']
            fg.camera.exposure_mode = fg.config[method_key]['exposureMode']
            fg.camera.meter_mode = fg.config[method_key]['meterMode']
            fg.camera.awb_mode = fg.config[method_key]['awbMode']
            if fg.config[method_key]['awbMode'] == 'off':
                fg.camera.awb_gains = (Fraction(200, 128), Fraction(200, 128)) # (red, blue)  [0..8] TODO: Get values from YAML, Only some randomly chosen values!  fg.config[method_key]['awbGain']
            fg.camera.image_effect = fg.config[method_key]['imageEffects']
            fg.camera.color_effects = fg.config[method_key]['colorEffects']
            fg.camera.rotation = fg.config[method_key]['rotation']
            fg.camera.hflip = fg.config[method_key]['hflip']
            fg.camera.vflip = fg.config[method_key]['vflip']
            fg.camera.crop = tuple(fg.config[method_key]['crop'])
            fg.camera.shutter_speed = fg.config[method_key]['shutterSpeed']
        print("Camera shutter_speed={}, exposure_speed={} at ISO=.".format(fg.camera.shutter_speed, fg.camera.exposure_speed, fg.camera.iso))
        print("Camera preparation done for method=".format(method))
    return True

def crop_image():
    pass


def camera_capture(filename,*rargs):
    if not fg.my_dev_flag:
        print("Camera capture: " + filename)
        filename = filename + fg.config['imaging']['extension']
        if len(rargs) > 0:
            if rargs[0] == 'autofocus':
                rawCapture = PiRGBArray(fg.camera)
                fg.camera.capture(rawCapture,'rgb')
                return rawCapture
        else:
            fg.camera.capture(filename)
            return True
        # fg.ledarr.send("CLEAR")


def imaging_callback(self, *largs):
    print '\nThis is the imaging callback speaking !\n<> Images are now taken!'

    # skip imaging step during autofocus
    if not fg.config['experiment']['is_autofocus_busy']:
        # take image
        fg.config['experiment']['imaging_method']='MEAS'
        take_image(self)
        deact_me = False
        if (fg.config['experiment']['time_left']-fg.config['experiment']['interval']) >= 0:
            # update config entries
            update_measurement_parameters(self)

            # update display entries
            update_measurement_status_display(self)
            return True
        elif any([fg.config['experiment']['time_left'] == 0,fg.config['experiment']['time_left']-fg.config['experiment']['interval'] < 0]):
            update_measurement_parameters(self)
            update_measurement_status_display(self)
            deact_me = True
        else:
            deact_me = True

        if deact_me:
            fg.config['experiment']['success'] = True
            imaging_method_dic = {"Bright": 'btn_imaging_technique_1', "qDPC": "btn_imaging_technique_2",
                                  "Custom": "btn_imaging_technique_3","Fluor":"btn_imaging_technique_fluor"}
            switch_start_condition(self, instance)
            deactivate(self.ids[imaging_method_dic[fg.config['experiment']['imaging_method']]])
            keys=['meas_disp','autofocus_measure']
            if keys[0] in fg.EVENT:
                event_delete(keys[0])
            if keys[1] in fg.EVENT:
                event_delete(keys[1])
            return False


def autofocus(self, instance):
    '''
    Autofocus to be called from main-routine on button click.
    :param self:
    :param instance:
    :return:
    '''
    set_autofocus(self,instance)
    change_activation_status(instance)
    key = 'autofocus_now' if (instance.uid == self.ids['btn_autofocus_now'].uid) else 'autofocus'
    if not key in fg.EVENT:
        run_autofocus(self,instance,key)
    else:
        event_delete(key)


def set_autofocus(self, instance):
    '''
    Button logic for autofocus.
    :param self:
    :param instance:
    :return:
    '''
    print("Autofocus-00a2- DevFlag={}".format(fg.my_dev_flag))
    #if not (fg.my_dev_flag):
    if check_active(instance):
        print("Autofocus-00a2- now deactivating autofocus")
        fg.config['experiment']['is_autofocus'] = False
        if instance.uid==self.ids['btn_autofocus'].uid:
            refresh_text_entry(instance, "Autofocus disabled!")
        print("Autofocus-00a4- Autofocus disabled")
    else:
        print("Autofocus-00a2- now setting autofocus")
        fg.config['experiment']['is_autofocus'] = True
        if instance.uid==self.ids['btn_autofocus'].uid:
            refresh_text_entry(instance, "Autofocus enabled!")
        print("Autofocus-00a4- Autofocus enabled")


def run_autofocus(self,instance,key):
    '''
    Always runs autofocus only once!
    '''
    if key == 'autofocus_now':
        if not fg.config['experiment']['is_autofocus_busy']:
            fg.EVENT['autofocus_now'] = Clock.schedule_once(partial(af.autofocus_callback, self,instance),1)#start direct after 1 sec
        else:#auto-deactivate autofocus
            set_autofocus(self, instance)
            change_activation_status(instance)
    else:
        fg.EVENT['autofocus_measure'] = Clock.schedule_interval(partial(run_autofocus, instance),fg.config['autofocus']['time_interval_min']*60)
    print('Autofocus-01-Started autofocus routine.')

def autofocus_callback(self, instance, *rargs):
    # start autofocus if necessary and only if it is not already in progress
    print("Autofocus-02-callback started.")
    if fg.config['experiment']['is_autofocus_request'] == True:
        if fg.config['experiment']['is_autofocus_busy'] == False:
            # only perform autofocus if it is not already doing so!
            now = time.time()
            af.autofocus_callback(self, instance)  # this runs through the algorithm in the autofocus toolbox
            time_taken = time.time() - now
            # adjust timing
            fg.config['experiment']['time_left'] += int(round(time_taken))
            fg.config['experiment']['time_passed'] += fg.config['experiment']['interval']

            # update display entries
            update_measurement_status_display(self)
        return True


def switch_start_condition(self, instance):
    dic = {"Bright": 'btn_imaging_technique_1', "qDPC": "btn_imaging_technique_2", "Custom": "btn_imaging_technique_3", "FLUO":"btn_imaging_technique_fluor"}
    deactivate(instance)

    if "Measurement" in instance.text:
        instance.text = "Start Measurement"
    instance.disabled = True

    for key in dic:
        deactivate(self.ids[dic[key]])
        change_enable_status(self.ids[dic[key]], True)

    #change_enable_status(self.ids['slider_interval'], True)
    #change_enable_status(self.ids['slider_duration'], True)
    change_enable_status(self.ids['btn_copy'], True)
    change_enable_status(self.ids['btn_snap'], False)
    change_enable_status(self.ids['btn_take_background'], False)
    change_enable_status(self.ids['btn_take_foreground'], False)
    change_enable_status(self.ids['btn_take_image'], False)

    fg.config['experiment']['time_left'] = fg.config['experiment']['duration']
    fg.config['experiment']['time_passed'] = 0
    fg.config['experiment']['images_total'] = floor(fg.config['experiment']['duration'] / fg.config['experiment'][
        'interval'])  # both values are in secs (e.g. 4500*60/1*60)

    fg.config['experiment']['images_left'] = fg.config['experiment']['images_total']
    fg.config['experiment']['images_taken'] = 0

    show_notification_labels(self, instance)

    fg.config['experiment']['active'] = 0


def switch_notify_color(self, color):
    self.ids['status_images_left'].color = color
    self.ids['status_time_left'].color = color
    self.ids['status_images_taken'].color = color
    self.ids['status_time_passed'].color = color
    self.ids['user_notify_expt'].color = color

    '''
    fg.callback_counter -= 1
    if fg.callback_counter == 5:
        print 'Last call of my callback, bye bye !'

        return False
    print 'My callback is called'
    '''


#############################
#                           #
# ==    Light Methods    == #
#                           #
#############################
def light_change_status(self, instance):
    if instance.text=='FLUO':
        if check_active(instance):
            chk_experiment_created(self,instance,instance.text)
            fg.fluo.send("FLUO",0)
        else: 
            fg.config['light']['intensity']=int(self.ids['slider_light_intensity'].value)            
            fg.fluo.send("FLUO", fg.config['light']['intensity']) #memes ON-setting
    else: 
        col = int(fg.config['light']['intensity_expt'])
        pattern='CUS'
        if check_active(instance):
            chk_experiment_created(self,instance,instance.text)
            fg.ledarr.send("CLEAR")
        else:
            if instance.text == 'FULL':
                fg.ledarr.send("RECT+0+0+8+8+1", col, col, col)
            elif instance.uid == self.ids['btn_light_preset_pattern'].uid or instance.uid == self.ids['btn_light_custom_pattern'].uid:
                if instance.uid == self.ids['btn_light_preset_pattern'].uid:
                    for idx in range(1, 5):
                        if fg.config['light_patterns']['active_p' + str(idx)] == 1:
                            pattern = 'p' + str(idx)
                            break
                fluidiscopeIO.update_matrix(self, ignore_NA=True, sync_only=False, pattern=pattern)
                self.ids["sm"].current = 'scr_light_set_2'
                self.ids["btn_scr_name"].text = 'LI\nGHT\nOPT\n2'
                #if instance.uid == self.ids['btn_light_preset_pattern'].uid:
                    #select_method(self,instance)
                fluidiscopeIO.settings_save_restore(self, instance, True)
            else:
                pass

def setNA(userNA):
    if 1 <= userNA <= 4:
        fg.config['light']['NA'] = int(userNA)
        fg.ledarr.send("NA", fg.config['light']['NA'])


# saves colorPicker-Value in File
def selected_color(self, instance):
    my_test_RGBA = []
    if fg.config['light']['color_picker_counter'] == 0:
        fg.config['light']['picked'] = [int(x * 255) for x in instance.color[0:3]]
        fg.config['light']['color_picked'] = [int(x * 255) for x in instance.color[0:3]]
        # print "RGBA = ", str(fg.config_active['light_properties']['picked'])
        fg.config['light']['color_picker_counter'] += 1
    elif fg.config['light']['color_picker_counter'] < 4:
        fg.config['light']['color_picker_counter'] += 1
    else:
        fg.config['light']['color_picker_counter'] = 0
    # print "color_picker_counter = %s" % str(fg.config_active['light_properties']['light_general_color_picker_counter'])


def light_settings_activate(self, instance):
    change_activation_status(instance)
    pos_nbr = int(str(instance.name)[len('scr_light_set_2_grid_'):])
    send_allowed = True
    print "pos-nbr: %s" % str(pos_nbr)
    if check_active(self.ids['btn_light_preset_pattern']):
        pattern_list = [self.ids['btn_light_set_2_pattern_1'], self.ids['btn_light_set_2_pattern_2'],
                        self.ids['btn_light_set_2_pattern_3'], self.ids['btn_light_set_2_pattern_4']]
        idx = sum(map(lambda x, y: int(x) * y, [check_active(x) for x in pattern_list], [1, 2, 3, 4]))
        key_name = ['light_patterns','p'+str(idx)]
        pattern = key_name[1]
        if idx == 0:
           send_allowed = False
    else:
        key_name = ['light','user']
        pattern = 'CUS'
    # case e.g. if no Pattern is selected
    if send_allowed:
        if check_active(instance):
            instance.fl_value = fg.config['light']['picked']
            instance.value = 1
            #fluidiscopeIO.update_matrix(self, instance, ignore_NA=False, sync_only=True, pattern=pattern)
            fg.ledarr.send("PXL", pos_nbr, list(fg.config['light']['picked']))
            instance.background_color = convert_color(fg.config['light']['picked'],1.0)
        else:
            instance.fl_value = [0,0,0]
            instance.value = 0
            if not fg.my_dev_flag:
                fg.ledarr.send("PXL", pos_nbr, list(instance.fl_value))
            #fluidiscopeIO.update_matrix(self, instance, ignore_NA=False, sync_only=True, pattern=pattern)
        fg.config[key_name[0]][key_name[1]][pos_nbr / 8][pos_nbr % 8] = [instance.fl_value[0],instance.fl_value[1],instance.fl_value[2]] # if not, then handling kivy.properties.ObservableList to list
        print(fg.config[key_name[0]][key_name[1]][pos_nbr / 8][pos_nbr % 8][:])

def convert_color(in_color,in_opacity):
    return [in_color[0]/255.0,in_color[0]/255.0,in_color[0]/255.0,in_opacity]

def matrix_switch(self, instance):
    fg.ledarr.send("CLEAR")
    if instance.text == "FILL": # not relevant anymore ->  or instance.text == "ON":
        fill_matrix(self, instance)
    elif instance.text == "CLEAR": # not relevant anymore -> or instance.text == "OFF":
        fg.config['light']['user'] = [[[0,0,0],] * 8 for i in range(8)]
        fluidiscopeIO.update_matrix(self, ignore_NA=True)


def fill_matrix(self, instance, ignore_NA=False):
    fg.ledarr.send("CLEAR")
    fg.config['light']['user'] = [[0] * 8 for i in range(8)]
    options = [[3, 3, 2, 2], [2, 2, 4, 4], [1, 1, 6, 6], [0, 0, 8, 8]]
    coords = options[3]

    if not ignore_NA:
        coords = options[fg.config['light']['NA'] - 1]

    color = [fg.config['light']['intensity']] * 3
    time.sleep(0.02)
    if not fg.my_dev_flag: 
        fg.ledarr.send("RECT", coords, 1, color)
    for row in range(coords[2]):
        for col in range(coords[3]):
            fg.config['light']['user'][row + coords[0]][col + coords[1]] = 1

    fluidiscopeIO.update_matrix(self, ignore_NA=True)


def light_set_patterns(self,instance):
    pattern_list = [self.ids['btn_light_set_2_pattern_1'],self.ids['btn_light_set_2_pattern_2'],self.ids['btn_light_set_2_pattern_3'],self.ids['btn_light_set_2_pattern_4']]
    pattern_list_uid = [pattern_list[0].uid, pattern_list[1].uid,pattern_list[2].uid, pattern_list[3].uid]
    if instance.uid in pattern_list_uid:
        if check_active(instance):
            if check_active(self.ids['btn_light_set_2_pattern_off']):
                change_activation_status(self.ids['btn_light_set_2_pattern_off'])
                self.ids['btn_light_set_2_pattern_off'].text = 'OFF'
            select_method(self, instance, "light_patterns")
            if not fg.my_dev_flag:
                fg.ledarr.send("CLEAR")
        else:
            select_method(self, instance, "light_patterns")
            if instance.value == 1 and not check_active(self.ids['btn_light_set_2_pattern_off']):
                change_activation_status(self.ids['btn_light_set_2_pattern_off'])
                self.ids['btn_light_set_2_pattern_off'].text = 'ON'
            if instance.value == 0 and check_active(self.ids['btn_light_set_2_pattern_off']):
                change_activation_status(self.ids['btn_light_set_2_pattern_off'])
                self.ids['btn_light_set_2_pattern_off'].text = 'ON'
            fluidiscopeIO.update_matrix(self, ignore_NA=True, sync_only=False, pattern=instance.text.lower())
    elif instance.uid == self.ids['btn_light_set_2_pattern_off'].uid:
        sum_active_patterns=0
        for myc in range(1,5):
            sum_active_patterns+=fg.config['light_patterns']['active_p'+str(myc)]
        idx = sum(map(lambda x,y:x*y,[check_active(x) for x in pattern_list],[1,2,3,4]))
        active_el = 'active_p'+str(idx)
        if fg.config['light_patterns'][active_el] == 1 and sum_active_patterns > 1:
            fg.config['light_patterns'][active_el] = 0
            self.ids['btn_light_set_2_pattern_off'].text = 'OFF'
        else:
            fg.config['light_patterns'][active_el] = 1
            self.ids['btn_light_set_2_pattern_off'].text = 'ON'
        change_activation_status(self.ids['btn_light_set_2_pattern_off'])
    elif instance.uid == self.ids['btn_light_set_2_pattern_run'].uid:
        if not check_active(instance) and 'pattern_disp_callback' not in fg.EVENT:
            select_method(self, instance, "light_patterns")
            pattern_list = prepare_illu_pattern_list()
            fg.EVENT['pattern_disp_callback'] = Clock.schedule_interval(partial(pattern_disp_callback,self,instance,pattern_list,False,'',fg.config['imaging']['speed']),3)
            pattern_disp_callback(self,instance, pattern_list, imaging=False, time_sleep=fg.config['imaging']['speed'])
        else:
            event_delete('pattern_disp_callback')
            select_method(self, instance, "light_patterns")
    else:
        pass
    #select_method()
    #btn_light_set_2_pattern_1

def prepare_illu_pattern_list():
    pattern_list = []
    for myc in range(1, 5):
        mycs = str(myc)
        if fg.config['light_patterns']['active_p' + mycs] == 1:
            pattern_list.append(mycs)
    print(pattern_list)
    return pattern_list

def pattern_disp_func(self,pattern_list,imaging=False,file_name_write='',time_sleep=0.1,*rargs):
    for mypat in pattern_list:
        time.sleep(0.04) # giving the arduino time to clear buffer
        file_name_write_dpc = file_name_write + '_MYPAT_P' + mypat
        #if not fg.my_dev_flag:
        fluidiscopeIO.update_matrix(self, ignore_NA=True, sync_only=False, pattern='p'+mypat)
        time.sleep(time_sleep) # waiting for the light to be active
        take_image_now(file_name_write_dpc,imaging_cause=fg.config['experiment']['imaging_cause'],filename=file_name_write_dpc)
        fg.ledarr.send("CLEAR")
        #else:
        #    print("Pattern_disp! I would have shown: " + mypat)
    return True

#############################
#                           #
# ==    Motor Methods    == #
#                           #
#############################

def motor_steps_settings(self, instance):
    # function is callable afer one of the motor-directions is chosen
    if check_active(self.ids['btn_motor_dir_x']):
        key_stepsize = "stepsize_xy"
    elif check_active(self.ids['btn_motor_dir_y']):
        key_stepsize = "stepsize_xy"
    elif check_active(self.ids['btn_motor_dir_z']):
        key_stepsize = "stepsize_z"
    if instance.uid == self.ids['btn_motor_stepsize_minus'].uid and (fg.config["motor"][key_stepsize] - fg.config["motor"]["change_amount"] >=0):
        fg.config["motor"][key_stepsize] -= fg.config["motor"]["change_amount"]
    elif instance.text == '+':
        fg.config["motor"][key_stepsize] += fg.config["motor"]["change_amount"]
    else :
        fg.config["motor"][key_stepsize] = 0
    self.ids["lbl_motor_stepsize"].text = str(fg.config["motor"][key_stepsize])


def move_motor(self, instance):
    testdict = {0: "DRVX", 1: "DRVY", 2: "DRVZ"}
    cmd = testdict[fg.config['motor']['active_motor']]
    limit_reached = False
    if fg.config['motor']['active_motor'] in [0,1]:
        stepsize_app = '_xy'
    else:
        stepsize_app = '_z'

    stepsize = floor(fg.config['motor']['stepsize'+stepsize_app] /
                     fg.config['motor']['conversion_factor'+stepsize_app])
    if instance.text == '<<':
        stepsize *= -1
    # move motor
    if fg.config['motor']['active_motor'] == 2:
        if stepsize < 0:
            limit_key = 'calibration_z_min'
        else:
            limit_key = 'calibration_z_max'
        if not check_active(self.ids['scr_motor_set_cal']):
            if abs(fg.config['motor']['calibration_z_pos'] + stepsize) > abs(fg.config['motor'][limit_key]):
                limit_reached == True
                self.ids['lbl_warning'].text = 'Z-limit reached at position:'+ str(fg.config['motor']['calibration_z_pos']) + 'from max=' + str(fg.config['motor']['calibration_z_max'])
    # manage progress-bar
    if not limit_reached:
        if not fg.my_dev_flag:
            fg.motors.send(cmd, stepsize)
        refresh_progress_bar = 0.2
        fg.config['motor']['calibration_z_pos'] += stepsize
        if instance.text == '<<':
            stepsize *= -1
        move_motor_display(self, instance, fg.config['motor']['active_motor'], stepsize, refresh_progress_bar)


def move_motor_display(self,instance, active_motor,stepsize,refresh_progress_bar,*rargs):
    if active_motor in [0,1]:
        max_time = fg.config['motor']['standard_move_time_xy'] * stepsize / fg.config['motor']['standard_move_dist_xy']
    else: # z-drive
        max_time = fg.config['motor']['standard_move_time_z'] * stepsize / fg.config['motor']['standard_move_dist_z']
    upd_val = 100 * refresh_progress_bar / max_time
    print(str(upd_val))
    fg.EVENT['pb_motor'] = Clock.schedule_interval(partial(move_motor_display_update, self, instance, upd_val),refresh_progress_bar)


def move_motor_display_update(self,instance,upd_val,event_obj,*rargs):
    if (self.ids['pb_motor_step'].value < 100):
        self.ids['pb_motor_step'].value += upd_val
        print(self.ids['pb_motor_step'].value)
    else:
        self.ids['pb_motor_step'].value = 0
        event_delete('pb_motor')
        select_method(self, instance, "motor_mov_buttons")


def btn_motor_refresh_text(self, instance):
    if instance.text in ['x','y']:
        refresh_entry = 'stepsize_xy'
    else:
        refresh_entry = 'stepsize_z'
    refresh_text_entry(self.ids["lbl_motor_stepsize"],str(fg.config["motor"][refresh_entry]))

# for now only implemented for z motor
def motor_calibrate(self, instance):
    if check_active(self.ids['btn_motor_dir_x']) or check_active(self.ids['btn_motor_dir_y']) or check_active(self.ids['btn_motor_dir_z']):
        if check_active(self.ids['btn_motor_dir_z']):
            if instance.uid == self.ids['scr_motor_set_cal_min'].uid:
                fg.config['motor']['calibration_z_min'] = fg.config['motor']['calibration_z_pos']
                self.ids['scr_motor_set_grid_lbl_value_calibration_z_min'].text = str(fg.config['motor']['calibration_z_min'])
            elif instance.uid == self.ids['scr_motor_set_cal_zero'].uid:
                fg.config['motor']['calibration_z_pos'] = 0
                self.ids['scr_motor_set_grid_lbl_value_calibration_z_pos'].text = str(fg.config['motor']['calibration_z_pos'])
            elif instance.uid == self.ids['scr_motor_set_cal_max'].uid:
                fg.config['motor']['calibration_z_max'] = fg.config['motor']['calibration_z_pos']
                self.ids['scr_motor_set_grid_lbl_value_calibration_z_max'].text = str(fg.config['motor']['calibration_z_max'])
            else:
                key_change = 'calibration_z_pos'

def motor_calibrate_activate(self, instance):
    select_method(self,instance,"motor_calibration_buttons")


##########################
#                        #
# == LABEL FUNCTIONS == #
#                        #
##########################
def refresh_text_entry(instance, new_text):
    instance.text = new_text

##########################
#                        #
# == Information refresh == #
#                        #
##########################
#def gather_last_state(app):
    # function intended to gather last state for specific objects
    # pass

# relay functions for dev-mode
def devmode_switch(func):
    if fg.my_dev_flag:
        print("%%DEVMODE---Function: {0} not evaluated---%%".format(func))
    else:
        return func

##########################
#                        #
# ==   DATA TOOLBOX   == #
#                        #
##########################

def show_last_im(self, instance):
    # (1) Create Layout
    # Layout of Popup
    box = BoxLayout(orientation='vertical')
    # insert Image
    subbox_1 = BoxLayout(size_hint_y=0.9)
    usr_src = str(fg.config['experiment']['expt_last_image'])
    # usr_src = '20180613_203118_Bright.jpg'
    print("show last img src: " + usr_src)
    print("Is File: " + str(os.path.isfile(usr_src)))
    # resize image and show smaller one -> try different factors
    usr_src = resizeImage(usr_src, resize_factor=5)
    widget_image = Image(source=usr_src)
    subbox_1.add_widget(widget_image)
    # add Button area
    subbox_2 = BoxLayout(size_hint_y=0.1, padding=(10, 5, 10, 5))
    popup_button = Button(text='Close')
    subbox_2.add_widget(popup_button)
    # Add to Layout of Popup
    box.add_widget(subbox_1)
    box.add_widget(subbox_2)

    # (2) create Popup
    popup_title = "Last Image: " + fg.config['experiment']['expt_last_image']
    popup = Popup(title=popup_title, content=box, size_hint=(0.8, 0.8), auto_dismiss=False)

    # (3) bind functions
    popup_button.bind(on_press=popup.dismiss)

    # (4) Open Popup
    popup.open()
    # fg.popup_last_im = True

    # fg.config_active['experiment_properties']['directory_copy'] = selection


'''Copy with progress bar?
import sys
class ProgressBar(object):
    def __init__(self, message, width=20, progressSymbol='c', emptySymbol='-'):
        self.width = width

        if self.width < 0:
            self.width = 0

        self.message = message
        self.progressSymbol = progressSymbol
        self.emptySymbol = emptySymbol

    def update(self, progress):
        totalBlocks = self.width
        filledBlocks = int(round(progress / (100 / float(totalBlocks))))
        emptyBlocks = totalBlocks - filledBlocks

        progressBar = self.progressSymbol * filledBlocks + \
                      self.emptySymbol * emptyBlocks

        if not self.message:
            self.message = u''

        progressMessage = u'\r{0} {1}  {2}%'.format(self.message,
                                                    progressBar,
                                                    progress)

        sys.stdout.write(progressMessage)
        sys.stdout.flush()

    def calculateAndUpdate(self, done, total):
        progress = int(round((done / float(total)) * 100))
        self.update(progress)
# from: https://www.pythoncentral.io/how-to-movecopy-a-file-or-directory-folder-with-a-progress-bar-in-python/
import os
import shutil
def countFiles(directory):
    files = []

    if os.path.isdir(directory):
        for path, dirs, filenames in os.walk(directory):
            files.extend(filenames)

    return len(files)
p = ProgressBar('Copying files...')
def makedirs(dest):
    if not os.path.exists(dest):
        os.makedirs(dest)

def copyFilesWithProgress(src, dest):
    numFiles = countFiles(src)

    if numFiles > 0:
        makedirs(dest)

        numCopied = 0

        for path, dirs, filenames in os.walk(src):
            for directory in dirs:
                destDir = path.replace(src, dest)
                makedirs(os.path.join(destDir, directory))

            for sfile in filenames:
                srcFile = os.path.join(path, sfile)

                destFile = os.path.join(path.replace(src, dest), sfile)

                shutil.copy(srcFile, destFile)

                numCopied += 1

                p.calculateAndUpdate(numCopied, numFiles)
        print
'''


def copytree(src, dst, overwrite_checked, symlinks=False, ignore=None):
    # function froM: https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth#12514470

    # print(dst)
    # st = os.stat(dst)
    # uid = st.st_uid
    # print(uid)
    # # output: 0
    # userinfo = pwd.getpwuid(st.st_uid)
    # print(userinfo)
    # # output: pwd.struct_passwd(pw_name='root', pw_passwd='x', pw_uid=0,
    # #          pw_gid=0, pw_gecos='root', pw_dir='/root', pw_shell='/bin/bash')
    # ownername = pwd.getpwuid(st.st_uid).pw_name
    # print(ownername)

    if not os.path.isdir(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, overwrite_checked, symlinks, ignore)
        else:
            if overwrite_checked:
                shutil.copyfile(s, d)
                # OSError: [Errno 1] Operation not permitted with shutil.copy2
                # os.chmod is failing -> shutil.copy is specified to copy permission bits
                # FAT32 does not know permissions
                # https://stackoverflow.com/questions/11835833/why-would-shutil-copy-raise-a-permission-exception-when-cp-doesnt
            else:
                if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                    shutil.copyfile(s, d)


def move_data(self, instance):
    if instance.text == "!Copy Data!":
        if fg.copy_path:
            try:
                copytree(str(fg.data_path), str(fg.copy_path), self.ids['scr_copy_2_check'].active)
                self.ids['scr_copy_2_progressbar'].value = 1000
                self.ids['scr_copy_2_status_lbl'].text = 'DONE COPYING!'
                fg.copy_path = ""
            except OSError as e:
                msg = "Unknown error occured. For USB devices please make sure \n"
                msg += "USB device is connected at specified copy path.\n"
                msg += "Current copy path is:\n" + str(fg.copy_path)
                self.ids['scr_copy_2_status_lbl'].text = msg
        else:
            msg = "Please select suitable destination folder."
            msg += "\nCurrent copy path is:\n" + str(fg.copy_path)
            self.ids['scr_copy_2_status_lbl'].text = msg
    elif instance.text == "DELETE":
        delete_data(self)


def delete_data(self):
    if self.ids['scr_copy_2_delete_check'].active:
        shutil.rmtree(fg.data_path, ignore_errors=True)
        subfolder = fg.today
        restore = uni.Path(fg.data_path, subfolder)
        subfolder = "expt_" + fluidiscopeInit.format_num(fg.expt_num)
        restore = uni.Path(restore, subfolder)
        os.makedirs(restore)
        self.ids['scr_copy_2_delete_check'].active = False
        self.ids['scr_copy_2_status_lbl'].text = "DONE DELETING."
    else:
        msg = "Please check 'sure'-checkbox first in order to\n"
        msg += "delete ALL experiment data\non RaspberryPi!"
        self.ids['scr_copy_2_status_lbl'].text = msg


def query_path_info(path):
    dir_count = 0
    file_count = 0
    for _, dirs, files in os.walk(path):
        dir_count += len(dirs)
        file_count += len(files)
    return (dir_count, file_count)

    # List of Files (LoF)
    # lof_source = glob.glob('')
    # lof_destination = glob.glob(fg.config_active['experiment_properties']['directory_copy'])


##########################
#                        #
# == GENERAL TOOLBOX == #
#                        #
##########################

# analyse object
def analyze_object(instance):
    for attr in dir(instance):
        print("obj.%s = %s" % (attr, getattr(instance, attr)))


def textinput_convert(text_input):
    value_converted = []
    check_var = 0
    # int ?
    try:
        value_converted = int(text_input)
    except ValueError:
        check_var = 1
    # float?
    if check_var == 1:
        try:
            value_converted = float(text_input)
        except ValueError:
            check_var = 2
    # array?
    if check_var == 2:
        try:
            if text_input[0] == '[' and text_input[1] != '[':
                text_input = text_input.replace("[", "")
                text_input = text_input.replace("]", "")
                text_input = text_input.replace(",", " ")
                try:
                    value_converted = map(int, text_input.split())
                except ValueError:
                    value_converted = map(float, text_input.split())
            elif text_input[0] == '(' and text_input[1] != '(':
                text_input = text_input.replace("(", "")
                text_input = text_input.replace(")", "")
                text_input = text_input.replace(",", " ")
                try:
                    value_converted = map(int, text_input.split())
                except ValueError:
                    value_converted = map(float, text_input.split())
            else:
                check_var = 3
        except:
            pass
    # boolean-case
    if check_var == 3:
        if re.sub('[fF][aA][lL][sS][eE]', '', text_input) == '':
            value_converted = False
        elif re.sub('[tT][rR][uU][eE]', '', text_input) == '':
            value_converted = True
        else:
            check_var = 4
    # string case
    if check_var == 4:
        value_converted = text_input
    # return
    return value_converted


######################
#                    #
# === CAMERA TOOLS ===#
#                    #
######################

# do Preview
def camera_preview(start):
    if (start is True):  # and (fg.popup_last_im is False):
        try:
            fg.camera.start_preview()
            fg.camera.preview.fullscreen = fg.config['imaging']['fullscreen']
            fg.camera.preview.alpha = fg.config['imaging']['alpha']
            fg.camera.preview.window = fg.config['imaging']['window']
        finally:
            print("Preview started")
    else:
        try:
            fg.camera.stop_preview()
        finally:
            print("Preview stopped!")


def camera_preview_change_status(self, instance):
    if not (fg.my_dev_flag):
        if check_active(instance):
            camera_preview(False)
            refresh_text_entry(instance, "Start preview")
            #self.ids["btn_autofocus"].disabled = True
        else:
            camera_preview(True)
            refresh_text_entry(instance, "Stop preview")
            #self.ids["btn_autofocus"].disabled = False
    else:
        warn_dev_mode(self)
		

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


#def measure_contrast(image):
    # process the image and get the edges
    #ksiz = 5  # gaussian blur diameter
    #my_blur = cv2.blur(image, (ksiz, ksiz))
    #my_edges = cv2.Canny(my_blur, 50, 150)
    #my_focus_val = cv2.mean(my_edges)[0]

    #return my_focus_val, my_blur, my_edges

######################
#                    #
# === INIT TOOLS ===#
#                    #
######################