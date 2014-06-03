FROM fedora

MAINTAINER Tobias Lindener <tobias.lindener@gmail.com>

RUN yum -q -y update
RUN yum -q -y install gcc make libtool openssl openssl-devel autoconf automake python-devel kernel-devel wget

RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN echo 'root:root' |chpasswd
RUN sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional pam_loginuid.so/g' /etc/pam.d/sshd
RUN mkdir -p /usr/local/src
RUN wget -O - http://openvswitch.org/releases/openvswitch-2.1.2.tar.gz | tar -xvz -C /usr/local/src
RUN cd /usr/local/src/openvswitch-1.3; ./configure; make; make install
RUN mkdir -p /dev/net
RUN mknod /dev/net/tun c 10 200
RUN mkdir -p /usr/local/etc/openvswitch
RUN ovsdb-tool create
RUN ovsdb-server --remote=punix:/usr/local/var/run/openvswitch/db.sock --detach
EXPOSE 6640 6633 6644

CMD ["/usr/bin/supervisord"]
