#!/bin/bash
apt-get update
apt-get install docker.io
ln -sf /usr/bin/docker.io /usr/local/bin/docker
apt-get install bridge-utils