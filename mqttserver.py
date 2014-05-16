__author__ = 'tlindener'

import DockerContainer

container = DockerContainer("./mqttserver/Dockerfile","tlindener/mqttserver")
container.build()
container.create()
container.run()