#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "Please run this script as root" 
   exit 1
fi

if [[ "$(python3 -V)" =~ "Python 3" ]]; then
 echo "Python 3 is installed"
fi