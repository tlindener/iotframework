#!/bin/bash
cd /home/iot/iotframework/hivemq
docker build --rm -t tlindener/hivemq .
hivemq=$(sudo docker run -d -P --name hivemq tlindener/hivemq)
cd /home/iot/iotframework
./pipework br1 $hivemq 192.168.5.5/24
