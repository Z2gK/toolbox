#!/bin/sh

if [ $# = 0 ]; then
    echo "Encrypts a file using openssl and AES-256 in CBC mode"
    echo "Argument: <filename>"
    exit 
fi

openssl enc -aes-256-cbc -in $1 -out $1.enc
