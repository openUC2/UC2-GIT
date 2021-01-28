# %%  Imports

#Fluidi imports
import fluidiscopeToolbox as toolbox
import fluidiscopeGlobVar as fg
from fluidException import fluidException
from fluidiscopeLogging import logger_createChild

# general imports
from copy import deepcopy
import datetime
import io
import logging
import numpy as np
import os
import re
from shutil import copyfile
from safe_cast import safe_str
import time
import unipath as uni

# conditioned imports
if os.name == 'nt':
    import yaml
else:
    from ruamel import yaml

if not fg.my_dev_flag and fg.i2c:
    from I2CDevice import I2CDevice

# %%  Code
# activate logging
logger = logger_createChild('io','UC2')


def load_config(config_file):
    try:
        if not os.path.isfile(config_file):
            raise fluidException('File "{0}" not found.'.format(config_file))

        tmp_dict = {}
        config_load = fluid_load(config_file)

        for sub in config_load:
            sub_file = uni.Path(config_file.parent, config_load[sub])
            if not os.path.isfile(sub_file):
                raise fluidException('File "{0}" not found.'.format(sub_file))
            tmp_dict[sub] = {}
            subconfig_load = fluid_load(sub_file)
            for x in subconfig_load:
                tmp_dict[sub][x] = subconfig_load[x]

    except Exception as exc:
        logger.error(exc)
        logger.error("Unable to load config file.")
        tmp_dict = {}

    return tmp_dict


def restore_config():
    logger.debug("Trying to restore config file from backup.")
    try:
        backup_path = uni.Path(fg.config_path, "backup")
        backup_file = uni.Path(backup_path, "main_config.bak")
        backup_config = load_config(backup_file)
    except Exception as exc:
        logger.error("Error: " + str(exc))
        logger.error("Restore failed.")
        exit()

    bak_files = [f for f in os.listdir(backup_path) if f.endswith(".bak")]
    for f in bak_files:
        src = str(uni.Path(backup_path, f))
        dst = str(uni.Path(fg.config_path, f))
        copyfile(src, dst)
        dstn = dst.replace('.bak', '.yaml')
        if os.path.exists(dstn):
            os.remove(dstn)
        os.rename(dst, dstn)

    try:
        restored_main_load = fluid_load(fg.config_file)
        for key in restored_main_load:
            update = restored_main_load[key].replace(".bak", ".yaml")
            restored_main_load[key] = update
        fluid_dump(fg.config_file, restored_main_load)

    except Exception as exc:
        logger.error("Error: " + str(exc))
        logger.error("Restore failed.")
        exit()

    logger.debug("Backup successfully restored.")


def load_user_config(userconfig):
    default_dict = load_config(fg.config_file)
    user_load = fluid_load(userconfig)
    try:
        completed_load = verify_user_config(user_load, default_dict)
        return completed_load
    except fluidException as e:
        logger.error(
            'Invalid key "{0}" found. Loading default.'.format(e.args[0]))
        return default_dict
    except Exception as e:
        logger.error(e)
        return default_dict


def verify_user_config(userload, defaultdict):
    for key in userload:
        if key in defaultdict:
            for subkey in userload[key]:
                if subkey in defaultdict[key]:
                    pass
                else:
                    raise fluidException(subkey)
        else:
            raise fluidException(key)

    for key in userload:
        for subkey in userload[key]:
            defaultdict[key][subkey] = userload[key][subkey]
    return defaultdict

# write config-file


def write_config():
    main_load = fluid_load(fg.config_file)
    trackme = []
    try:
        for sub in main_load:
            trackme = sub
            sub_file = uni.Path(fg.config_path, main_load[sub])
            fluid_dump(sub_file, fg.config[sub])
    except Exception as exc:
        logger.error(exc)
        logger.warning('Please consider Leaving the Application. Error happened when writing into: {}. Content was:'.format(trackme))
        logger.warning(fg.config[trackme])
        # exit()
    logger.debug("Config written.")


def write_user_config(userconfig, *args):
    if(safe_str(args[0], default=False)):
        write_path = uni.Path(fg.config_path, args[0])
    else:
        write_path = uni.Path(fg.config_path, fg.today)

    fluid_dump(write_path, userconfig)
    logger.debug("User-config written.")


def fluid_load(read_file):
    try:
        with io.open(read_file) as stream:
            data = yaml.safe_load(stream)
        return data
    except Exception as exc:
        logger.error(read_file)
        logger.error(exc)
        exit()


