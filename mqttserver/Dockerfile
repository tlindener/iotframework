FROM ubuntu
MAINTAINER Tobias Lindener <tobias.lindener@outlook.com>

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install openssh-server supervisor apt-utils wget build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev -y
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /usr/local/src
RUN wget -O - http://mosquitto.org/files/source/mosquitto-1.3.tar.gz | tar -xvz -C /usr/local/src
RUN cd /usr/local/src/mosquitto-1.3; make; make install
RUN cp /usr/local/src/mosquitto-1.3/lib/libmosquitto.so.1 /lib/libmosquitto.so.1 
RUN adduser --system --disabled-password --disabled-login mosquitto
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN echo 'root:root' |chpasswd
# Bad security, add a user and sudo instead!
RUN sed --in-place=.bak 's/without-password/yes/' /etc/ssh/sshd_config
EXPOSE 22 1883
CMD ["/usr/bin/supervisord"]



	
