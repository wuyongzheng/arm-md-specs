#!/bin/bash

if [ $# -ne 3 ] ; then
	echo Usage: bash $0 rmm-chaps.tsv DEN0137_1.0-rel0_rmm-arch_external.pdf rmm
	exit
fi

tsv="$1"
inpdf="$2"
prefix="$3"

START=""
END=""
NAME=""

declare -A NAME_SEEN
LAST_PAGE=0
IFS=$'\t\n'
for i in $(<$tsv) ; do
	if [ -z $START ] ; then
		START=$i
	elif [ -z $END ] ; then
		END=$i
	elif [ -z $NAME ] ; then
		NAME=$i
	fi

	if [ -z $NAME ] ; then
		continue
	fi

	# It's a comment
	if [[ "$START" == "#"* ]]; then
		START=""
		END=""
		NAME=""
		continue
	fi

	if [[ ${NAME_SEEN[$NAME]+_} ]]; then
		echo Warning: repeated chapter name $NAME
	fi
	NAME_SEEN[$NAME]=1

	if (( START > END )) ; then
		echo Warning: reversed start-end $START $END $NAME
	fi
	if [ $LAST_PAGE -ne 0 ] ; then
		if (( LAST_PAGE + 1 > START )) ; then
			echo Warning: overlapping page $START $NAME
		elif (( LAST_PAGE + 1 < START )) ; then
			echo Warning: missing page $((LAST_PAGE + 1))
		fi
	fi
	LAST_PAGE=$END

	mutool clean "$inpdf" "$prefix-$NAME.pdf" $START-$END
	docling --to md --image-export-mode placeholder "$prefix-$NAME.pdf"
	rm "$prefix-$NAME.pdf"

	START=""
	END=""
	NAME=""
done
