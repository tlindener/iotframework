__author__ = 'tlindener'
import docker
import subprocess

class OpenVSwitch(object):
    
	def __init__(self, switchaddress):
		self.SwitchAddress = "--db=%s" % switchaddress
		self.Bridges = []
	
	def addBridge(self,name):
		subprocess.call(["ovs-vsctl",self.SwitchAddress,"add-br",name])
		subprocess.call(["ovs-vsctl",self.SwitchAddress,"set","bridge",name,"datapath_type=netdev"])
		self.Bridges.append(name)
	def addPortToBridge(self,bridge,port):
		subprocess.call(["ovs-vsctl",self.SwitchAddress,"add-port",bridge,port])
	def attachContainerToBridge(self,bridge,containerPid,switchPid,containerDevice,switchDevice,ipAddress):
		tempDeviceName = "xcdf"
		tempDeviceName2 = "local-%s" % tempDeviceName
		subprocess.call(["ip","link","add","name",tempDeviceName,"type","veth","peer","name",tempDeviceName2])
		subprocess.call(["ip","link","set",tempDeviceName,"netns",str(switchPid)])
		subprocess.call(["ip","link","set",tempDeviceName2,"netns",str(containerPid)])
		subprocess.call(["ip","netns","exec",str(containerPid),"ip","link","set",tempDeviceName2,"name",containerDevice])
		subprocess.call(["ip","netns","exec",str(switchPid),"ip","link","set",tempDeviceName,"name",switchDevice])
		self.addPortToBridge(bridge,switchDevice)
		subprocess.call(["ip","netns","exec",str(containerPid),"ifconfig",containerDevice,ipAddress,"up"])
		subprocess.call(["ip","netns","exec",str(switchPid),"ip","link","set",switchDevice,"up"])
	def attachSwitchToBridge(self,foreignBridge,foreignSwitchAddress,foreignSwitchPid, foreignSwitchDevice,switchBridge,switchPid,switchDevice,ipAddress):
		switch = OpenVSwitch(foreignSwitchAddress)
		switch.addPortToBridge(foreignBridge,foreignSwitchDevice)
		self.attachContainerToBridge(switchBridge,foreignSwitchPid,switchPid,foreignSwitchDevice,switchDevice,ipAddress)
