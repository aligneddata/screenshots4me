#!/bin/bash

capture () {
	screen_id=$1
	screencapture -t jpg -D${screen_id} -x ~/tmp/scn${screen_id}_$vardate.jpg	
}

if [ "$1" == '' ]; then
	screen_list=1
else
	screen_list="$@"
fi

vardate=$(date '+%Y-%m-%d_%H.%M.%S')
echo $vardate
for screen_id in $screen_list; do
	capture "$screen_id"
done

