#!/bin/bash

#defines positional argument variables
SEARCH_PATTERN=$1
OUTPUT=$2

OCCURANCES=$(grep -o $SEARCH_PATTERN /workspaces/ds2002-course/mywork/mobydick.txt | wc -w)

echo $OCCURANCES

echo "The search pattern $SEARCH_PATTERN was found $OCCURANCES time(s)" >> $OUTPUT








