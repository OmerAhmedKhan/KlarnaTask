#!/bin/bash

sudo apt install virtualenv
mkdir /home/virtual_env
cd /home/virtual_env/
virtualenv -p python3 klarna_test
. klarna_test/bin/activate
cd /home/KlarnaPythonTest/
python3 setup.py install
python3 api.py
