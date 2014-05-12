#!/bin/bash
cd /home/iot/iotframework/nodered
docker build --rm -t tlindener/nodered .
nodered=$(sudo docker run -d -p 1880:1880 --name nodered tlindener/nodered)
cd /home/iot/iotframework
./pipework br1 $nodered 192.168.5.4/24
