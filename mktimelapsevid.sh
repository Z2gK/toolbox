#!/bin/sh
# Make a time lapse video using properly sequenced list of jpeg files in list.txt
# Output video in timelapse.avi

#mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o timelapse.avi -mf type=jpeg:fps=24 mf://@list.txt

#mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=4/3:vbitrate=8000000 -vf scale=1024:768 -o timelapse.avi -mf type=jpeg:fps=20 mf://@list.txt

# Unusual flipping around
mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=4/3:vbitrate=8000000 -vf scale=640:480 -o timelapse.avi -mf type=jpeg:fps=5 mf://@list.txt
