FROM ubuntu
MAINTAINER Tobias Lindener <tobias.lindener@gmail.com>

# Install the relevant packages
RUN apt-get update && apt-get install apache2 libapache2-mod-php5 php5-dev php-pear -y
RUN apt-get install apt-utils wget build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev -y
RUN mkdir -p /usr/local/src
RUN wget -O - http://mosquitto.org/files/source/mosquitto-1.3.tar.gz | tar -xvz -C /usr/local/src
RUN cd /usr/local/src/mosquitto-1.3; make; make install
RUN cp /usr/local/src/mosquitto-1.3/lib/libmosquitto.so.1 /lib/libmosquitto.so.1 
# Enable the php mod we just installed
RUN a2enmod php5
RUN echo "extension=mosquitto.so" >> /etc/php5/apache2/php.ini 
RUN pecl install Mosquitto-alpha
# Add our websites files to the default apache directory (/var/www)
ADD index.php /var/www/index.php

# Update our apache sites available with the config we created
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf

# expose port 80 so that our webserver can respond to requests.
EXPOSE 80

# Manually set the apache environment variables in order to get apache to work immediately.
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache
ENV APACHE_RUN_DIR /var/run/apache2

# Execute the apache daemon in the foreground so we can treat the container as an 
# executeable and it wont immediately return.
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
