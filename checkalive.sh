#!/bin/sh

if [ $# -ne 2 ]; then
    echo "Monitors the alive status of an address through pings"
    echo "Arguments: <IP Address> <Log filename>"
    exit 1
fi

IPAddr=$1
LOGFILENAME=$2

while true; do
    DATESTRING=`date`
    ping -w 2000 -c 1 $IPAddr > /dev/null
    if [ $? -eq 0 ]; then
	echo "$IPAddr is UP at $DATESTRING" >> $LOGFILENAME;
    else
	echo "$IPAddr is DOWN at $DATESTRING" >> $LOGFILENAME;
    fi
    sleep 69s
done