def fluid_dump(write_file, data):
    # try:
    with io.open(write_file, 'w', encoding='utf8') as stream:
        yaml.safe_dump(data, stream, default_flow_style=False)
    # except Exception as exc:
    #    print(exc)
    #    print("Using yaml.dump for file {}".format(write_file))
    #    with io.open(write_file, 'w', encoding='utf8') as stream:
    #        yaml.dump(data, stream, default_flow_style=False)
        # exit()
def io_createCHK(self):
    '''
    Returns array with btns to check for activity.
    '''
    # prepare empty array
    chk = [False] * 20

    # Camera-Options 1
    chk[0] = self.ids['scr_cam_set_1_btn_save'].uid
    chk[1] = self.ids['scr_cam_set_1_btn_restore'].uid
    chk[2] = self.ids['btn_cam_set_1'].uid

    # Camera-Options 2
    chk[3] = self.ids['scr_cam_set_2_btn_save'].uid
    chk[4] = self.ids['scr_cam_set_2_btn_restore'].uid
    chk[5] = self.ids['btn_cam_set_2'].uid

    # Light-Options 2
    chk[6] = self.ids['scr_light_set_2_btn_save'].uid
    chk[7] = self.ids['scr_light_set_2_btn_restore'].uid
    chk[8] = self.ids['btn_light_set_2'].uid

    # Experiment Settings
    chk[9] = self.ids['scr_imaging_set_btn_save'].uid
    chk[10] = self.ids['scr_imaging_set_btn_restore'].uid
    chk[11] = self.ids['btn_imaging_set'].uid

    # Motor Settings
    chk[12] = self.ids['scr_motor_set_btn_save'].uid
    chk[13] = self.ids['scr_motor_set_btn_restore'].uid
    chk[14] = self.ids['btn_motor_set'].uid

    # Autofocus Settings
    chk[15] = self.ids['scr_autofocus_set_btn_save'].uid
    chk[16] = self.ids['scr_autofocus_set_btn_restore'].uid
    chk[17] = self.ids['btn_autofocus_set'].uid
    chk[18] = self.ids['btn_autofocus_opt'].uid

    # Tomography Options
    chk[19] = self.ids['btn_tomography_settings'].uid

    # done?
    return chk

def settings_save_restore_switcher(self, restore, config_name,layout_prename):
    '''
    switches between readout and -in with exception handling.
    '''
    for key in fg.config[config_name]:
        prop_help = layout_prename + key
        try:
            if restore:
                self.ids[prop_help].text = str(fg.config[config_name][key])
            else:
                fg.config[config_name][key] = toolbox.textinput_convert(self.ids[prop_help].text)
        except:
            logger.warning("ID: {} not found. SKIPPED!".format(prop_help))

def settings_save_restore(self, instance, restore):
    '''
    Switches save and Restore commands for different menues.
    '''
    # get check
    chk = io_createCHK(self)
    
    # select interface/switching-group for active instance
    chk = [x == instance.uid for x in chk]

    # prepare namings / assign tasks
    if any(chk[:3]):
        config_name = 'cam'
        layout_prename = 'scr_cam_set_1_grid_lbl_value_'
    elif any(chk[3:6]):
        config_name = 'cam'
        layout_prename = 'scr_cam_set_2_grid_lbl_value_'
    elif chk[6]:
        fg.config['light']['default'] = deepcopy(fg.config['light']['user'])
    elif any(chk[7:9]):
        if restore:
            fg.config['light']['user'] = deepcopy(
                fg.config['light']['default'])
            self.ids['slider_light_set_2_NA'].value = fg.config['light']['NA']
        update_matrix(self, ignore_NA=True, sync_only=False)
    elif any(chk[9:12]):
        config_name = 'imaging'
        layout_prename = 'scr_imaging_set_grid_lbl_value_'
    elif any(chk[12:15]):
        config_name = 'motor'
        layout_prename = 'scr_motor_set_grid_lbl_value_'
    elif any(chk[15:19]):
        config_name = 'autofocus'
        layout_prename = 'scr_autofocus_set_lbl_value_'
    elif chk[19]:
        config_name = 'tomo'
        layout_prename = 'tm_'
        #key_prefix = 'tomography_lbl_'
        #key_dict = ['tm_backlash', 'tm_motor', 'tm_takeimage', 'tm_startPOS', 'tm_endPOS', 'tm_steps', 'tm_stepsize', 'tm_steptime', 'tm_totalTime']

    # update values
    if any(chk[:6]+chk[9:]):
        settings_save_restore_switcher(self,restore,config_name,layout_prename)

    # store if necessary
    if not restore:
        logger.debug("Writing Settings into file for {}".format(repr(instance.text)))
        write_config()


