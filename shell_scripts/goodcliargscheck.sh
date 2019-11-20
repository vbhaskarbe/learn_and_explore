
E_WRONGARGS=85 # Non-numerical argument (bad argument format).

case "$1" in
 "" ) lines=50;;
 *[!0-9]*) echo "Usage: `basename $0` file-to-cleanup"; exit $E_WRONGARGS;;
 * ) lines=$1;;
esac
