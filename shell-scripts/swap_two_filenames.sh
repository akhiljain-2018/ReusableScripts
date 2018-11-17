
#!/bin/sh
# Simple scripts to switch one file with another one.
# Author: Akhil Jain

#TODO: 
#1. Check if two arguments are passed
#2. Check if the both files exist.

tmp=`mktemp`
mv $1 $tmp
mv $2 $1
mv $tmp $2