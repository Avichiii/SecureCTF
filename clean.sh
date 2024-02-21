#!/bin/bash

sudo -l
if [[ $? -ne 1 ]]
then
    echo "you need sudo previlage"
    exit 1
fi

if [[ -d "~.vscode-root" ]]
then 
    sudo git rm -rf --cached .vscode-root
    sudo rm -rf ~.vscode-root
else
    removeList=("*Cache*" "logs" "*Dict*" "databases" "Service Worker" "User" "*Storage*" "*Cookies*" "*Trust*" "Preferences" "*Network*" "Crashpad" "*Transport*" machineid)
    for del in ${removeList[*]}
    do
        sudo git rm -rf --cached "$del"
        sudo rm -rf "$del"
    done
fi                                                                                                   


