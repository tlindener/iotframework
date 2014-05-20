#!/bin/bash
cd /home/iot/iotframework/mqttclient
docker build --rm -t tlindener/mqttclient .
for i in {6..10}
do
	mqttserver=$(sudo docker run -d -P tlindener/mqttclient)
	sudo docker inspect --format='{{ .State.Pid }}' $mqttserver 	
done

cd /home/iot/iotframework/mqttserver
docker build --rm -t tlindener/mqttserver .
mqttserver=$(sudo docker run -d -P tlindener/mqttserver)
sudo docker inspect --format='{{ .State.Pid }}' $mqttserver
