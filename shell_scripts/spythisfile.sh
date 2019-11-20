#!/bin/sh

file="$1"
#/scratch/bvaradar/view_storage/bvaradar_oui11one/oracle/work/toii/toiir/toiir021/home/.patch_storage/102000_Jan_24_2006_05_43_46/files/lib/xml.jar/oracle/xml/jaxb/orajaxb.class
T=`ls -l $file | awk '{ print $8}'`
while [ true ]
do
  sleep 1
  #echo "$T => $nT" 
  nT=`ls -l $file | awk '{ print $8}'`
  if [ "$T" != "$nT" ]
  then
     echo "$nT => $file" 
     T=$nT
  fi
done

