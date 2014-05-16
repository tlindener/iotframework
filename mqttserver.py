__author__ = 'tlindener'
from DockerContainer import DockerContainer

container = DockerContainer("/home/iot/iotframework/mqttserver/","tlindener/mqttserver")
container.build()
container.create()
container.run()
