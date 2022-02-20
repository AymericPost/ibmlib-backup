#!/bin/bash

args=("$@")

for arg in ${args[@]}; do
	sleep 3
	head -c 300 /dev/urandom | tr -dc 'a-zA-Z0-9~!@#$%^&*_-' | fold -w 50 | head -n 1 > ~/$(echo $arg).FILE
done
