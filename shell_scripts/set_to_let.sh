

for i in `seq 46 87`
do
  echo "tvmhdi$i.tsc"
  #ade co -nc tvmhdi$i.tsc
#  sed -i 's/Unlet JAVA_HOME/Unset JAVA_HOME/g' tvmhdi$i.tsc
  #sed -i 's/Unlet ORACLE_CONFIG_HOME/Unset ORACLE_CONFIG_HOME/g' tvmhdi$i.tsc
  #sed -i 's/Unlet ORACLE_CCR_DEV/Unset ORACLE_CCR_DEV/g' tvmhdi$i.tsc
#  sed -i 's/Relet ORACLE_HOME/Reset ORACLE_HOME/g' tvmhdi$i.tsc
#  sed -i 's/Relet ORACLE_CCR_DEV/Reset ORACLE_CCR_DEV/g' tvmhdi$i.tsc
  sed -i 's/unlet ORACLE_CONFIG_HOME/unset ORACLE_CONFIG_HOME/g' tvmhdi$i.tsc
  sed -i 's/unlet ORACLE_CCR_DEV/unset ORACLE_CCR_DEV/g' tvmhdi$i.tsc
done
