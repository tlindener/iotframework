FROM ubuntu

MAINTAINER Tobias Lindener <tobias.lindener@gmail.com>

RUN apt-get update
RUN apt-get install openvswitch-controller openvswitch-brcompat openvswitch-switch openvswitch-datapath-source udev openssh-server supervisor apt-utils wget build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev gcc make libtool openssl libssl-dev autoconf automake python-dev linux-headers-generic wget -y


RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisord/supervisord.conf
RUN echo 'root:root' |chpasswd
RUN sed --in-place=.bak 's/without-password/yes/' /etc/ssh/sshd_config
EXPOSE 22 6640 6633 6644

CMD ["/usr/bin/supervisord -c /etc/supervisord"]
