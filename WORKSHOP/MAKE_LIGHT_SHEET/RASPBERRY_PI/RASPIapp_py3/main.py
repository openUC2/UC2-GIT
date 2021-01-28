# I/O
if (1):
    import os
    # os.environ['KIVY_TEXT'] = 'egl_rpi'
    os.environ['KIVY_WINDOW'] = 'sdl2'  # 'egl_rpi'  # 'sdl2'
    # os.environ['KIVY_GL_BACKEND'] = 'gl'
    # time.sleep(1)
    pass
    # Fluidiscope

if True:
    import unipath as uni
    import socket
    import serial
    import datetime
    import time
    import logging
    import io
    import sys
    import os
    from kivy.app import App
    from kivy.lang import Builder
    from kivy.config import Config
    from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.widget import Widget
    from kivy.uix.button import Button
    from kivy.uix.label import Label
    from kivy.uix.popup import Popup
    from kivy.uix.textinput import TextInput
    from kivy.clock import Clock
    from kivy.clock import mainthread
    from functools import partial
    from kivy.utils import platform
    from kivy.core.window import Window
    from kivy.properties import NumericProperty, StringProperty, ListProperty
    import fluidiscopeGlobVar as fg
    import fluidiscopeInit
    import fluidiscopeToolbox as toolbox
    import fluidiscopeIO
    import fluidiscopeLogging as fl
if fg.i2c:
    from I2CDevice import I2CDevice

if not fg.my_dev_flag:
    import picamera

# Initialization
fl.logging_init()
fluidiscopeInit.load_config()
fluidiscopeInit.controller_init()
fluidiscopeInit.GUI_define_sizes()

# activate main-logger
logger = fl.logger_createChild('main','UC2')

# GUI classes


