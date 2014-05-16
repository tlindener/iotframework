__author__ = 'tlindener'
import docker
import subprocess

class DockerContainer(object):
    StartedContainer = []

    def __init__(self, dockerfilepath, tag):
        self.docker = docker.Client(base_url='unix://var/run/docker.sock',
                                    version='1.7',
                                    timeout=10)
        self.Dockerfilepath = dockerfilepath
        self.Tag = tag


    def build(self):
        self.DockerBuildResult = self.docker.build(path=self.Dockerfilepath, tag=self.Tag, quiet=False, fileobj=None,
                                               nocache=False,
                                               rm=True, stream=False, timeout=None)

    def create(self):
        self.DockerCreateResult = self.docker.create_container(self.Tag, command=None, hostname=None, user=None,
                                                       detach=False, stdin_open=False, tty=False, mem_limit=0,
                                                       ports=None, environment=None, dns=None, volumes=None,
                                                       volumes_from=None, network_disabled=False, name=None,
                                                       entrypoint=None, cpu_shares=None, working_dir=None)
        return self.DockerCreateResult.get("Id")


    def run(self):
        result = self.docker.start(self.DockerCreateResult)
        self.StartedContainer.append(result)

    def kill(self):
        self.docker.kill(self.DockerCreateResult.get("Id"))

    def attachtonetwork(self,bridge,ipaddress):
	subprocess.call(['./pipework',bridge,self.DockerCreateResult.get("Id"),ipaddress])

				  

		
	
