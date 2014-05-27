#!/bin/bash
apt-get remove openvswitch-switch -y
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
rm -rf /var/run/netns
