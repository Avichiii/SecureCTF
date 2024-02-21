#!/bin/bash
if [[ -d "~.vscode-root" ]]
then 
    git rm -rf --cached .vscode-root
    rm -rf ~.vscode-root
else
    removeList=("*Cache*" logs Dictionaries databases "Service Worker" User "*Storage*" "*Cookies*" "*Trust*" Preferences "Network*" Crashpad)
    for del in ${removeList[*]}
    do
        git rm -rf --cached $del
        rm -rm $del
    done
fi

