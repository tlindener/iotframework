FROM ubuntu

MAINTAINER Tobias Lindener <tobias.lindener@gmail.com>

RUN apt-get update
RUN apt-get install gcc make libtool openssl openssl-devel autoconf automake python-devel kernel-devel wget -y


ADD scripts/install-ovs.sh /tmp/install-ovs.sh

EXPOSE 6640 6633 6644

CMD /tmp/install-run-ovs.sh
