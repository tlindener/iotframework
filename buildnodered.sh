#!/bin/bash
cd /home/iot/iotframework/nodered
docker build --rm -t tlindener/nodered .
nodered=$(sudo docker run -d -P --name nodered tlindener/nodered)
cd /home/iot/iotframework
./pipework br1 $nodered 192.168.5.4/24