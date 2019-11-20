#!/bin/bash
eval echo \$$#
echo ${!#}
echo "Parent PID = $$"
(
  echo "Iam subshell"
)&
echo "Subshells PID = $!"
echo "Parent PID again = $$"
