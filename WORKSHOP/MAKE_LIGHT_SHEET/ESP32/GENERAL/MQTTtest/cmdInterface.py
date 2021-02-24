'''
    Simplified command-line interface to just talk to the MQTT-modules directly
    
'''

# %% imports 
from MQTTDevice import MQTTDevice
import paho.mqtt.client as mqtt
from random import randint
from time import time, sleep


# global parameters
__author__ = "René Lachmann"
__date__ = "02.07.2020" 
__version__ = "0.1a"



# %% function definitions

class MQTTtest():
    '''
    Simple class to contain necessary code elements
    '''

    def __init__(self,setup_name,device_ID,device_MQTT_name,mqtt_broker_ip,mqtt_client_name,mqtt_client_pass,mqtt_port,mqtt_keepalive,mqtt_uselogin):
        
        # get parameters and store in instance
        self.setup_name         = setup_name
        self.device_ID          = device_ID
        self.device_MQTT_name   = device_MQTT_name
        self.mqtt_broker_ip     = mqtt_broker_ip
        self.mqtt_client        = None
        self.mqtt_client_name    = mqtt_client_name
        self.mqtt_client_pass    = mqtt_client_pass
        self.mqtt_port          = mqtt_port
        self.mqtt_keepalive     = mqtt_keepalive
        self.mqtt_uselogin      = mqtt_uselogin
        self.devices            = {}
        
        # connect to MQTT server
        self.mqtt_connect_to_server()

    def mqtt_register_devices(self, device_name, device_ID):
        '''
        Adds devices to pointers.

        Note: no ERROR-catches! 
        '''
        self.devices[device_name] = MQTTDevice(setup=self.setup_name, device=device_ID,mqtt_client=self.mqtt_client)

    def mqtt_connect_to_server(self):
        mqtt.Client.connected_flag = False  # create flag in class
        mqtt.Client.bad_connection_flag = False  # new flag
        mqtt.Client.disconnect_flag = False
        mqtt.Client.turnoff_flag = False

         # define broker
        self.mqtt_client = mqtt.Client(self.device_MQTT_name)  # creates a new client
        if self.mqtt_uselogin:
            self.mqtt_client.username_pw_set(self.mqtt_client_name, self.mqtt_client_pass)

        # attach functions to client
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.on_disconnect = self.on_disconnect

        # start loop to process received messages
        self.mqtt_client.loop_start()

        try:
            print("mqtt_client: connecting to broker ".format(self.mqtt_broker_ip))
            self.mqtt_client.connect(host=self.mqtt_broker_ip, port=self.mqtt_port, keepalive=self.mqtt_keepalive)
            
            
            while not self.mqtt_client.connected_flag and not self.mqtt_client.bad_connection_flag:
                print("mqtt_client: Waiting for established connection.")
                sleep(1)
            
            if self.mqtt_client.bad_connection_flag:
                self.mqtt_client.loop_stop()
                print(
                    "WARNING -> mqtt_client: had bad-connection. Not trying to connect any further.")
                
        except Exception as err:  # e.g. arises when port errors exist etc
            print("mqtt_client: Connection failed")
            print(err)


    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:  # connection established
            client.connected_flag = True
            #logger.info("Connected with result code = {}".format(rc))
            print("Connected with result code = {}".format(rc))
        else:
            #logger.warning("Connection error")
            print("Connection error")
            client.bad_connection_flag = True

    def on_message(self, client, userdata, message):
        if message == "off":
            client.turnoff_flag = True
        print("Time on receive={}\nReceived={}\nTopic={}\nQOS={}\nRetain Flag={}".format(time().str,message.payload.decode("utf-8"), message.topic, message.qos, message.retain))


    def on_disconnect(self, client, userdata, rc):
        
        print("disconnecting reason: {}".format(rc))
        client.connected_flag = False
        client.disconnect_flag = True

    def commanddef(self):
        '''
        prints a list of available commands
        '''
        self.command_dict = {'i': 'individual pixel', 'o': 'off', 'r': 'rectangular', 'x': 'exit'}
        print('The following commands are avialable:\n================================')
        for m in self.command_dict:
            print("{}: {}".format(m,self.command_dict[m]))
                            
    def loop(self,use_device):
        print('What shall be done?')
        self.commanddef()
        while True:    
            cmd = input()
                
            if cmd == 'i':
                self.devices[use_device].send("CLEAR")
                self.devices[use_device].send("PXL", 35, 40, 127, 200)
            elif cmd in ['o','x']:
                self.devices[use_device].send("CLEAR")
                self.devices[use_device].send("CLEAR")
                if cmd == 'x':
                    break
            elif cmd == 'r':
                self.devices[use_device].send("NA+3")
                self.devices[use_device].send("RECT+0+0+8+8+1", 120, 120, 120)
            else: 
                print('Nothing to do here...')

        print('Have fun :)')

if __name__ == '__main__':
    # set parameters
    setup_name          = "S001"
    device_ID           = "RAS01"
    device_MQTT_name    = "RASPI_" + str(randint(0, 100000))
    mqtt_broker_ip      = "localhost"
    mqtt_client_name    = "raspi1" # not necessary
    mqtt_client_pass    = "1ipsar" # not necessary
    mqtt_port           = 1883
    mqtt_keepalive      = 60
    mqtt_uselogin       = False

    # init class and auto-connect to server
    uc2 = MQTTtest(setup_name=setup_name,device_ID=device_ID,device_MQTT_name=device_MQTT_name,mqtt_broker_ip=mqtt_broker_ip,mqtt_client_name=mqtt_client_name,mqtt_client_pass=mqtt_client_pass,mqtt_port=mqtt_port,mqtt_keepalive=mqtt_keepalive,mqtt_uselogin=mqtt_uselogin)

    # add devices for testing -> LED
    uc2.mqtt_register_devices(device_name='LED',device_ID='LAR01')
    uc2.devices['LED'].send("CLEAR")
    uc2.devices['LED'].send("CLEAR")

    # add a motor ... and so on
    uc2.mqtt_register_devices(device_name='Motor_z',device_ID='MOT01')
    uc2.mqtt_register_devices(device_name='Motor_x',device_ID='MOT02')
    uc2.mqtt_register_devices(device_name='Motor_y',device_ID='MOT02')

    # loop for userinput
    uc2.loop(use_device='LED')
