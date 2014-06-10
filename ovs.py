__author__ = 'tlindener'
import docker
import subprocess


self.docker = docker.Client(base_url='unix://var/run/docker.sock',
                                    version='1.7',
                                    timeout=10)
self.DockerCreateResult = self.docker.create_container(davetucker/docker-ovs:2.1.2, command="/bin/supervisord -n", hostname=None, user=None,
                                                       detach=False, stdin_open=False, tty=False, mem_limit=0,
                                                       ports=[6633, 6640, 6644], environment=None, dns=None, volumes=None,
                                                       volumes_from=None, network_disabled=False, name=None,
                                                       entrypoint=None, cpu_shares=None, working_dir=None

result = self.docker.start(self.DockerCreateResult, port_bindings={6633:6633, 6640:6640, 6644:6644})