#!/bin/bash
IFS=':'
read name pass uid gid comm home lshel<<EOF
$(grep nfsnobody /etc/passwd)
EOF
echo "$name $pass $uid $gid $comm $home $lshel"
: Reset it
IFS=' \t\n'
