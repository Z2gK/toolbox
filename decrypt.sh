#!/bin/sh

if [ $# = 0 ]; then
    echo "Decrypts a file using openssl and AES-256 in CBC mode"
    echo "Argument: <filename>"
    exit 
fi

infile=$1
outfile=${infile%.enc}
if [ $infile = $outfile ]; then
    echo "Error: Input file should have .enc extension"
    exit
fi

openssl enc -aes-256-cbc -d -in $infile -out $outfile
