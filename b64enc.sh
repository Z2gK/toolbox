#!/bin/sh
# requires openssl

if [ $# = 0 ]; then
    echo "Encodes a file into base64 using openssl"
    echo "Argument: <filename>"
    exit 
fi

openssl enc -base64 -in $1 -out $1.b64
