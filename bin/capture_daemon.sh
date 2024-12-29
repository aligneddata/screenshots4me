#!/bin/bash

if [ "$1" != '' ]; then
	delay=$1
else
	delay=10
fi
source venv/bin/activate

while true; do
	bash -x ./capture_once.sh
	sleep 10
done

