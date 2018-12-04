#!/bin/bash


HEXSTRING=$1
PRINTFSTRING=""
for i in $HEXSTRING; do
    #echo $i
    SPECIAL='\x'
    #echo $SPECIAL
    PRINTFSTRING=${PRINTFSTRING}${SPECIAL}$i
done

# echo -n $PRINTFSTRING
printf $PRINTFSTRING | cat