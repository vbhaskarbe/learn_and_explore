#!/bin/bash
FILETYPE=".dml"
OUTTAG="outbound_"
# If no argument is given assume current dir
if [ $# -ne 1 ]
then
   srcDir="."
else 
   srcDir="$1"
fi
echo "Info: srcDir = $srcDir"
# check if the directory is readable
if [ ! -r $srcDir ]
then
   echo "ERROR: The directory $srcDir is not readable"
   exit 1
fi
# Get all the files with extension $FILETYPE
find "$srcDir" -name "*$FILETYPE" -print > .allfiles$$
# Loop through each file in the list
while read origname
do  
   # Separate filename from dirpath do attach outbound to filename
   basname=`basename $origname`
   dirloc=`dirname $origname`
   newfile="${dirloc}/${OUTTAG}${basname}"
   # loop through each line
   while read line    
   do
       # Check if it is a decimal line? If decimal line then get the value to decrement.
       value=`echo "$line" | sed 's/\(.*dec.*(\)\(.*\)\().*\)$/\2/'`
       if [ "X$line" = "X$value" ]  
       then
           # Non-decimal line just echo it to new file
	   # echo "$line" >> $newfile
	   echo "$line"
       else 
	   # Got Decimal line, do the conversion.
	   value=`expr $value - 1`
           #set -xv            
	   modline=`echo \"$line\" | sed 's/\(.*dec.*(\)\(.*\)\().*\) \(.*\)$/\1'"$value"'\3 outbound_\4/'`		
	   newline=`echo '$line' | sed 's/\(.*dec.*(\)\(.*\)\().*\) \(.*\);\(.*\)$/string(1) \4_sign;\5/'`
           set +xv
      	   echo $modline
	   echo $newline	   
	   # echo $modline >> $newfile
	   # echo $newline >> $newfile	   
       fi
   done < $origname    
   echo "Info: $origname converted to $newfile"
exit
done < .allfiles$$

# Cleranup
rm .allfiles$$
