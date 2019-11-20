#!/bin/bash

[ $# -eq 2 ] || { echo "Error: Wrong arguments."; exit 1; }
SRCPATCH=$1
DUPCOUNT=$2
DSTPATCH=$SRCPATCH
for (( dCount = 0; dCount < DUPCOUNT; dCount++))
do 
  let "DSTPATCH = $DSTPATCH + 1"
  echo "DSTPATCH = $DSTPATCH"
  cp -r $SRCPATCH $DSTPATCH
  sed -i 's/'"$SRCPATCH"'/'"$DSTPATCH"'/g' $DSTPATCH/etc/config/inventory.xml
  for file in `find $DSTPATCH/files -type f 2>/dev/null`
  do
     newfile=`echo $file | sed 's/\(.*\)\.class/\1'$DSTPATCH'.class/'`
     mv $file $newfile
     echo "$file => $newfile"
     partfile=`basename $file`
     npartfile=`echo $partfile | sed 's/\(.*\)\.class/\1'$DSTPATCH'.class/'`      
     sed -i 's:'"$partfile"':'"$npartfile"':g' $DSTPATCH/etc/config/actions.xml
  done
done

