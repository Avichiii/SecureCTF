#!/bin/bash

sudo -l
if [[ $? -ne 0 ]]
then
    echo "you need sudo previlage"
    exit 1
fi

if [[ -d "~.vscode-root" ]]
then 
    sudo git rm -rf --cached .vscode-root 2>/dev/null
    sudo rm -rf .vscode-root 2>/dev/null
else
    removeList=("*Cache*" "logs" "*Dict*" "languagepacks*" "databases" "Service*" "User" "*Storage*" "*Cookies*" "*Trust*" "Preferences" "*Network*" "Crashpad" "*Transport*" machineid)
    for del in ${removeList[*]}
    do
        sudo git rm -rf --cached "$del" 2>/dev/null
        sudo rm -rf "$del" 2>/dev/null
    done
fi                                                                                                   


