'''
Initialization and Management of Logging Functions.
'''
# %% imports 

# fluidi
import fluidiscopeGlobVar as fg

# general 
from kivy.logger import Logger
import logging
import io
import os
from shutil import copy2
import sys
import time

# conditional imports 
if os.name == 'nt':
    import yaml
else:
    from ruamel import yaml
# %% code

def dir_test_existance(mydir):
    try:
        if not os.path.exists(mydir):
            os.makedirs(mydir)
    finally:
        pass

def logging_init():
    '''
    Isolator for basic logging-creation. 
    '''
    logging_load_config()


def open_log(logging_ini):
    try:
        with io.open(logging_ini) as stream:
            data = yaml.safe_load(stream)
        return data
    except Exception as e: 
        print('Unable to read logging-file from given PATH.')


def logger_create(logname,path_save=None,base_logger='UC2'):
    '''
    Creates a new logger-element. 
    '''
    # sanity-check
    if logname == None: 
        logname = base_logger
    if path_save == None:
        try: 
            path_save = logging.getLogger(logname).handlers[0].baseFilename
        except:
            path_save = os.path.join(os.getcwd(), 'log', "uc2-{}.log".format(time.strftime("%Y%m%d_%H%M%S", time.localtime())))

    # create empty logger
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)

    # create a logging format
    fformatter = logging.Formatter('[ %(levelname)-8s ] [ %(name)-13s ] [ %(asctime)s ] %(message)s')
    sformatter = logging.Formatter('[ %(levelname)-8s ] [ %(name)-13s ] %(message)s')

    # create a file handler
    fhandler = logging.FileHandler(path_save)
    fhandler.setLevel(logging.DEBUG)
    fhandler.setFormatter(fformatter)

    #create stream-handler
    shandler = logging.StreamHandler(sys.stdout)
    shandler.setLevel(logging.DEBUG)
    shandler.setFormatter(sformatter)
    shandler.name = logname
    shandler._name = logname

    # add the file handler to the logger
    logger.addHandler(fhandler)
    logger.addHandler(shandler)

    # parameters
    logger.propagate = False
    logger.disabled = False

    return logger

def logger_createChild(logname,base_logger_name):
    '''
    Creates a chiled logger that passes loggings through to parent, but only until there if parent has "propagate==False". 
    '''
    return logging.getLogger(base_logger_name).getChild(logname)

def logger_methodTest(logger):
    logger.info(logger_methodTest.__name__)


def logger_testlevels(logger):
    logger.debug(logger)
    logger.info(logger)
    logger.warning(logger)
    logger.error(logger)


def logging_load_config():
    '''
    Loads logger configuration, redirects kivy-logger and prepares UC2-logger.
    '''  
    # Parameters get time and date
    log_path = os.getcwd() + "/log/"
    dir_test_existance(log_path)
    logging_filename = "uc2-{}.log".format(time.strftime("%Y%m%d_%H%M%S", time.localtime()))
    log_path_full = os.path.abspath(log_path + logging_filename)
    
    # copy existing loggings to new file
    kivy_logfile = Logger.handlers[1].filename
    copy2(kivy_logfile, log_path_full)

    # load config-file
    logdict = open_log(os.path.join(os.getcwd(), 'config', 'logging.ini'))
    logging.config.dictConfig(logdict)

    # create UC2-Logger and add to config
    logger = logger_create('UC2', log_path_full)

    # manipulate root-logger -> no effect, as kivy manipulated logging before already
    #rootLog = logging.RootLogger.root
    #rootLog.handlers += logger.handlers


    # switch kivy-logger
    kivyLog = logging.root
    kn = 1
    kname = kivyLog.handlers[kn].name
    kivyLog.handlers[kn] = logger.handlers[0]
    kivyLog.handlers[kn].name = kname

    # finish
    logger.debug("Logging successfully initialized to -> " + logging_filename)

