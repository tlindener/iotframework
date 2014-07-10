__author__ = 'tlindener'
import docker
import subprocess
from OpenVSwitch import OpenVSwitch

class DockerContainer(object):
    StartedContainer = []

    def __init__(self, dockerfilepath, tag):
        self.docker = docker.Client(base_url='unix://var/run/docker.sock',
                                    version='1.9',
                                    timeout=10)
        self.Dockerfilepath = dockerfilepath
        self.Tag = tag
	self._ContainerPid = None		
    @property
    def ContainerPid(self):
        return self._ContainerPid

    @ContainerPid.setter
    def ContainerPid(self, value):
	print(value)
	self._ContainerPid = value

    def build(self):
        self.DockerBuildResult = self.docker.build(path=self.Dockerfilepath, tag=self.Tag, quiet=False, fileobj=None,
                                               nocache=False,
                                               rm=True, stream=False, timeout=None)

    def create(self,initcommand,ports):
        if not initcommand:
		initcommand = None
	self.DockerCreateResult = self.docker.create_container(self.Tag, command=initcommand, hostname=None, user=None,
                                                       detach=False, stdin_open=False, tty=False, mem_limit=0,
                                                       ports=ports, environment=None, dns=None, volumes=None,
                                                       volumes_from=None, network_disabled=False, name=None,
                                                       entrypoint=None, cpu_shares=None, working_dir=None)
        return self.DockerCreateResult.get("Id")

    def run(self,portbindings):
        self.docker.start(self.DockerCreateResult,privileged=True ,port_bindings=portbindings)
       	result = self.docker.inspect_container(self.DockerCreateResult)
	self.ContainerPid = result.get("State").get("Pid")
	netnspath = "/var/run/netns/%d" % self.ContainerPid
	procpath = "/proc/%d/ns/net" % self.ContainerPid
	subprocess.call(["mkdir","/var/run/netns"])
	subprocess.call(["rm","-f",netnspath])
	subprocess.call(["ln","-s",procpath,netnspath])
		

    def kill(self):
        self.docker.kill(self.DockerCreateResult.get("Id"))

				  

		
	
