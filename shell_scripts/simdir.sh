#!/bin/bash

str=/a/b/c/d/filename.sh
dirName=${str##/.*}
echo "dirname = $dirName"
str=/a/b/c/d/filename.sh
dirName=${str%%/.*}
echo "dirname = $dirName"
