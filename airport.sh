#!/bin/bash

if [ "$1" == "off" ]; then
    /usr/sbin/networksetup -setairportpower en1 $1
    echo "AirPort WiFi turned $1"
    for (( i=3; i>0; i-- )); 
    do
        echo "Restart in $i"
        sleep 1
    done
    /usr/sbin/networksetup -setairportpower en1 on
    echo "AirPort Wifi turned on"
elif [ "$1" == "on" ]; then
    /usr/sbin/networksetup -setairportpower en1 $1
    echo "AirPort Wifi turned $1"
else
    echo "Usage: ./airport.sh [on/off]"
fi
