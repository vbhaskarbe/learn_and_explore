#!/bin/bash

CURDIR=$PWD
DSTDIR="/scratch/bvaradar/view_storage/bvaradar_osp11106vu/osp/test/toio/toiou"
for tNo in `seq 112 127`
do
   tscFile=toiou${tNo}.tsc
    tscDir=toiou${tNo}/log
   echo "ade mkelem -nc $tscFile"
   echo "ade mkdir -p $tscDir"
   echo "cp $CURDIR/$tscFile $tscFile"
   for logFile in `ls $CURDIR/$tscDir`
   do
	echo "ade mkelem -nc $tscDir/$logFile"
        echo "cp $CURDIR/$tscDir/$logFile $tscDir/$logFile"
   done   
done

