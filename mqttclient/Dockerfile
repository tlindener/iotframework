# Build mosquitto from source
FROM ubuntu
MAINTAINER Tobias Lindener <tobias.lindener@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN \ 
    apt-get update ;\
    apt-get upgrade -y ;\
    apt-get install wget build-essential libwrap0-dev libssl-dev python-distutils-extra -y

RUN \
    mkdir -p /usr/local/src ;\
    cd /usr/local/src ;\
    wget http://mosquitto.org/files/source/mosquitto-1.3.tar.gz ;\
    tar xvzf ./mosquitto-1.3.tar.gz ;\
    cd /usr/local/src/mosquitto-1.3 ;\
    make ;\
    make install
	
RUN cp /usr/local/src/mosquitto-1.3/lib/libmosquitto.so.1 /lib/libmosquitto.so.1 
RUN adduser --system --disabled-password --disabled-login mosquitto
ADD client.sh /root/client.sh
CMD ["/root/client.sh"]
