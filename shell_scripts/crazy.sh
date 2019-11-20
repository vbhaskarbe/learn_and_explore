#FS=,
#et -- $@
#cho -e "$1\n$2\n$3\n$4\n$5";

set -- ${1//,/}
shift
myvar="$@"
echo "$myvar"

wibble_list=( $1 )

function spangulate {
    while [ $# -gt 0 ] ; do
        wibble=$1
        echo "Current wibble is ${wibble}"
        shift
    done
}

echo "${wibble_list[@]}"
spangulate "${wibble_list[@]}"

# Run as 
#$ ./crazy.sh "spam,eggs,baked beans,ham"
#Current wibble is spam
#Current wibble is eggs
#Current wibble is baked beans
#Current wibble is ham
