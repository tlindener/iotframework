FROM ubuntu
MAINTAINER Tobias Lindener <tobias.lindener@outlook.com>

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install apt-utils wget build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev -y
RUN mkdir -p /usr/local/src
RUN cd /usr/local/src
RUN wget -O - http://www.hivemq.com/downloads/releases/latest
RUN unzip hivemq-1.5.0.zip
RUN cd /usr/local/src/hivemq-1.5.0
RUN chmod 755 run.sh 

EXPOSE 1883
CMD ["/usr/local/src/run.sh"]



	
