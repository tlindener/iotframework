FROM ubuntu
MAINTAINER Tobias Lindener <tobias.lindener@outlook.com>

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y libfuse2
RUN cd /tmp ; apt-get download fuse
RUN cd /tmp ; dpkg-deb -x fuse_* .
RUN cd /tmp ; dpkg-deb -e fuse_*
RUN cd /tmp ; rm fuse_*.deb
RUN cd /tmp ; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst
RUN cd /tmp ; dpkg-deb -b . /fuse.deb
RUN cd /tmp ; dpkg -i /fuse.deb

RUN apt-get install openjdk-7-jdk openjdk-7-jre unzip apt-utils wget build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev -y
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64
RUN mkdir -p /usr/local/src
RUN cd /usr/local/src; wget -O hivemq.zip  http://www.hivemq.com/downloads/releases/latest
RUN cd /usr/local/src; unzip hivemq.zip
RUN chmod 755 /usr/local/src/hivemq-1.5.0/bin/run.sh 

EXPOSE 1883
CMD ["/usr/local/src/hivemq-1.5.0/bin/run.sh"]



	
