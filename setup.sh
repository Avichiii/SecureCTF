#!/bin/bash

# cloning the repo
git clone https://github.com/Avichiii/SecureCTF /opt/SecureCTF || exit 1

cd /opt/SecureCTF || exit 1

# requirements
pip install -r requirements.txt || exit 1

# launch the application
python app.py

