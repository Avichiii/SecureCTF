#!/bin/bash

if [[ -d "/opt/SecureCTF" ]]
then
    cp /opt/SecureCTF/setup.sh /opt || exit 1
    rm -r /opt/SecureCTF || exit 1
    chmod +x setup.sh || exit 1
    
    echo "Project is upto date!"
    
    ./setup.sh || exit 1
    rm /opt/setup.sh || exit 1
else
    echo "There is no Directory called /opt/SecureCTF"
    echo "run setup.sh to setup locally."
    exit 1
fi

    
