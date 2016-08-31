#!/bin/sh
# Starts to record stream from radio at specified frequency
# The recording will last for two hours and will be in pcm format
# This script can be activated by a cron job at a certain time

if [ $# -ne 2 ]; then
    echo "Usage: <freq in MHz> <output directory>"
    echo "E.g. 92.4 /output/directory"
    exit
fi

# check that output directory exists

FREQ=$1
OUTPUTDIR=$2

# check that output directory exists
if [ ! -d $OUTPUTDIR ]; then
    echo "Output directory does not exist!"
    exit
fi

DATESTRING=`date +%Y%m%d`
OUTPUTFILENAME="$OUTPUTDIR"/rec"$DATESTRING".pcm

rtl_fm -f "$FREQ"e6 -M wbfm -s 200000 -r 48000 $OUTPUTFILENAME &
RTLPID=#!

# sleep 130m # sleep for 2 hours 10 mins - for a recording of that length
sleep 10s  # sleep for 10 seconds
kill -s SIGTERM $RTLPID    # check if this signal is correct
echo "recording done"

# aplay -r 48000 -f S16_LE
