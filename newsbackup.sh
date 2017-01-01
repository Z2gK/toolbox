#!/bin/sh

BACKUPDIR=/mnt/data/Documents/Kindle/News

for d in $HOME/Calibre\ Library/calibre/*
do
    ISSUE=${d##/*/}
    if [ ! -d "$BACKUPDIR/$ISSUE" ]; then
	echo $ISSUE does not exist
	echo Copying...
	cp -pr "$d" $BACKUPDIR/
    fi
done
