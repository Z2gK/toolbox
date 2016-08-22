#!/bin/sh
# requires openssl

if [ $# = 0 ]; then
    echo "Encodes a file into base64 using openssl"
    echo "Argument: <filename>"
    exit 
fi

if [ -e $1.b64 ]
then
    read -p "File exists. Overwrite (y/n)? " choice
    case $choice in
	y|Y) openssl enc -base64 -in $1 -out $1.b64;;
	* ) echo "Not overwriting"; exit;;
    esac

fi

openssl enc -base64 -in $1 -out $1.b64
