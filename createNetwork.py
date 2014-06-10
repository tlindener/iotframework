__author__ = 'tlindener'
from DockerContainer import DockerContainer
from OpenVSwitch import OpenVSwitch

 
ovs = DockerContainer("","davetucker/docker-ovs:2.1.2")
ovs.create("/bin/supervisord -n",[6633, 6640, 6644])
ovs.run({6633:6633, 6640:6640, 6644:6644})

switch = OpenVSwitch("tcp:172.17.42.1:6640")
switch.addBridge("ovsbr0")

container = DockerContainer("/home/iot/iotframework/mqttserver/","tlindener/mqttserver")
container.build()
container.create()
container.run({})
container.attachtonetwork(ovs.ContainerPid,"eth5","eth1","192.168.5.5/24")

container2 = DockerContainer("mqttserver/","tlindener/mqttclient")
container2.build()
for a in range(6,10):
	container2.create()
	container2.run({})
	address = "192.168.5.%d/24" % a
	devicename = "eth%d" % a
	container2.attachtonetwork(ovs.ContainerPid,devicename,"eth1",address)
