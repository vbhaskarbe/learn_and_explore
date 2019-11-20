#!/bin/bash
while IFS=: read user passwd uid gid comm hdir lshell
do
   if [ X"$user" = "Xnfsnobody" ]
   then
      echo "$user $passwd $uid $gid"
      exit 0
   fi
done < /etc/passwd
