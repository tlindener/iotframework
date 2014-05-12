#!/bin/bash
while [true]
do
mosquitto_pub -h 192.168.5.5 -p 1883 -t test -m "mosquitto is alive"
done