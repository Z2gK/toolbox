#!/bin/sh
# Starts to record stream from radio at specified frequency
# The recording will last for two hours and will be in pcm format
# This script can be activated by a cron job at a certain time

if [ $# -ne 2 ]; then
    echo "Usage: <freq in MHz> <recording duration> <output directory>"
    echo "E.g. 92.4 10m /output/directory"
    echo "<recording duration> should be in timeout format"
    exit
fi

# check that output directory exists

FREQ=$1
DURATION=$2
OUTPUTDIR=$3

# check that output directory exists
if [ ! -d $OUTPUTDIR ]; then
    echo "Output directory does not exist!"
    exit
fi

DATESTRING=`date +%Y%m%d`
OUTPUTFILENAME="$OUTPUTDIR"/rec"$DATESTRING".pcm

#rtl_fm -f "$FREQ"e6 -M wbfm -s 200000 -r 48000 $OUTPUTFILENAME &
#RTLPID=$!
# sleep 130m # sleep for 2 hours 10 mins - for a recording of that length
#sleep 20s  # sleep for 10 seconds
#kill -15 $RTLPID    # check if this signal is correct

timeout $DURATION rtl_fm -f "$FREQ"e6 -M wbfm -s 200000 -r 48000 $OUTPUTFILENAME

echo "recording done"

# For conversion to wav using ffmpeg
# Now encoding to wav
# echo "converting to wav"
# WAVEFILENAME=${OUTPUTFILENAME%.pcm}.wav
# ffmpeg -f s16le -ar 48k -ac 1 -i $OUTPUTFILENAME $WAVFILENAME
# rm $OUTPUTFILENAME

# Command to play
# aplay -r 48000 -f S16_LE <filename>


# crontab installation and configuration
# systemctl enable cronie
# VISUAL=emacs crontab -e
# Enter this crontab line
# min(0-59) hour(0-23) dayofmonth(1-31) month(1-12) dayofweek(0-6,sun-sat) command
# 55          20           *              *            5     $HOME/bin/recordradio.sh 98.0 130m <directory-to-save>
