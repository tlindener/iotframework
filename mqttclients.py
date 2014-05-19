__author__ = 'tlindener'
from DockerContainer import DockerContainer

container = DockerContainer("mqttserver/","tlindener/mqttclient")
container.build()
for a in range(6,10):
	container.create()
	container.run()
	address = "192.168.5.%d/24" % a
	container.attachtonetwork("br1",address)


