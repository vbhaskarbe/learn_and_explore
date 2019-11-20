#!/bin/bash 
trap 'echo "VAR-TRACE> \$variable = \"$variable\""' DEBUG 
# Echoes the value of $variable after every command.
variable=29 
echo "Just initialized \"\$variable\" to $variable." 
let "variable *= 3" 
echo "Just multiplied \"\$variable\" by 3." 
exit 0

