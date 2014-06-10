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
		
    @property
    def ContainerPid(self):
        """I'm the 'x' property."""
        return self.ContainerPid

    def build(self):
        self.DockerBuildResult = self.docker.build(path=self.Dockerfilepath, tag=self.Tag, quiet=False, fileobj=None,
                                               nocache=False,
                                               rm=True, stream=False, timeout=None)

    def create(self,initcommand,ports):
        if not initcommand:
		initcommand = None
	self.DockerCreateResult = self.docker.create_container(self.Tag, command=initcommand, hostname=None, user=None,
                                                       detach=False, stdin_open=False, tty=False, mem_limit=0,
                                                       ports=None, environment=None, dns=None, volumes=None,
                                                       volumes_from=None, network_disabled=False, name=None,
                                                       entrypoint=None, cpu_shares=None, working_dir=None)
        return self.DockerCreateResult.get("Id")

    def run(self,portbindings):
        result = self.docker.start(self.DockerCreateResult, port_bindings=portbindings)
        self.StartedContainer.append(result)
	self.ContainerPid = result.get("Pid")
	netnspath = "/var/run/netns/%d" % pid
	procpath = "/proc/%d/ns/net" % pid
	subprocess.call(["rm","-f",netnspath])
	subprocess.call(["ln","-s",procpath,netnspath])
		

    def kill(self):
        self.docker.kill(self.DockerCreateResult.get("Id"))

    def attachtonetwork(self,foreignNamespace,foreignDevice,ownDevice,ipAddress):
	tempDeviceName = "xcdf"
	tempDeviceName2 = "local-%d" % tempDeviceName
	subprocess.call(["ip","link","add","name",tempDeviceName,"type","veth","peer","name",tempDeviceName2])
	subprocess.call(["ip","link","set",tempDeviceName,"netns",foreignNamespace])
	subprocess.call(["ip","link","set",tempDeviceName2,"netns",self.ContainerPid])
	subprocess.call(["ip","netns","exec",self.ContainerPid,"ip","link","set",tempDeviceName2,"name",ownDevice])
	subprocess.call(["ip","netns","exec",foreignNamespace,"ip","link","set",tempDeviceName,"name",foreignDevice])
	switch = OpenVSwitch("tcp:172.17.42.1:6640")
	switch.addPortToBridge("ovsbr0",foreignDevice)
	subprocess.call(["ip","netns","exec",self.ContainerPid,"ifconfig",ownDevice,ipAddress,"up"])
	subprocess.call(["ip","netns","exec",foreignNamespace,"ip","link","set",foreignDevice,"up"])
				  

		
	
