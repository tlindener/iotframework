#!/bin/bash
cd /home/iot/iotframework/lighttpd
docker build --rm -t tlindener/lighttpd .
lighttpd=$(sudo docker run -d -p 80:80 --name lighttpd tlindener/lighttpd)
cd /home/iot/iotframework
./pipework br1 $lighttpd 192.168.5.2/24
