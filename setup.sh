#!/bin/bash

# cloning the repo
git clone https://github.com/Avichiii/SecureCTF /opt/SecureCTF

cd /opt/SecureCTF

# requirements
pip install -r requirements.txt

# launch the application
python app.py

