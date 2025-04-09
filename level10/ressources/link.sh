#!/bin/bash
while true
do
	touch /tmp/token
	rm -f /tmp/token
	ln -s /home/user/level10/token /tmp/token		
	rm -f /tmp/token
done