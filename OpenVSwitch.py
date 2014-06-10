__author__ = 'tlindener'
import docker
import subprocess

class OpenVSwitch(object):
    

	def __init__(self, switchaddress):
		self.SwitchAddress = "--db=%d" % switchaddress
	
	def addBridge(self,name):
		subprocess.call(["ovs-vsctl",self.SwitchAddress,"add-br",name])
		subprocess.call(["ovs-vsctl",self.SwitchAddress,"set","bridge",name,"datapath_type=netdev"])
		
	def addPortToBridge(self,port,bridge):
		subprocess.call(["ovs-vsctl",self.SwitchAddress,"add-port",bridge,port])
