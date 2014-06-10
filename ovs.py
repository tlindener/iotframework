from __future__ import print_function
__author__ = 'tlindener'
import docker

docker = docker.Client(base_url='unix://var/run/docker.sock',
                                    version='1.9',
                                    timeout=10)
result = docker.create_container("davetucker/docker-ovs:2.1.2", command="/bin/supervisord -n", hostname=None, user=None,
                                                       detach=False, stdin_open=False, tty=False, mem_limit=0,
                                                       ports=[6633, 6640, 6644], environment=None, dns=None, volumes=None,
                                                       volumes_from=None, network_disabled=False, name=None,
                                                       entrypoint=None, cpu_shares=None, working_dir=None)
print(result)
docker.start(result,port_bindings={6633: 6633, 6640: 6640, 6644: 6644})
