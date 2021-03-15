#!/bin/bash

CLASSOPTION="" 
OUTFILE="tutorial.pdf"

if [ $# -eq 0 ]; then
    echo "At least one arqument required"
    exit 1
fi

if [ $# -eq 1 ] || [ $2 = "tutorial" ]; then
   CLASSOPTION="" 
   OUTFILE="tutorial.pdf"
elif [ $2 = "handout" ]; then
   CLASSOPTION="handout,notes" 
   OUTFILE="handout.pdf"
else
    echo "Invalid parameters passed"
    exit 1
fi

cd $1 &&
pandoc main.md -t beamer -o $OUTFILE -V "classoption=$CLASSOPTION" && 
cd ..