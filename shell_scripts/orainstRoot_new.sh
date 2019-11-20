#!/bin/sh

#Usage: orainstRoot.sh [INVLOC=Inventory_Loc] [INVPTRLOC=Path_to_oraInst.loc] [GRP=group]
#Testcases covered
#===============

#1. orainstRoot.sh
#    INVLOC is set to Default directory 
#    Group is set to default group g900
   
#2. orainstRoot.sh GRP=dba
#    Error case: Only group is given. It should be used with INVLOC or INVPTRLOC

#3. orainstRoot.sh INVLOC=Invalid_Directory INVPTRLOC=Valid_oraInst.loc GRP=dba
#    Error case: INVLOC Directory does not exist

#4. orainstRoot.sh INVLOC=Valid_Directory INVPTRLOC=Valid_oraInst.loc GRP=dba
#    INVLOC takes precedence over INVPTRLOC.
#    Group will be changed to dba

#5. orainstRoot.sh INVPTRLOC=Valid_oraInst.loc GRP=dba
#    inventory_loc line is extracted from given orainst.loc
#    INVLOC is set accordingly.
#    Group will be set to dba


if [ -d "/etc" ]; then
   chmod 755 /etc;
fi

flag=0;
#Process each CL argument
for arg in "$@"
do
#Split them from var=value to $1 as var and $2 as value. 
#If it is not in var=value format default '*' case is triggered.
#If there are duplicate arguments, the one appearing latest in CL list will be used.
  IFS='='
  set -- $arg
   case $1 in
     INVLOC) INVLOC=$2;
               flag=1;
	;;
     INVPTRLOC) INVPTRLOC=$2;
               flag=1;
	;;
     GRP) GRP=$2;
	;;
   esac
done 

#check Only GRP was given?
if [ -n "$GRP" ];then
   if [ $flag -eq 0 ];then
        echo "Error: GRP Should be used with INVLOC or INVPTRLOC"      
        echo "Usage: $0 [INVLOC=Inventory_Loc] [INVPTRLOC=Path_to_oraInst.loc] [GRP=group]"
        echo "Inventory_loc directory must exist"
        echo "oraInst.loc should be valid"
        exit 1
   fi
fi

#if INVLOC is not null and exists
if [ -n "$INVLOC" ];then
    #If given INVLOC is not present then error out
    if [ ! -d $INVLOC ];then
         echo "Error: Given INVLOC directory $INVLOC does not exist";
         exit 1
    fi
    echo "Inventory location is $INVLOC"
#if INVPTRLOC is not null and exists
elif [ -n "$INVPTRLOC" ]; then
    if [ -f $INVPTRLOC ];then
        #Extract inventory_loc=<PATH_TO_INVENTORY>
        invloc_line=`grep '^inventory_loc' $INVPTRLOC`
        #Uncommented inventory_loc line not present? error out.
        if [ $? -ne 0 ];then
           echo "Error: No valid inventory_loc line present in $INVPTRLOC"
           exit 1
        else        
           set -- $invloc_line
           INVLOC=$2          
        fi        
        #Extract inst_group=g900
        inst_group_line=`grep '^inst_group' $INVPTRLOC`
        if [ $? -eq 0 ];then
           set -- $inst_group_line       
           GRP=$2
        fi     
     fi
else 
    #Default behavior
    if [ -f "/scratch/sumsanka/oraInventory7/oraInst.loc" ]; then
	cp /scratch/sumsanka/oraInventory7/oraInst.loc /etc/oraInst.loc;
    else
	INVPTR=/etc/oraInst.loc
	INVLOC=/scratch/sumsanka/oraInventory7
	GRP=g900
	PTRDIR="`dirname $INVPTR`";
	# Create the software inventory location pointer file
	if [ ! -d "$PTRDIR" ]; then
		 mkdir -p $PTRDIR;
	fi
	echo "Creating the Oracle inventory pointer file ($INVPTR)";
	echo    inventory_loc=$INVLOC > $INVPTR
	echo    inst_group=$GRP >> $INVPTR
	chmod 644 $INVPTR
	# Create the inventory directory if it doesn't exist
	if [ ! -d "$INVLOC" ];then
		 echo "Creating the Oracle inventory directory ($INVLOC)";
 	    	 mkdir -p $INVLOC;
	fi
    fi
fi

#If INVLOC is not null and exists
if [ -n "$INVLOC" ];then
     echo "Changing permissions of $INVLOC to 770.";
     chmod -R g+rw,o-rwx $INVLOC;
else
     echo "Changing permissions of /scratch/sumsanka/oraInventory7 to 770.";
     chmod -R g+rw,o-rwx /scratch/sumsanka/oraInventory7;
fi

if [ $? != 0 ]; then
        if [ -n "$INVLOC" ]; then
            echo "OUI-35086:WARNING: chmod of $INVLOC to 770 failed!";
        else
	    echo "OUI-35086:WARNING: chmod of /scratch/sumsanka/oraInventory7 to 770 failed!";
	fi
fi

#check If flag was set?
if [ $flag -eq 1 ]; then
  #If GRP is not null and exists
  if [ -n "$GRP" ]; then
      echo "Changing groupname of $INVLOC to $GRP.";
      chgrp -R $GRP $INVLOC;
      if [ $? != 0 ]; then
        echo "OUI-10057:WARNING: chgrp of $INVLOC to $GRP failed!";
      fi
  fi 
else 
  #This should be default group 
  echo "Changing groupname of /scratch/sumsanka/oraInventory7 to g900.";
  chgrp -R g900 /scratch/sumsanka/oraInventory7;
  if [ $? != 0 ]; then
   echo "OUI-10057:WARNING: chgrp of /scratch/sumsanka/oraInventory7 to g900 failed!";
  fi
fi

#Finally we are done. ;-)
echo "The execution of the script is complete"
