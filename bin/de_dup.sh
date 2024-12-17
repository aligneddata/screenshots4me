#!/bin/bash

# Purpose: remove duplicated jpg files
# Arguments:
#	a list of jpg files sorted by time sequence

action_on_duplicate () {
	if [ "$DUP_ACTION" == 'DEL' ]; then
		log_info "Removing file ${previous_file}"
		rm -f "${previous_file}"
	fi
}

compare_files() {
	# current_file, previous_file, current_file
	python diff_jpgs.py $DEDUP_THRESHOLD "${previous_file}" "${current_file}"
	diff=$?
	if [ "$diff" == '0' ]; then
		log_debug "About same, (DEDUP_THRESHOLD=$DEDUP_THRESHOLD): ${previous_file} == ${current_file}"
		action_on_duplicate "${previous_file}"
	else
		log_debug "Different, (DEDUP_THRESHOLD=$DEDUP_THRESHOLD): ${previous_file} == ${current_file}"
	fi
}


#
# main
#
source venv/bin/activate
source ~/bin/logger.sh

# remove files with differences equal or less than this threshold
if [ "$DEDUP_THRESHOLD" != '' ]; then
	DEDUP_THRESHOLD=$DEDUP_THRESHOLD
else
	DEDUP_THRESHOLD=10  
fi
DUP_ACTION=$DUP_ACTION  # DEL must be specified explictly
log_info "DEDUP_THRESHOLD=$DEDUP_THRESHOLD, DUP_ACTION=$DUP_ACTION "

previous_file=
for current_file in "$@"
do
	if [ "$previous_file" != '' ]; then
		log_debug "Comparing: $previous_file, $current_file"
	    compare_files "${previous_file}" "${current_file}"
	fi
    previous_file="${current_file}"
done