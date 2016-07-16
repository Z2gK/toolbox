#!/bin/sh

if [ $# = 0 ]; then
    echo "Decodes a file in base64 using openssl"
    echo "Argument: <filename>"
    exit 
fi

infile=$1
outfile=${infile%.b64}
if [ $infile = $outfile ]; then
    echo "Error: Input file should have .b64 extension"
    exit
fi

openssl enc -base64 -d -in $infile -out $outfile
