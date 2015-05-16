#!/bin/bash

# This script is written by kradalby (username: kradalby here at GitHub)

#Use this as a osx service.
# Edit for own needs.
# 
# Install:
# Open Automater.app
# Create Service
# Change to no input and add Run Shell Script
# Paste path to script ( make sure it is executable )
# Save and add a shortcut to it under System Preferences > Keyboard > Shortcuts

url=https://hakloev.no/sc/
filename=`date '+%Y%m%d%H%M%S'`.png
path=~/Pictures/Screenshots/
mkdir -p $path
screencapture -o -i $path$filename
scp $path$filename hakloev:/var/www/hakloev.no/screenshots/ > /dev/null
printf $url$filename | pbcopy
