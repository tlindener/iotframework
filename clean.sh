#!/bin/bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
rm -rf /var/run/netns
