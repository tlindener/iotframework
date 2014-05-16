__author__ = 'tlindener'
import docker

class DockerContainer(object):
    StartedContainer = []

    def __init__(self, dockerfilepath, tag):
        self.docker = docker.Client(base_url='unix://var/run/docker.sock',
                                    version='1.9',
                                    timeout=10)
        self.Dockerfilepath = dockerfilepath
        self.Tag = tag


    def build(self):
        self.DockerBuildResult = self.docker.build(path=self.dockerfilepath, tag=self.Tag, quiet=False, fileobj=None,
                                               nocache=False,
                                               rm=True, stream=False, timeout=None,
                                               custom_context=False, encoding=None)
        return self.DockerBuildResult


    def create(self):
        self.DockerCreateResult = self.docker.create_container(self.Tag, command=None, hostname=None, user=None,
                                                       detach=False, stdin_open=False, tty=False, mem_limit=0,
                                                       ports=None, environment=None, dns=None, volumes=None,
                                                       volumes_from=None, network_disabled=False, name=None,
                                                       entrypoint=None, cpu_shares=None, working_dir=None,
                                                       memswap_limit=0)
        return self.DockerCreateResult


    def run(self):
        result = self.docker.start(self.DockerCreateResult)
        self.StartedContainer.append = result


    def runmultiple(self, number):
        for a in range(1, number + 1):
            result = c.start(self.DockerCreateResult)
            self.StartedContainer.append = result


    def kill(self, instance):
        self.docker.kill(instance)


    def killrunning(self):
        for a in self.StartedContainer:
            self.docker.kill(a)
            self.StartedContainer.remove(a)

				  

		
	