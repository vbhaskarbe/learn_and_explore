#!/bin/bash

shift
shift
if [ $# -ne 0 ]
then
    set $(echo "$*" | sed 's/=/:/g')
fi
echo "$*"
