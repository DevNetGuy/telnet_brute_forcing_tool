#!/bin/sh 
HOST="192.168.1.1"
USER="one"
PASSWD="one
"
CMD1="logout"
CMD="?"
( echo open "$HOST"
sleep 2
 echo "$USER"
sleep 2
echo "$PASSWD"
sleep 2
echo "$CMD"
sleep 2
echo "$CMD1"
sleep 2
) | telnet 