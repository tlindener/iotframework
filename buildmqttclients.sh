#!/bin/bash
cd /home/iot/iotframework/mqttclient
docker build --rm -t tlindener/mqttclient .
for i in {6..10}
do
   mqttserver=$(sudo docker run -d -P tlindener/mqttclient)
cd /home/iot/iotframework
./pipework br1 $mqttserver 192.168.5.$i/24
done
