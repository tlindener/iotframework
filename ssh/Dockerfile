# sshd
#
# VERSION               0.0.1

FROM     ubuntu
MAINTAINER Thatcher R. Peskens "thatcher@dotcloud.com"

# make sure the package repository is up to date
RUN apt-get update
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd 
RUN echo 'root:root' |chpasswd
# Bad security, add a user and sudo instead!
RUN sed --in-place=.bak 's/without-password/yes/' /etc/ssh/sshd_config

EXPOSE 22
CMD    /usr/sbin/sshd -D