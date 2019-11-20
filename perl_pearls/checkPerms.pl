#!/usr/loca/bin/perl 

($dev,$ino,$mode,$nlink,$uid,$gid,$rdev,$size,$atime,$mtime,$ctime,$blksize,$blocks) = stat ($ARGV[0]);
print "\n mode = $mode\n";

$mode = (stat($ARGV[0]))[2];
printf "Permissions are %04o\n", $mode & 07777;
