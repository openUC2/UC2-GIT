#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:24:49 2020

@author: bene
"""

# -*- coding: utf-8 -*-
 
import paho.mqtt.client as mqtt
 
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("message received: ", msg)
    print("message topic: ", message.topic)
 
def on_connect(client, userdata, flags, rc):
    client.subscribe('/home/data')
 
BROKER_ADDRESS = "localhost"
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(BROKER_ADDRESS)
 
print("Connected to MQTT Broker: " + BROKER_ADDRESS)
 
client.loop_forever()