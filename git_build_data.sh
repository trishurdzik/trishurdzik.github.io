#!/bin/bash

#
# Purpose: create an html file with the current date and time and the current git ID version
#  

# setup variables
HOMEDIR=`pwd`

# Run the Generate Tags File script in the _posts_tags directory
cd _posts_tags
./_gen_post_tags_files.sh
cd $HOMEDIR

OUTPUT_FILE="git_build_data.html"
OUTPUT_DIRECTORY="_includes"

WRAP_START="<div class=\"git_build_data\">"
WRAP_END="</div>"

# create output directory if it does not exist
if [ ! -d ${OUTPUT_DIRECTORY} ]; then
    mkdir -p ${OUTPUT_DIRECTORY}
fi

# overwrite output file if it does exist with new file
touch ${OUTPUT_DIRECTORY}/${OUTPUT_FILE}

# open html div
echo ${WRAP_START} > ${OUTPUT_DIRECTORY}/${OUTPUT_FILE}

# append built by
BUILTBY=`whoami`
echo "<span>Built By: ${BUILTBY}</span> " >> ${OUTPUT_DIRECTORY}/${OUTPUT_FILE}

# append current date and time
date +%F\ %T >> ${OUTPUT_DIRECTORY}/${OUTPUT_FILE}

# append git ID version
git describe --all --long | cut -d "-" -f 3 >> ${OUTPUT_DIRECTORY}/${OUTPUT_FILE}
git rev-parse HEAD >> ${OUTPUT_DIRECTORY}/${OUTPUT_FILE}

# close html div
echo ${WRAP_END} >> ${OUTPUT_DIRECTORY}/${OUTPUT_FILE}

# add and commit changes to git
git add ${OUTPUT_DIRECTORY}/${OUTPUT_FILE}
# git commit -a -m "updated git_build_data.html"

# go back to starting directory
cd $HOMEDIR
