#!/bin/bash

# Target system OS : Ubuntu Server 13.04
# This installer will install python, Django framework , Apache HTTP server
# The server will be run on port 80

# Install prerequisites
# In case there is no python
if test -z `which python`
then
    if test -z `which gcc`
    then
        # In case there is no gcc
        sudo apt-get install gcc
    fi
    tar xvjf Python-2.7.5.tar.bz2
    cd Python-2.7.5
    ./configure
    make
    cd ..
fi

# Install Django
tar xzvf Django-1.5.4.tar.gz
cd Django-1.5.4
sudo python setup.py install

# Install apache2
if test -z `which apachectl`
then
    sudo apt-get install apache2 libapache2-mod-wsgi
fi

# Copy install webpage files
cp -r ./ElectionSimulation ${HOME}/ElectionSimulation

# Set configuration files
# store a back up of the default configuration
cat etc/apache2/sites-available/default > etc/apache2/sites-available/default_back_up

# write the configuration
# Replace all %HOME% with the real ${HOME} in the template file and write it all to the real file
sed -e "s|%HOME%|${HOME}|g" < ./ApacheConfig > etc/apache2/sites-available/default
sudo apachectl restart