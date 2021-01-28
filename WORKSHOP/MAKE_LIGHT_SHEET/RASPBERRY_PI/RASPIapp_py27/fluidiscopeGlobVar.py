# here the global variables are defined
import socket
import datetime
import unipath as uni
import os

global VERSION
global EVENT
global APP

global my_dev_flag
global started_first_exp

global config
global camera
global motors
global ledarr

global code_path
global project_path
global config_path
global data_path
global expt_path
global save_path
global copy_path
global expt_num
global today

today = datetime.datetime.now().strftime("%Y%m%d") # datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") -> important for saving the expimernts
if os.name == 'nt':
    my_dev_flag = True
else:
    my_dev_flag = False
started_first_exp = False

VERSION = '0.2b'
config = []
EVENT = {}
APP = []
motors = []
ledarr = []
