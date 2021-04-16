#!/bin/bash

function compile {
    echo "Compiling $1 $3"
    cd $1 &&
    pandoc main.md -t beamer -o $3 -V "classoption=$2" && 
    cd ..
}

if [ $# -eq 0 ]; then
    echo "At least one arqument required"
    exit 1
fi

if [ $# -eq 1 ]; then
   compile $1 "" "tutorial.pdf"
   compile $1 "handout,notes" "handout.pdf"
elif [ $2 = "tutorial" ]; then
   compile $1 "" "tutorial.pdf"
elif [ $2 = "handout" ]; then
   compile $1 "handout,notes" "handout.pdf"
else
    echo "Invalid parameters passed"
    exit 1
fi