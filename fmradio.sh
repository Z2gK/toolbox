#!/bin/sh
if [ $# -ne 1 ]; then
    echo "Usage: <freq in MHz>"
    echo "E.g. 92.4"
    exit
fi

FREQ=$1

rtl_fm -f "$FREQ"e6 -M wbfm -s 200000 -r 48000 - | aplay -r 48000 -f S16_LE


# See www.ibm.com/developerworks/library/l-job-terminating
# for info on terminating processes at a certain time


