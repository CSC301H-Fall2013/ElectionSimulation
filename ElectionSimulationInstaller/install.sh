#!/bin/bash

if test -z `which python`
then
    tar xvjf Python-2.7.5.tar.bz2
    cd Python-2.7.5
    ./configure
    make
    cd ..
fi

tar xzvf Django-1.5.4.tar.gz
cd Django-1.5.4
sudo python setup.py install