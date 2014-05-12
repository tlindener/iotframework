# Build mosquitto from source
FROM ubuntu
MAINTAINER Tobias Lindener <tobias.lindener@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN \ 
    apt-get update ;\
    apt-get upgrade -y ;\
    apt-get install wget build-essential libwrap0-dev libssl-dev python-distutils-extra -y

RUN apt-get install apt-utils wget build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev -y
RUN mkdir -p /usr/local/src
RUN wget -O - http://mosquitto.org/files/source/mosquitto-1.3.tar.gz | tar -xvz -C /usr/local/src
RUN cd /usr/local/src/mosquitto-1.3; make; make install
RUN cp /usr/local/src/mosquitto-1.3/lib/libmosquitto.so.1 /lib/libmosquitto.so.1 
RUN adduser --system --disabled-password --disabled-login mosquitto

	
RUN cp /usr/local/src/mosquitto-1.3/lib/libmosquitto.so.1 /lib/libmosquitto.so.1 
RUN adduser --system --disabled-password --disabled-login mosquitto
ADD client.sh /root/client.sh
CMD ["/root/client.sh"]
