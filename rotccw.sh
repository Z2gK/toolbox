#!/bin/sh
# Rotates list of files in argument and outputs them in the current directory, with the same filename
# Example usage: ~/bin/rotccw.sh /mnt/data600GB/Documents/Timelapse/noon/frames/*

for FILE in $@; do
  convert $FILE -rotate -90 ./${FILE##/*/}
done
