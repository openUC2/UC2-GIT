import errno
import fluidiscopeGlobVar as fg
from fluidiscopeLogging import logger_createChild
import logging
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
    logger = ''
    logging_active = True

    def __init__(self, setup, device):
        self.setup = setup
        self.device = device
        self.topic_base = "/" + self.setup + "/" + self.device + "/"
        self.mqtt_subscribe()
        self.logger = logger_createChild(self.topic_base,'UC2')

    def mqtt_subscribe(self, *args):
        fg.mqttclient.subscribe(self.topic_base + self.topic_announce)
        fg.mqttclient.subscribe(self.topic_base + self.topic_status)

    def send(self, *args, **kwargs):
        self.payload = self.extractCommand(args,kwargs)
        # if fg.my_dev_flag:
        #    print(
        #        "Debugging mode. Generated Command=[{}] has not been sent.".format(cmd))
        # else:
        # print("MQTTclient: Topic={0}, Payload=".format(cmd))
        fg.mqttclient.publish(self.topic_base + self.topic_send, self.payload)

    def extractCommand(self, *args, **kwargs):
        cmd = ""
        delim = MQTTDevice.delim_inst  # so that it is not different per instances
        #self.logger.debug("MQTTclient_extractCommand -> starting for: {}".format(args))
        logme = True
        # check whether logging-directive was attached
        if type(args[-1])== dict:
            if 'logging' in args[-1]:
                logme = args[-1]['logging']
            args=args[0]

        for i, arg in enumerate(args):
            if type(arg) == list:
                sep = [str(x) for x in arg]
                # if i == 0:
                #    self.topic = self.topic_base + sep[0]
                #    sep = sep[1:]
                cmd += delim.join(sep)
            else:
                # if i == 0:
                #    sep = arg.split(MQTTDevice.delim_inst)
                #    self.topic = self.topic_base + sep[0]
                #    arg = delim.join(sep[1:])
                #    arg += delim if not (arg == "") else ""
                cmd += str(arg)
            cmd += delim
                # if i > 0:
                 
        if logme:
            self.logger.debug("MQTTDevice_extractCommand -> topic_spec={}, cmd={}.".format(self.topic_base, cmd[:-1]))
        return cmd[:-1]

    # def request(self):
    #    ans = self.requestEvent()
    #    if ans and (ans != "BUSY"):
    #        print("Receiving: {0}".format(ans))
    #        return ans

    # def sendCommand(self, *args):
    #    self.send(*args)
    #    time.sleep(0.0025)
    #    return self.request()
