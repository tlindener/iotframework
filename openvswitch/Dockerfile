FROM ubuntu

MAINTAINER Tobias Lindener <tobias.lindener@gmail.com>

RUN apt-get update
RUN apt-get install udev openssh-server supervisor apt-utils wget build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev gcc make libtool openssl libssl-dev autoconf automake python-dev linux-headers-generic wget -y


RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN echo 'root:root' |chpasswd
RUN sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional pam_loginuid.so/g' /etc/pam.d/sshd
RUN mkdir -p /usr/local/src
RUN wget -O - http://openvswitch.org/releases/openvswitch-2.1.2.tar.gz | tar -xvz -C /usr/local/src
RUN cd /usr/local/src/openvswitch-2.1.2; ./configure; make; make install
RUN mkdir -p /dev/net
RUN mkdir -p /usr/local/etc/openvswitch
RUN ovsdb-tool create
RUN ovsdb-server --remote=punix:/usr/local/var/run/openvswitch/db.sock --detach
EXPOSE 6640 6633 6644

CMD ["/usr/bin/supervisord"]
