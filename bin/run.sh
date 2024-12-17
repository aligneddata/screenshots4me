#!/bin/bash

source venv/bin/activate

ORI_DIR=$HOME/Desktop
SRC_DIR=files_in
DST_DIR=files_out

mv "$ORI_DIR"/Screen*png "$SRC_DIR"/
cd "$SRC_DIR"/
for a_file in Screen*png
do
	python ../appocrmac.py "$a_file" $DST_DIR/"$a_file".txt $DST_DIR/"$a_file".png $DST/"$a_file".json
	ret $?
	if [ "$ret" = "0" ]
	then
		mv "$a_file" $DST_DIR/
		echo "Done: $a_file"
	else
		echo "Error: $a_file"
	fi
	rm -f *png.png *json  # not very useful
done
cd -

