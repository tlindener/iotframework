FROM phusion/baseimage
MAINTAINER Tobias Lindener <tobias.lindener@gmail.com>

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN echo "root:iot" |chpasswd
# Bad security, add a user and sudo instead!
RUN sed --in-place=.bak 's/without-password/yes/' /etc/ssh/sshd_config
RUN apt-get install apt-utils wget build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev openssh-server -y

RUN mkdir -p /usr/local/src
RUN wget -O - http://mosquitto.org/files/source/mosquitto-1.3.tar.gz | tar -xvz -C /usr/local/src
RUN cd /usr/local/src/mosquitto-1.3; make; make install
RUN cp /usr/local/src/mosquitto-1.3/lib/libmosquitto.so.1 /lib/libmosquitto.so.1 

RUN adduser --system --disabled-password --disabled-login mosquitto
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 1883
EXPOSE 22
CMD ["/usr/local/sbin/mosquitto"]
