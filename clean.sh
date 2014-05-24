#!/bin/bash
apt-get remove openvswitch-switch -Y
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
rm -rf /var/run/netns
