#!/bin/sh
#
# $Header: as_swinstall.sh 28-jan-2008.00:19:31 bvaradar Exp $
#
# as_swinstall.sh
#
# Copyright (c) 2007, Oracle. All rights reserved.  
#
#    NAME
#      as_swinstall.sh - <one-line expansion of the name>
#
#    DESCRIPTION
#      <short description of component this file declares/defines>
#
#    NOTES
#      <other useful comments, qualifications, etc.>
#
#    MODIFIED   (MM/DD/YY)
#    bvaradar    04/12/07 - Creation
#

#Set default values
TRUE=1
FALSE=0
SH_SHELL="/bin/sh"
DEFAULT_SH_ORANAME="as11gHome"
DEFAULT_SH_ORABASE="$T_WORK/as11g"
DEFAULT_SH_ADDITIONALINST=$FALSE
SH_INITTSC="initializerdata.tsc"
SH_INVNAME="oraInventory"
SH_INSTNAME="runInstaller"
SH_RSPNAME="asop_swonlysilent.rsp"
SH_ORAINST="asop_orainst.loc"
SHIPHOME=""
SHHOME_BASE=""

echo "Info: Args: $0 $*"

GROUP=$USER_GROUP
export GROUP

echo "GROUP = $GROUP"

echo;echo "Info: To run this install script for a shiphome 'X',Set SHIPHOME_LOC to path of 'X' before invoking";echo
#If user has not set the Ship Home Base location, use the default logic for 'latest - 1' daily shiphome.
if [ -z $SHIPHOME_LOC ]
then
   echo "Info: Using daily shiphome from default location"
   SHHOME_BASE=/net/stlinma7/vol/shiphomes_linux/releaseBuilder/linux/dailyShiphomes/ias/11.1.1.0.0/daily
   #Always take the last but one shiphome
   SHIPHOME=`ls -ldtr $SHHOME_BASE/* | tail -2 | head -1 | tr -s " " " " | cut -d " " -f9`
#  SHIPHOME="/net/stlinma7/vol/shiphomes_linux/releaseBuilder/linux/dailyShiphomes/ias/11.1.1.0.0/beta3/071024.1944"
#  SHIPHOME="/net/stlinma7/vol/shiphomes_linux/releaseBuilder/linux/dailyShiphomes/ias/11.1.1.0.0/daily/080124.1100"
   echo "Info: Using shiphome $SHIPHOME"
else
   echo "Info: Using shiphome from environment variable SHIPHOME_LOC"
   SHIPHOME=$SHIPHOME_LOC
fi
echo "Info: SHIPHOME = $SHIPHOME"

#User did not give Home name and/or location? Use default values.
SH_ORANAME=$1
: ${SH_ORANAME:="$DEFAULT_SH_ORANAME"}
SH_ORABASE=$2
: ${SH_ORABASE:="$DEFAULT_SH_ORABASE"}
SH_ADDITIONALINST=$3
: ${SH_ADDITIONALINST:="$DEFAULT_SH_ADDITIONALINST"}
SH_CENTINV=

if [ $SH_ADDITIONALINST -ne $FALSE ] 
then
    SH_ORANAME=${SH_ORANAME}${SH_ADDITIONALINST}    
    SH_CENTINV=$4
fi

if [ ! -d $SH_ORABASE ]
then
   echo "Info: Creating SH_ORABASE directory recursively."
   mkdir -p $SH_ORABASE
fi

echo "Info: T_WORK = $T_WORK"

SH_ORAHOME=$SH_ORABASE/$SH_ORANAME
if [  $SH_ADDITIONALINST -ne $FALSE ]
then
  #New home install into existing central inventory
  SH_ORACINV=$SH_CENTINV
else
  SH_ORACINV=$SH_ORABASE/$SH_INVNAME
fi

echo "Info: SH_ORANAME = $SH_ORANAME"
echo "Info: SH_ORAHOME = $SH_ORAHOME"
echo "Info: SH_ORABASE = $SH_ORABASE"
echo "Info: SH_ORACINV = $SH_ORACINV"
echo "Info: SH_CENTINV = $SH_CENTINV"
SH_RSPFILELOC="$SH_ORABASE/$SH_RSPNAME"
SH_ORAINSTLOC="$SH_ORABASE/$SH_ORAINST"
echo "Info: SH_RSPFILELOC = $SH_RSPFILELOC"
echo "Info: SH_ORAINSTLOC = $SH_ORAINSTLOC"
echo 

mkdir -p $SH_ORABASE >> $T_WORK/mkdir.log

