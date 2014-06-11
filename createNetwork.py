__author__ = 'tlindener'
from DockerContainer import DockerContainer
from OpenVSwitch import OpenVSwitch
import time
 
ovs = DockerContainer("","davetucker/docker-ovs:2.1.2")
ovs.create("/bin/supervisord -n",[6633, 6640, 6644])
ovs.run({6633: 6633, 6640: 6640, 6644: 6644})
<<<<<<< HEAD
time.sleep(10)
bridgeName = "ovsbr0"
=======
time.sleep(5)
>>>>>>> origin/iotframework-python
switch = OpenVSwitch("tcp:172.17.42.1:6640")
switch.addBridge(bridgeName)

container = DockerContainer("/home/iot/iotframework/mqttserver/","tlindener/mqttserver")
container.build()
container.create("/usr/bin/supervisord",[22,1883])
container.run({22: 5000, 1883: 1883})
switch.attachContainerToBridge(bridgeName,container.ContainerPid,ovs.ContainerPid,"eth1","eth5","192.168.5.5/24")

for a in range(6,10):
	container2 = DockerContainer("/home/iot/iotframework/mqttclient/","tlindener/mqttclient")
	container2.build()
	container2.create("",[])
	container2.run({})
	address = "192.168.5.%d/24" % a
	devicename = "eth%d" % a
	switch.attachContainerToBridge(bridgeName,container2.ContainerPid,ovs.ContainerPid,"eth1",devicename,address)

