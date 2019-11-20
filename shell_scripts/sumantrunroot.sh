#!/bin/sh

#Backup CL arguments
cliArgs="$@"
#Process each CL argument
for arg in "$@"
do
   #Split them from -var=value to $1 as -var and $2 as value. 
   #If it is not in -var=value format default '*' case is triggered.
   #If there are duplicate arguments, the one appearing latest in CL list will be used.
   IFS='='
   set -- $arg
   case $1 in
     invPtrLoc|INVPTRLOC|invptrloc) INVPTRLOC=$2;;
     invLoc|INVLOC|invloc) INVLOC=$2;;
     GRP|grp) GRP=$2;;
#     *) echo "This case is not expected => $1";;      
     *) ;;      
   esac
done 
#Restore CL arguments
set -- $cliArgs

#Show what we got! ;-)
echo "INVPTRLOC = $INVPTRLOC"
echo "INVLOC = $INVLOC"
echo "GRP    = $GRP"

