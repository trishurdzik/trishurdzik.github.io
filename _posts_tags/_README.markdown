---
title: Readme
layout: none
exclude_search: true
---

## This script is now run by the git_build_data.sh script

Running the git_build_data.sh script will generate the _posts_tags markdown files for all the tags

## Generating the _posts_tags markdown files for all the tags

Run the script:

```bash
$ _gen_post_tags_files.sh 
```

This script will generate the markdown files for all the tags in the `_post_tags.txt` file. The script will create a markdown file for each tag in the `_posts_tags` directory.


## Bash Commands for generating tag files used in the script

Lowercase filenames and titles for tags. Spaces and hyphens replaced with underscores

```bash
cat _post_tags.txt | sort | awk '{print $3}' | while read line; do FILENAME=${line,,}; FILENAME=${FILENAME// /_}; FILENAME=${FILENAME//-/_}; echo -e "---\ntitle: ${line,,}\nlayout: tags\n---\n" > "${FILENAME}.md" ; done;
```

Lowercase filenames and titles for tags. Spaces removed from filenames

```bash
cat _post_tags.txt | sort | while read line; do FILENAME=${line,,}; FILENAME=${FILENAME// /_}; echo -e "---\ntitle: ${line,,}\nlayout: tags\n---\n" > "${FILENAME}.md" ; done;
```

Lowercase titles and spaces removed from filenames

```bash
$ cat _post_tags.txt | sort | while read line; do echo -e "---\ntitle: ${line,,}\nlayout: tags\n---\n" > "${line// /_}.md" ; done;
```
