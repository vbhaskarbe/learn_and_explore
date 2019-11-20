
for i in `seq 41 83`
do
  echo "tvmhdg$i.log"
#  sed -i '/.* was successfully created./{ N
#					 s/^\(.* was successfully created.\)\n[ ]*$/\1/
   sed -i '{ N
	  s/\(.*\)\(The OCM configuration response file .* was successfully created.\)/\1\n\2/

}' tvmhdg$i.log
done
