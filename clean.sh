#!/bin/bash
if [[ -d ".vscode-root" ]]
then 
    git rm -rf --cached .vscode-root
    rm -rf .vscode-root
else
    git rm -rf --cached "*Cache*"
    git rm -rf --cached logs
    git rm -rf --cached Dictionaries
    git rm -rf --cached databases
    git rm -rf --cached "Service Worker"
    git rm -rf --cached User
    git rm -rf --cached "*Storage*"
    git rm -rf --cached "*Cookies*"
    git rm -rf --cached "*Trust*"
    git rm --cached Preferences
    git rm -rf --cached "Network*"
    git rm -rf --cached Crashpad
fi

