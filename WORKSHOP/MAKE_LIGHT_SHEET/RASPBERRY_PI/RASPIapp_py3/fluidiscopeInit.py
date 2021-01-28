import datetime
import logging
import logging.config
import platform
import os
import serial
import socket
import time
import yaml

from kivy.config import Config
import fluidiscopeGlobVar as fg
import fluidiscopeIO
from fluidiscopeLogging import logger_createChild

import unipath as uni

if fg.i2c:
    from I2CDevice import I2CDevice
    from I2CBus import I2CBus
else:
    from MQTTDevice import MQTTDevice
    import paho.mqtt.client as mqtt

if not fg.my_dev_flag:
    import picamera

# logging Functions ------------------------------------------------------------------------------
logger = logger_createChild('init','UC2')

# General Init ------------------------------------------------------------------------------

def controller_init():
    if fg.i2c:
        arduino_init()
    else:  # case of e.g. ESP32
        mqtt_init()
    camera_init()


def camera_init():
    try:
        arch = os.uname()[4]
    except:
        arch = os.name
    if "arm" in arch:
        fg.camera = picamera.PiCamera()
        #print("cam is online")
        logger.debug("Cam is online.")

    # I2C Functions ------------------------------------------------------------------------------


def arduino_init():
    # address = I2CBus.scanBus()
    fg.ledarr = I2CDevice(0x07)  # normally 0x07
    fg.motors = I2CDevice(0x08)  # normally 0x08
    # time.sleep(1.0) #because accessing same device
    # sits on the same Arduino as motors for now
    fg.fluo = I2CDevice(0x08)
    # fg.ledarr.announce()
    # fg.motors.announce()
    #fluidiscopeIO.send(fg.ledarr, "CLEAR")

# MQTT Functions ------------------------------------------------------------------------------


def mqtt_init():
    # connect to server
    from random import randint
    setup_name = fg.config['comcat']['mqtt_setup']
    device_ID = fg.config['comcat']['mqtt_device_id_prefix'] + str(randint(0, 100000))
    device_MQTT_name = fg.config['comcat']['mqtt_device_name']
    mqtt_connect_to_server(broker=fg.config['comcat']['mqtt_ip'], mqttclient_name=fg.config['comcat']['mqtt_client_name'], mqttclient_pass=fg.config['comcat']['mqtt_client_pass'], mqttclient_ID=device_ID, port=fg.config['comcat']['mqtt_port'], keepalive=fg.config['comcat']['mqtt_keepalive'], use_login=fg.config['comcat']['mqtt_use_login'])

    # register devices
    fg.raspi = mqtt_register_devices(device_MQTT_name,setup_name)
    #fg.raspi = MQTTDevice(setup_name, device_MQTT_name)
    fg.ledarr = mqtt_register_devices(fg.config['comcat']['mqtt_device_LEDS'],setup_name)
    fg.motors = mqtt_register_devices(fg.config['comcat']['mqtt_device_MOTORS'],setup_name)
    fg.fluo = mqtt_register_devices(fg.config['comcat']['mqtt_device_LASER'],setup_name)
    #fg.ledarr = MQTTDevice(setup_name,  fg.config['comcat']['mqtt_device_LEDS'])
    #fg.motors = [MQTTDevice(setup_name, "MOT02"), MQTTDevice(setup_name, "MOT02"), MQTTDevice(setup_name, "MOT01")]
    #fg.fluo = MQTTDevice(setup_name, "MOT01")

def mqtt_register_devices(devices,setup_name):
    '''
    Adds devices to pointers.

    Note: no ERROR-catches! 
    '''
    if devices is None or devices == '':
        namer = None
    elif type(devices) == str:
        namer = MQTTDevice(setup_name, devices)
    else:
        namer = []
        for m in devices:
            namer.append(MQTTDevice(setup_name, m))

    # done?
    return namer

