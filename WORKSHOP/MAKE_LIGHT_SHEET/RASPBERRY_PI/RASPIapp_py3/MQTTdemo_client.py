import paho.mqtt.client as mqtt
import time
import sys

# functions


def on_connect(client, userdata, flags, rc):
    if rc == 0:  # connection established
        client.connected_flag = True
        print("Connected with result code = {0}".format(rc))
    else:
        print("Connection error")
        client.bad_connection_flag = True


def on_message(client, userdata, message):
    #print("on message")
    a = time.time()
    print("Time on receive={0}".format(a))
    if message == "off":
        client.turnoff_flag = True
    print("Received={0}\nTopic={1}\nQOS={2}\nRetain Flag={3}".format(
        message.payload.decode("utf-8"), message.topic, message.qos, message.retain))


def on_disconnect(client, userdata, rc):
    #logging.info("disconnecting reason: {0}".format)
    print("disconnecting reason: {0}".format)
    client.connected_flag = False
    client.disconnect_flag = True


# Variables ------------------------------------------------------------------------------------------
setup_name = "S0"
broker = "10.9.2.116"  # "192.168.43.151"  # "10.9.1.62"  # "192.168.43.239"

mqttclient_name = "raspi1"
mqttclient_pass = "1ipsar"
mqttclient_ID = "Raspi1"
port = 1883
keepalive = 60
# flags
mqtt.Client.connected_flag = False  # create flag in class
mqtt.Client.bad_connection_flag = False  # new flag
mqtt.Client.disconnect_flag = False
mqtt.Client.turnoff_flag = False
# define broker
mqttclient = mqtt.Client(mqttclient_ID)  # creates a new client
mqttclient.username_pw_set(mqttclient_name, mqttclient_pass)
# attach functions to client
mqttclient.on_connect = on_connect
mqttclient.on_message = on_message
mqttclient.on_disconnect = on_disconnect
# start loop to process received messages
mqttclient.loop_start()
try:
    print("MQTTClient: connecting to broker ", broker)
    mqttclient.connect(broker, port, keepalive)
    while not mqttclient.connected_flag and not mqttclient.bad_connection_flag:
        print("MQTTClient: Waiting for established connection.")
        time.sleep(1)
    if mqttclient.bad_connection_flag:
        mqttclient.loop_stop()
        print("MQTTClient: had bad-connection. Not trying to connect any further.")
except Exception as err:  # e.g. arises when port errors exist etc
    print("MQTTClient: Connection failed")
    print(err)

mqttclient.subscribe("S0/MOTz1/MOV", qos=1)
mqttclient.publish("S0/MOTz1/MOV", "1", qos=1, retain=False)

time.sleep(2)
print("waiting for flush")
time.sleep(2)
