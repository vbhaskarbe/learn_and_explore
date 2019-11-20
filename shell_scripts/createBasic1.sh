#!/bin/sh
#
# $Header: createBasic1.sh 17-dec-2007.04:56:24 spatra Exp $
#
# createBasic1.sh
#
# Copyright (c) 2006, 2007, Oracle. All rights reserved.  
#
#    NAME
#      createBasic1.sh - Creates MAS instance, creates one oc4j one ohs and routing relations, starts the farm and components
#
#    DESCRIPTION
#      <short description of component this file declares/defines>
#
#    NOTES
#      <other useful comments, qualifications, etc.>
#
#    MODIFIED   (MM/DD/YY)
#    spatra      12/17/07 - Added creation of oc4j_admin
#    spatra      06/25/07 - fix for script 
#    shpandey    06/17/07 - creating instance oc4j and app for deinstall
#    sjnaik      03/07/07 - 
#    spatra      02/21/07 - Adding header.
#    spatra      02/19/07 - Creation
#
oracle_home=$1
instance_home=$2
instance_name=$3
farm_name=$4
instance_delete_home=$5
instance_delete_name=$6

echo $oracle_home=$1
echo $instance_home
echo $instance_name
echo $farm_name
echo $instance_delete_home
echo $instance_delete_name

HOSTNAME=`hostname`
DOMAINNAME=`domainname`
HOST=$HOSTNAME.$DOMAINNAME

export ORACLE_HOME=$oracle_home
export PATH=$oracle_home/jdk/bin:$PATH
export JAVA_HOME=$oracle_home/jdk
###################################SET OC4J PASSWORD###################################

#not needed anymore
#java -cp $ORACLE_HOME/j2ee/home/jazn.jar:$ORACLE_HOME/j2ee/home/jazncore.jar oracle.security.jazn.util.JAZNInstallHelper -oh $ORACLE_HOME -realm jazn.com -user oc4jadmin  -oldpwd welcome  -newpwd welcome1 -clearpwd true

###################################CREATE FARM###################################

echo "createMASInstance(name=\"$instance_name\", farm=\"$farm_name\", oi=\"$instance_home\")" > /tmp/test.script

####################################START FARM###################################

echo "startInstance(oi=\"$instance_home\")" >> /tmp/test.script

####################################CREATE OHS###################################
echo "connect(\"admin\")" >> /tmp/test.script
echo "cd (\"$instance_name\")" >> /tmp/test.script
#echo "startTxn()" >> /tmp/test.script
echo "createComponent(type=\"OHSComponent\", name=\"ohs1\")" >> /tmp/test.script
#echo "commitTxn()" >> /tmp/test.script
echo "cd (\"..\")" >> /tmp/test.script

####################################CREATE OC4J###################################

echo "cd (\"$instance_name\")" >> /tmp/test.script
#echo "startTxn()" >> /tmp/test.script
echo "createComponent(type=\"OC4JComponent\", name=\"oc4j1\")" >> /tmp/test.script
#echo "commitTxn()" >> /tmp/test.script

####################################CREATE OC4J_Admin###################################

echo "createComponent(type=\"OC4JComponent\", name=\"oc4j_admin\")" >> /tmp/test.script
#echo "commitTxn()" >> /tmp/test.script


####################################CREATE RELATIONSHIP###################################

#echo "createRelationship(name=\"relation1\", type=\"routing\",uTopoNode=\"oc4j1\", pTopoNode=\"ohs1\")" >> /tmp/test.script

####################################START OHS####################################

echo "cd (\"ohs1\")" >> /tmp/test.script
echo "start()" >> /tmp/test.script
echo "listPorts()" >> /tmp/test.script
echo "cd (\"..\")" >> /tmp/test.script

####################################START OC4J####################################

echo "cd (\"oc4j1\")" >> /tmp/test.script
echo "start()" >> /tmp/test.script
echo "listPorts()" >> /tmp/test.script
echo "cd (\"..\")" >> /tmp/test.script

####################################START OC4J_Admin####################################

echo "cd (\"oc4j_admin\")" >> /tmp/test.script
echo "start()" >> /tmp/test.script
echo "listPorts()" >> /tmp/test.script
echo "cd (\"../..\")" >> /tmp/test.script
echo "exit()" >> /tmp/test.script
###################################CREATE INSTANCE FOR DELETION###################################

echo "connect(\"admin\")" >> /tmp/test.script
echo "createInstance(name=\"$instance_delete_name\", oi=\"$instance_delete_home\")" >> /tmp/test.script

####################################START INSTANCE FOR DELETION###################################

echo "startInstance(oi=\"$instance_delete_home\")" >> /tmp/test.script

####################################CREATE OC4J_delete###################################

#echo "cd (\"..\")" >> /tmp/test.script
echo "cd (\"$instance_delete_name\")" >> /tmp/test.script
#echo "startTxn()" >> /tmp/test.script
echo "createComponent(type=\"OC4JComponent\", name=\"oc4j_delete\")" >> /tmp/test.script
#echo "commitTxn()" >> /tmp/test.script

####################################START OC4J_delete####################################

echo "cd (\"oc4j_delete\")" >> /tmp/test.script
echo "start()" >> /tmp/test.script
echo "listPorts()" >> /tmp/test.script



####################################START APP DEPLOY####################################
echo "deployApp(deployurl=\"deployer:mas:$HOST:9999\",deployuser=\"admin\",deploypassword=\"welcome1\", applicationname=\"webapp\",deployfile=\"$ADE_VIEW_ROOT/asinst/src/test/env_setup/webapp.ear\",bindAllWebApps=\"http-web-site\")" >> /tmp/test.script
echo "exit()" >> /tmp/test.script






####################################RUN SCRIPT####################################

$ORACLE_HOME/bin/asctl script /tmp/test.script
