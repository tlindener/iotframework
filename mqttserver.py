__author__ = 'tlindener'
from DockerContainer import DockerContainer

container = DockerContainer("/home/iot/iotframework/mqttserver/","tlindener/mqttserver")
container.build()
container.create()
container.run()
container.attachtonetwork("br1","192.168.5.5/24")


