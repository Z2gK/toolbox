#!/bin/sh
# increases the brightness and contrast
# Example usage: ~/bin/brightness-contrast20.sh /path-to-directory/frames/*

for FILE in $@; do
  convert $FILE -brightness-contrast 20x20 ./${FILE##/*/}
done
