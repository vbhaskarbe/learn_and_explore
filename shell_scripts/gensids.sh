#!/bin/bash

S1="SID=sent sid0"
S2="SID=bent sid1"
S3="SID=cent sid2"
S4="SID=dent sid3"
S5="SID=kent sid4"
S6="SID=ment sid5"
S7="SID=nfcent sid6"
S8="SID=pent sid7"
S9="SID=rent sid8"
S10="SID=tent sid9"
S11="SID=vent sid10"
S12="SID=went sid11"
S13="SID=yent sid12"
tscfile=toiir001.tsc

for tscfile in `ade lsco | grep .tsc`
#for tscfile in /scratch/bvaradar/view_storage/bvaradar_ospmainvu/osp/test/toi/toii/toiir/toiir001.tsc
do
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13
do 
sidvar=S$i
set -- ${!sidvar}
if grep $1 $tscfile >/dev/null
then
   sed -i '/tscinit/a\
import '$2'' $tscfile
   sed -i 's/'$1'/SID=^'$2'^/' $tscfile
fi
done
done