#Create the sample response file
echo "Info: Creating the response file at $SH_RSPFILELOC"
echo [ENGINE] > $SH_RSPFILELOC
echo VERSION=1.0.0.0.0 >> $SH_RSPFILELOC
echo [GENERIC] >> $SH_RSPFILELOC
echo INSTALL AND CONFIGURE TYPE=false >> $SH_RSPFILELOC
echo INSTALL AND CONFIGURE LATER TYPE=true >> $SH_RSPFILELOC
echo CONFIGURE ONLY TYPE=false >> $SH_RSPFILELOC
echo ORACLE_HOME_NAME=$SH_ORANAME >> $SH_RSPFILELOC
echo ORACLE_HOME=$SH_ORABASE/$SH_ORANAME >> $SH_RSPFILELOC
echo BOOTSTRAP MAS AND EM EXPRESS=false >> $SH_RSPFILELOC
echo ADMINISTRATOR PASSWORD=welcome1 >> $SH_RSPFILELOC
echo ADMINISTRATOR PASSWORD CONFIRM=welcome1 >> $SH_RSPFILELOC
echo [SYSTEM] >> $SH_RSPFILELOC
echo [APPLICATIONS] >> $SH_RSPFILELOC
echo [RELATIONSHIPS] >> $SH_RSPFILELOC

#Create the oraInst.loc
if [  $SH_ADDITIONALINST -ne $FALSE ]
then
    	echo "Info: This home will be registered into central inventory at $SH_CENTINV"
	SH_ORAINSTLOC=$SH_CENTINV
else 
	echo; echo "Info: Creating the oraInst.loc at $SH_ORAINSTLOC"
	echo "Info: The inventory used is $SH_ORACINV"
	echo inventory_loc=$SH_ORACINV > $SH_ORAINSTLOC
	echo inst_group=$GROUP >> $SH_ORAINSTLOC
fi

#invoke the installer and wait till completion
echo; echo "Info: Invoking runInstaller to install software only install in silent mode"
echo
echo "Info: $SH_SHELL $SHIPHOME/Disk1/$SH_INSTNAME -s -response $SH_RSPFILELOC -invPtrLoc $SH_ORAINSTLOC -waitForCompletion"
echo
if [ $SH_ADDITIONALINST -eq $FALSE ] 
then
	echo "set ORACLE_HOME_NAME $SH_ORANAME" >> $T_WORK/$SH_INITTSC
	echo "set ORACLE_HOME $SH_ORABASE/$SH_ORANAME" >> $T_WORK/$SH_INITTSC
	echo "set ASCTL_DIR $ORACLE_HOME/bin" >> $T_WORK/$SH_INITTSC
	echo "set INVPTR1 $SH_ORAINSTLOC" >> $T_WORK/$SH_INITTSC
        echo "set CENTRALINV $SH_ORACINV" >> $T_WORK/$SH_INITTSC
	echo "set LOCALHOST `hostname`" >> $T_WORK/$SH_INITTSC
	echo "set USERNAME $USER" >> $T_WORK/$SH_INITTSC
	echo "set T_HOSTURL ^LOCALHOST^.us.oracle.com" >> $T_WORK/$SH_INITTSC
else
	echo "set ORACLE_HOME_NAME$SH_ADDITIONALINST $SH_ORANAME" >>  $T_WORK/$SH_INITTSC
	echo "set ORACLE_HOME$SH_ADDITIONALINST $SH_ORABASE/$SH_ORANAME" >> $T_WORK/$SH_INITTSC
        echo "set INVPTR$SH_ADDITIONALINST $SH_ORAINSTLOC" >> $T_WORK/$SH_INITTSC
        echo "set CENTRALINV$SH_ADDITIONALINST $SH_ORACINV" >> $T_WORK/$SH_INITTSC
        echo "set LOCALHOST$SH_ADDITIONALINST `hostname`" >> $T_WORK/$SH_INITTSC
        echo "set USERNAME$SH_ADDITIONALINST $USER" >> $T_WORK/$SH_INITTSC
        echo "set T_HOSTURL$SH_ADDITIONALINST ^LOCALHOST^.us.oracle.com" >> $T_WORK/$SH_INITTSC
fi
#exit 0
$SH_SHELL $SHIPHOME/Disk1/$SH_INSTNAME -s -response $SH_RSPFILELOC -invPtrLoc $SH_ORAINSTLOC -waitForCompletion
echo; echo "Info: Install done"
#Change the mode
echo "Info: Changing permissions to +rw"
chmod +wr -R $SH_ORABASE/$SH_ORANAME

echo "Info: $0: Script Done"

