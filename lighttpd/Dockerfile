FROM ubuntu
MAINTAINER Tobias Lindener <tobias.lindener@gmail.com>

# Install the relevant packages
RUN apt-get update
RUN apt-get install automake libtool pkg-config libpcre3 libpcre3-dev openssl libssl-dev git libbz2-dev -y

RUN mkdir -p /usr/local/src
RUN git clone --recursive git://github.com/nori0428/mod_websocket.git
RUN git clone --recursive https://github.com/lighttpd/lighttpd1.4.git
RUN cd lighttpd1.4
RUN git checkout lighttpd-1.4.33
RUN cd ../mod_websocket
RUN ./bootstrap
RUN ./configure --with-lighttpd=/usr/local/src/lighttpd1.4
RUN make install
RUN cd ../lighttpd1.4
RUN ./autogen.sh
RUN ./configure --with-websocket=all
RUN make
RUN make install
RUN mkdir /root/www -p

ADD websocket.conf /usr/local/src/lighttpd1.4/websocket.conf


CMD ["/usr/local/src/lighttpd1.4/lighttpd", "-D", "-f", "websocket.conf"]
