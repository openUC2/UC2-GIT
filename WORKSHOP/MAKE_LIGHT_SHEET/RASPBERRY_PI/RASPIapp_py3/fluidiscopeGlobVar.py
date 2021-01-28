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
global fluo
global mqttclient

global code_path
global project_path
global config_path
global data_path
global expt_path
global save_path
global copy_path
global expt_num
global today
global i2c
#global setup_number

# datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") -> important for saving the expimernts
today = datetime.datetime.now().strftime("%Y%m%d")
if os.name == 'nt':
    my_dev_flag = True
else:
    my_dev_flag = False
started_first_exp = False

i2c = False
#setup_number = "004"
VERSION = '0.4'
config = []
EVENT = {}
APP = []
motors = []
ledarr = []
fluo = []