def slider_setNA(self, instance):
    self.ids['slider_light_set_2_NA'].text = 'NA = ' + str(instance.value)
    logger.debug("Instance.Value: " + str(instance.value))
    toolbox.setNA(int(instance.value))
    toolbox.fill_matrix(self, instance)
    logger.debug("NA set by slider: {}".format(fg.config['light']['NA']))


def update_matrix(self, ignore_NA=False, sync_only=True, pattern='CUS'):
    fg.config['light']['update_matrix_active'] = True
    prop_help = 'scr_light_set_2_grid_'
    if pattern == 'CUS':
        pattern_key = ['light', 'user']
    else:
        pattern_key = ['light_patterns', pattern]
    n = fg.config['light']['matrixdim'][0]
    m = fg.config['light']['matrixdim'][1]
    offset_x = 0
    offset_y = 0

    if not ignore_NA:
        offset_x = int((m - fg.config['light']['NA'] * 2) * 0.5)
        offset_y = int((n - fg.config['light']['NA'] * 2) * 0.5)

    for row in range(n):
        if offset_y <= row < n - offset_y:
            for col in range(m):
                if offset_x <= col < m - offset_x:
                    pos = row * n + col
                    prop_help = 'scr_light_set_2_grid_' + str(pos)
                    if np.sum(fg.config[pattern_key[0]][pattern_key[1]][row][col]) > 0:
                        self.ids[prop_help].value = 1
                        self.ids[prop_help].fl_value = fg.config[pattern_key[0]
                                                                 ][pattern_key[1]][row][col]
                        toolbox.activate(self.ids[prop_help])
                        #logger.debug("Turn-on light of {} at Pos {} with val {}."format(,[row,col],self.ids[prop_help].fl_value))
                    else:
                        self.ids[prop_help].value = 0
                        self.ids[prop_help].fl_value = [0, 0, 0]
                        toolbox.deactivate(self.ids[prop_help])

                    if not sync_only and np.sum(self.ids[prop_help].fl_value) > 0:
                        fg.ledarr.send("PXL", pos, list(
                            self.ids[prop_help].fl_value),logging=1)
                        time.sleep(fg.config['experiment']['i2c_send_delay'])
                        #logger.debug("sent:{0} of {1}".format(support_str,type(list(support_str))))
    fg.config['light']['update_matrix_active'] = False


def prepareFolder():
    # increase the number of current experiment by 1
    fg.started_first_exp = True

    # check if the correct date is chosen - if not create a new folder
    if fg.config['experiment']['last_expt_date'] != fg.today:
        fg.expt_num = 1
    else:
        fg.config['experiment']['last_expt_num'] += 1
        fg.expt_num = fg.config['experiment']['last_expt_num']

    expt_folder = "expt_" + format_num(fg.expt_num)
    fg.expt_path = str(uni.Path(fg.save_path, expt_folder))

    # assign current experiment parameters to config file
    fg.config['experiment']['last_expt_date'] = fg.today
    fg.config['experiment']['path_last_expt'] = fg.expt_path

    # create dir
    dir_test_existance(fg.expt_path)
    return fg.config


def dir_test_existance(mydir):
    try:
        if not os.path.exists(mydir):
            os.makedirs(mydir)
            logger.debug(
                'Folder: {0} created successfully'.format(mydir))
    finally:
        logger.debug('Folder check done!')


def format_num(x):
    # prepare correct file_name
    expt_num = str(x)
    ndigits = len(expt_num)
    ndigits = 3 if (ndigits < 3) else ndigits
    expt_num = expt_num.zfill(ndigits)
    return expt_num

# Solution from:
# https://stackoverflow.com/questions/15785719/how-to-print-a-dictionary-line-by-line-in-python


def dumpclean(obj):
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                logger.debug(k)
                dumpclean(v)
            else:
                logger.debug('%s : %s' % (k, v))
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                dumpclean(v)
            else:
                logger.debug(v)
    else:
        logger.debug(obj)
