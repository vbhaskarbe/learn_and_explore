clear 
echo $PATH
echo ${PATH#*:}
echo {0..9}
echo {a..p}
echo {A..Z}

File=/etc/fstab
{
read line1
read line2
} < $File
echo "First line in $File is:"
echo "$line1"
echo
echo "Second line in $File is:"
echo "$line2"

var="-n"
echo $var
# Has the effect of "echo -n", and outputs nothing.
echo ~+ 
echo ~-

args=$#
lastarg=${!args}
echo $lastarg
lastarg=${!#}
echo $lastarg
let n_minus_one=$#-1
if [ $n_minus_one -eq -1 ];
then
	echo $0
else 
	shift $n_minus_one
	echo $1 
fi

: ${CLUSTER_NAME?}
