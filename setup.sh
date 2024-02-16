#!/bin/bash

if [[ ! -d "/opt/SecureCTF"]]
then
    mkdir /opt/SecureCTF
    # cloning the repo
    git clone https://github.com/Avichiii/SecureCTF /opt/SecureCTF || exit 1
fi


cd /opt/SecureCTF || exit 1

# requirements
pip install -r requirements.txt || exit 1

# launch the application
python app.py