def mqtt_connect_to_server(broker, mqttclient_name, mqttclient_pass, mqttclient_ID, port=1883, keepalive=60, use_login=False):
    mqtt.Client.connected_flag = False  # create flag in class
    mqtt.Client.bad_connection_flag = False  # new flag
    mqtt.Client.disconnect_flag = False
    mqtt.Client.turnoff_flag = False

    # define broker
    fg.mqttclient = mqtt.Client(mqttclient_ID)  # creates a new client
    if use_login:
        fg.mqttclient.username_pw_set(mqttclient_name, mqttclient_pass)

    # attach functions to client
    fg.mqttclient.on_connect = on_connect
    fg.mqttclient.on_message = on_message
    fg.mqttclient.on_disconnect = on_disconnect

    # start loop to process received messages
    fg.mqttclient.loop_start()
    try:
        logger.info("MQTTClient: connecting to broker ".format(broker))
        #print("MQTTClient: connecting to broker ", broker)
        fg.mqttclient.connect(host=broker, port=port, keepalive=keepalive)
        while not fg.mqttclient.connected_flag and not fg.mqttclient.bad_connection_flag:
            logger.info("MQTTClient: Waiting for established connection.")
            #print("MQTTClient: Waiting for established connection.")
            time.sleep(1)
        if fg.mqttclient.bad_connection_flag:
            fg.mqttclient.loop_stop()
            logger.warning(
                "MQTTClient: had bad-connection. Not trying to connect any further.")
            #print("MQTTClient: had bad-connection. Not trying to connect any further.")
    except Exception as err:  # e.g. arises when port errors exist etc
        logger.error("MQTTClient: Connection failed")
        logger.error(err)
        #print("MQTTClient: Connection failed")
        # print(err)

    # TODO: spawn Thread that checks for connection status
    # add:
    # if client1.turnoff_flag:
    #    client1.disconnect()
    #    client1.loop_stop()


def on_connect(client, userdata, flags, rc):
    if rc == 0:  # connection established
        client.connected_flag = True
        logger.info("Connected with result code = {}".format(rc))
        #print("Connected with result code = {0}".format(rc))
    else:
        logger.warning("Connection error")
        #print("Connection error")
        client.bad_connection_flag = True

def on_message(client, userdata, message):
    #print("on message")
    a = time.time().str
    logger.info("Time on receive={0}".format(a))
    #print("Time on receive={0}".format(a))
    if message == "off":
        client.turnoff_flag = True
    logger.info("Received={0}\nTopic={1}\nQOS={2}\nRetain Flag={3}".format(
        message.payload.decode("utf-8"), message.topic, message.qos, message.retain))


def on_disconnect(client, userdata, rc):
    #logging.info("disconnecting reason: {0}".format)
    logger.warning("disconnecting reason: {0}".format)
    client.connected_flag = False
    client.disconnect_flag = True


# Further Functions ------------------------------------------------------------------------------


def GUI_define_sizes():
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '480')
    Config.set('graphics', 'borderless', 'True')
    Config.write()
    pass


def load_config():
    test_text = ""
    fg.code_path = uni.Path.cwd()
    fg.project_path = fg.code_path.parent
    fg.data_path = uni.Path(fg.code_path, "data")
    fg.save_path = uni.Path(fg.data_path, str(fg.today))
    fg.config_path = uni.Path(fg.code_path, "config")
    fg.config_file = uni.Path(fg.config_path, "main_config.yaml")
    fg.config = fluidiscopeIO.load_config(fg.config_file)
    fg.autofocus_path = uni.Path(fg.code_path, "autofocus")
    fg.copy_path = ""

    if not fg.config:
        fluidiscopeIO.restore_config()
        test_text = "from backup "
        fg.config = fluidiscopeIO.load_config(fg.config_file)
    print("Configuration file {0}loaded".format(test_text))

    # add further security changes
    # should always be empty if no imaging technique is chosen
    fg.config['experiment']['active_methods'] = []
