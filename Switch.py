__author__ = 'tlindener'

class Switch:
	
	def __init__(self,ports,bridgeName):
		self.Container = DockerContainer("","davetucker/docker-ovs:2.1.2")
		ovs1.create("/bin/supervisord -n",[6633, 6640, 6644])
		ovs1.run(ports)
		time.sleep(3)
		self.BridgeName = bridgeName
		self.ctladdress = "tcp:172.17.42.1:%d" % ports[6640]
		self.OpenVSwitch = OpenVSwitch(self.ctladdress)
		self.OpenVSwitch.addBridge(bridgeName)
		
	@property
    def Container(self):
        return self.Container
		
	@property
    def OpenVSwitch(self):
        return self.OpenVSwitch
	
	@property
    def ContainerPid(self):
        return self.Container.ContainerPid
		
	@property
    def Bridge(self):
        return self.BridgeName
	
	@property
    def Address(self):
        return self.ctladdress
	
	def attachSwitchToBridge(self,foreignSwitch,foreignDevice,device,ipaddress):
		self.OpenVSwitch.attachSwitchToBridge(foreignSwitch.Bridge,foreignSwitch.Address,foreignSwitch.ContainerPid,foreignDevice,device,ipaddress)
		
	def attachContainerToBridge(self,containerPid,containerDevice,ipAddress):
		self.OpenVSwitch.attachSwitchToBridge(self.BridgeName,containerPid,self.ContainerPid,switchDevice,ipAddress)