
for i in `seq 79 87`
#for i in `seq 56 59`
do
  sed 's/^#[ \t]*/# /g' tvmhdi$i.tsc | sed -n '8,14p'
done