class Fluidiscope(BoxLayout):
    init_var = ListProperty([fg.config['light']['intensity_expt'], str(fg.config['motor']['stepsize_z']), fg.config['light_patterns']['active_p1'],
                             fg.config['light_patterns']['active_p2'], fg.config['light_patterns']['active_p3'], fg.config['light_patterns']['active_p4']])
    meas_var = ListProperty([toolbox.imaging_set_time_write(fg.config['experiment']['interval']), toolbox.imaging_set_time_write(fg.config['experiment']['duration']),
                             '', '', '', ''])
    # screen management

    def scr_switch(self, instance):
        toolbox.scr_switch(self, instance)

    def unlock_options(self, instance):
        toolbox.unlock_options(self, instance)

    # imaging functions
    def btn_function_preview(self, instance):
        return toolbox.preview_switch(self, instance)

    def experiment_duration_format(self, instance, value):
        return toolbox.experiment_duration_format(self, instance, value)

    def select_imaging_time_entry(self, instance):
        toolbox.select_method(self, instance, "select_imaging_time_entry")

    def imaging_set_time(self, instance, value):
        toolbox.imaging_set_time(self, instance, value)

    def imaging_set_time_init(self):
        toolbox.imaging_set_time_init(self)

    # change autofocus to true/false
    def btn_function_autofocus(self, instance):
        toolbox.autofocus(self, instance)

    def select_imaging_method(self, instance):
        toolbox.select_method(self, instance, "imaging_method")

    def btn_tomography_settings(self, instance):
        toolbox.tomography_settings(self, instance)

    def tomography_btn_logic(self, instance):
        toolbox.tomography_btn_logic(self, instance)

    #def tomography_startmeas(self, instance):
    #    toolbox.tomography_startmeas(self, instance)

    def btn_camera_live_settings(self, instance):
        toolbox.camera_live_settings(self, instance)

    # do a measurement (e.g. SNAP, experiment)
    def measurement_control(self, instance):
        if instance.uid == self.ids['btn_snap'].uid:
            fg.config['experiment']['imaging_cause'] = 'SNAP'
        else:
            fg.config['experiment']['imaging_cause'] = 'MEAS'
        # set active etc
        if fg.config['experiment']['active'] == 0:
            fg.config['experiment']['active'] = 1
            toolbox.run_measurement(self, instance)
            if instance.uid == self.ids['btn_snap'].uid:
                fg.config['experiment']['active'] = 0
        else:
            fg.config['experiment']['active'] = 0
            fg.config['experiment']['success'] = False
            toolbox.abort_measurement(self, instance)
            if not instance.uid == self.ids['btn_snap']:
                instance.text = "Start Measurement"

    def autofocus(self, instance):
        toolbox.change_activation_status(instance)
        toolbox.autofocus(self, instance)

    # tomography modes
    def tomography_btn_set(self, instance):
        pass

    # motor functions
    def btn_motor_movement_direction(self, instance):
        toolbox.btn_motor_refresh_text(self, instance)
        toolbox.select_method(self, instance, "motor_buttons")

    def motor_stepsize(self, instance):
        toolbox.motor_steps_settings(self, instance)

    def btn_function_move_motor(self, instance):
        if fg.my_dev_flag:
            logger.debug(
                "I am I am delivering data to the arduino by pidgeon. Takes a while...")
        if not 'pb_motor' in fg.EVENT:
            toolbox.move_motor(
                self, instance, fg.config['motor']['active_motor'])
            toolbox.select_method(self, instance, "motor_mov_buttons")

    def motor_calibrate(self, instance):
        toolbox.motor_calibrate(self, instance)

    def motor_calibrate_activate(self, instance):
        toolbox.motor_calibrate_activate(self, instance)

    # light functions

    def slider_change(self, instance):
        toolbox.slider_change(self, instance)

    def buttons_light(self, instance):
        toolbox.buttons_light(self, instance)

    # def buttons_light_fluo(self,instance):
    #    toolbox.buttons_light_fluo(self,instance)

    def colorpicker_selected_color(self, instance):
        toolbox.selected_color(self, instance)

    def light_settings_activate(self, instance):
        toolbox.light_settings_activate(self, instance)

    def slider_setNA(self, instance):
        if not fg.my_dev_flag:
            fluidiscopeIO.slider_setNA(self, instance)
        else:
            fluidiscopeIO.update_matrix(
                self, ignore_NA=True, sync_only=False)

    def matrix_switch(self, instance):
        toolbox.matrix_switch(self, instance)

    def light_set_patterns(self, instance):
        toolbox.light_set_patterns(self, instance)

    def buttons_motor(self, instance):
        if fg.my_dev_flag:
            logger.debug(
                'I am delivering data to the arduino by pidgeon. Takes a while...')
        else:
            toolbox.motor_change_status(instance)
        toolbox.select_method(self, instance, "motor_buttons")

    # menu buttons
    def start_experiment(self, instance):
        self.scr_switch(instance)
        fluidiscopeIO.prepareFolder()
        fg.config['experiment']['active'] = 0

    def options_settings_save(self, instance):
        fluidiscopeIO.settings_save_restore(self, instance, False)

    def options_settings_restore(self, instance):
        fluidiscopeIO.settings_save_restore(self, instance, True)

    def options_settings_back(self):
        toolbox.settings_back(self)

    # show data functions
    def show_last_im(self, instance):
        toolbox.show_last_im(self, instance)

    def popup_dismiss(self, instance):
        self.ids['popup_last_im'].dismiss()

    # copy functions
    def popup_choose_directory(self, instance):
        toolbox.popup_choose_copy_directory(self, instance)

    def copy_data(self, instance):
        toolbox.move_data(self, instance)

    def delete_data(self, instance):
        toolbox.move_data(self, instance)

    # general functions
    def init_properties(self):
        toolbox.init_properties(self)

    def create_clock(self, instance, touch, *args):
        if(instance.text == 'X'):
            # callback = FluidiscopeApp().get_running_app().stop()
            # Clock.schedule_once(callback, 1.5)
            # touch.ud['event'] = callback
            pass

    def delete_clock(self, instance, touch, *args):
        # Clock.unschedule(touch.ud['event'])
        pass

    def btn_end_program(self):
        toolbox.end_fluidiscope(FluidiscopeApp())

    # overwrite def-function
    def __init__(self, **kwargs):
        super(Fluidiscope, self).__init__()  # **kwargs
        # self.drives_list.adapter.bind(
        #    on_selection_change=self.drive_selection_changed)

    def get_drives(self):
        if platform == 'win':
            import win32api

            drives = win32api.GetLogicalDriveStrings()
            drives = drives.split('\000')[:-1]

            return drives
        else:
            return []

    def drive_selection_changed(self, *args):
        if len(args[0].selection) > 0:  # hasattr(args[0].selection[0],'text'):
            selected_item = args[0].selection[0].text
        else:
            selected_item = args[0].data[0]
        self.file_chooser.path = selected_item

    def drive_selection_update(self):
        #self.drives_list.adapter.data = self.get_drives()
        # if (hasattr(self.drives_list, '_reset_spopulate')):
        #    self.drives_list._reset_spopulate()
        pass

    def chkbox_delete_active(self):
        print("********* Checkbox on_active works **********")
        info = toolbox.query_path_info(fg.data_path)
        msg = "Proceeding will erase ALL EXPERIMENT DATA\n"
        msg += "on RaspberryPi! \n\n"
        msg += "{0} files in {1} directories".format(info[0], info[1])
        self.ids['scr_copy_2_status_lbl'].text = msg


# MAIN APP CLASS

class FluidiscopeApp(App):
    title = 'Fluidiscope'

    def build(self):
        '''
        Can be used to implement own pre-call conditions and set pointers. It seems, that 'fluidiscope.kv' is loaded earlier already and hence the last call is not necessary any-more.
        '''

        # self.icon = 'icon.png'
        # print("Thank you for starting Fluidiscopy v%s.\n  Copyright (C) 2017 Benedict Diederich & Rene Richter") % fg.VERSION
        # create the root widget and give it a reference of the application instance (so it can access the application settings)
        self.fluidiscope = Fluidiscope(app=self)
        self.root = self.fluidiscope
        fg.APP = self.root

        # do before creation
        # self.init_properties(self)
        
        #call not necessary???
        #return Builder.load_file(uni.Path(fg.code_path, 'fluidiscope.kv'))

    # def after_created(self):
        # self.set_init_variables
        # self.init_properties()
        #self.ids['slider_light_intensity'].value = fg.config['light']['intensity_expt']
        # self.imaging_set_time_init(self)
        # print self.ids['slider_light_intensity'].value


# ---------- START APP ----------
if __name__ == '__main__':
    FluidiscopeApp().run()
