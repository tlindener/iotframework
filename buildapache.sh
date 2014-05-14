#!/bin/bash
cd /home/iot/iotframework/apache
docker build --rm -t tlindener/apache .
apache=$(sudo docker run -d -p 80:80 --name apache tlindener/apache)
cd /home/iot/iotframework
./pipework br1 $apache 192.168.5.3/24
