from subprocess import STDOUT, check_call
import os
check_call(['apt-get', 'update'],
     stdout=open(os.devnull,'wb'), stderr=STDOUT) 
check_call(['apt-get', 'install', '-y', 'docker.io','bridge-utils','python-pip','openvswitch-controller','openvswitch-switch','openvswitch-datapath-source','python-openvswitch'],
     stdout=open(os.devnull,'wb'), stderr=STDOUT) 
check_call(['ln', '-sf','/usr/bin/docker.io','/usr/local/bin/docker'],
     stdout=open(os.devnull,'wb'), stderr=STDOUT)