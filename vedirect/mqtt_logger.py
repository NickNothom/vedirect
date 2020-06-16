#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse, os, time
from vedirect import Vedirect
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
mqttc = mqtt.Client()
mqttc.username_pw_set("mqtt", password="companion")

def print_data_callback(packet):
    #publish.single("vedirect/PPV", str(packet["PPV"]), hostname="ion.local")
    mqttc.publish("homeassistant/sensor/blueboat/state", packet["PPV"])
    print(packet["PPV"])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process VE.Direct protocol')
    parser.add_argument('--port', help='Serial port')
    parser.add_argument('--timeout', help='Serial port read timeout', type=int, default='60')
    args = parser.parse_args()
    ve = Vedirect(args.port, args.timeout)
    mqttc.connect("ion.local")
    mqttc.loop_start()
    print(ve.read_data_callback(print_data_callback))
