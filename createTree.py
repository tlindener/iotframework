__author__ = 'tlindener'
from DockerContainer import DockerContainer
from OpenVSwitch import OpenVSwitch
import time
 
ovs1 = DockerContainer("","davetucker/docker-ovs:2.1.2")
ovs1.create("/bin/supervisord -n",[6633, 6640, 6644])
ovs1.run({6633: 6611, 6640: 6612, 6644: 6613})
bridgeName = "ovsbr0"
ovs2 = DockerContainer("","davetucker/docker-ovs:2.1.2")
ovs2.create("/bin/supervisord -n",[6633, 6640, 6644])
ovs2.run({6633: 6621, 6640: 6622, 6644: 6623})
ovs3 = DockerContainer("","davetucker/docker-ovs:2.1.2")
ovs3.create("/bin/supervisord -n",[6633, 6640, 6644])
ovs3.run({6633: 6631, 6640: 6632, 6644: 6633})
time.sleep(3)
ovsadr1 = "tcp:172.17.42.1:6612"
ovsadr2 = "tcp:172.17.42.1:6622"
ovsadr3 = "tcp:172.17.42.1:6632"
ovsswitch1= OpenVSwitch(ovsadr1)
ovsswitch1.addBridge(bridgeName)
ovsswitch2=OpenVSwitch(ovsadr2)
ovsswitch2.addBridge(bridgeName)
ovsswitch3=OpenVSwitch(ovsadr3)
ovsswitch3.addBridge(bridgeName)

ovsswitch1.attachSwitchToBridge(bridgeName,ovsadr2,ovs2.ContainerPid,"eth1",bridgeName,ovs1.ContainerPid,"eth1","192.168.1.2/24")
ovsswitch1.attachSwitchToBridge(bridgeName,ovsadr3,ovs3.ContainerPid,"eth1",bridgeName,ovs1.ContainerPid,"eth2","192.168.1.3/24")


container = DockerContainer("/home/iot/iotframework/mqttserver/","tlindener/mqttserver")
container.build()
container.create("/usr/bin/supervisord",[22,1883])
container.run({22: 5000, 1883: 1883})
ovsswitch2.attachContainerToBridge(bridgeName,container.ContainerPid,ovs2.ContainerPid,"eth1","eth5","192.168.5.5/24")

for a in range(6,33):
	container2 = DockerContainer("/home/iot/iotframework/mqttclient/","tlindener/mqttclient")
	container2.build()
	container2.create("",[])
	container2.run({})
	address = "192.168.5.%d/24" % a
	devicename = "eth%d" % a
	ovsswitch3.attachContainerToBridge(bridgeName,container2.ContainerPid,ovs3.ContainerPid,"eth1",devicename,address)
for a in range(34,66):
	container2 = DockerContainer("home/iot/iotframework/mqttclient/","tlindener/mqttclient")
	container2.create("",[])
	container2.run({})
	address = "192.168.5.%d/24" % a
	devicename = "eth%d" % a
	ovsswitch2.attachContainerToBridge(bridgeName,container2.ContainerPid,ovs2.ContainerPid,"eth1",devicename,address)
