import errno
#import fluidiscopeGlobVar as fg
#from fluidiscopeLogging import logger_createChild
#import logging
import paho.mqtt.client as mqtt
import os
import sys
import time


class MQTTDevice(object):
    '''
    Class that communicates with MQTT devices while mimicing the calling syntax from I2CDevice
    '''
    # delimiters
    # delim_strt = "*"
    # delim_stop = "#"
    delim_cmds = ";"
    delim_inst = "+"
    # common commands
    com_cmds = {"STATUS": "STATUS", "LOGOFF": "LOGOFF", "NAME": "NAME"}
    # MQTT-data
    topic_send = "RECM"  # topic for commands received by device
    topic_status = "STAT"
    topic_announce = "ANNO"

    # add logger
    #logger = ''
    logging_active = True

    def __init__(self, setup, device, mqtt_client):
        self.setup = setup
        self.device = device
        self.mqtt_client = mqtt_client
        self.topic_base = "/" + self.setup + "/" + self.device + "/"
        self.mqtt_subscribe()
        #self.logger = logger_createChild(self.topic_base,'UC2')

    def mqtt_subscribe(self, *args):
        self.mqtt_client.subscribe(self.topic_base + self.topic_announce)
        self.mqtt_client.subscribe(self.topic_base + self.topic_status)

    def send(self, *args, **kwargs):
        self.payload = self.extractCommand(args,kwargs)
        self.mqtt_client.publish(self.topic_base + self.topic_send, self.payload)

    def extractCommand(self, *args, **kwargs):
        cmd = ""
        delim = MQTTDevice.delim_inst  # so that it is not different per instances
        logme = True

        # check whether logging-directive was attached
        if type(args[-1])== dict:
            if 'logging' in args[-1]:
                logme = args[-1]['logging']
            args=args[0]

        for i, arg in enumerate(args):
            if type(arg) == list:
                sep = [str(x) for x in arg]
                cmd += delim.join(sep)
            else:
                cmd += str(arg)
            cmd += delim
                 
        if logme:
            print("MQTTDevice_extractCommand -> topic_spec={}, cmd={}.".format(self.topic_base, cmd[:-1]))
        return cmd[:-1]
