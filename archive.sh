#!/bin/bash

EXERCISEPATH="Documents"
NOTEBOOKPATH="lab/practicelabs"

TIMESTAMP=$(date +"%Y%m%d_%H%M")

ARCHIVENAME="practicelabs_$TIMESTAMP.tar.gz"

cd $HOME
tar czf $ARCHIVENAME $EXERCISEPATH $NOTEBOOKPATH
cd -
