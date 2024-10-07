#!/usr/bin/env bash

# This script installs the git hooks in the .git/hooks directory
# It is meant to be run from the root of the repository

# Get the current working directory
PWD=$(pwd)

# Pre-commit hook Does not exist
if [ -f .git/hooks/pre-commit ]; then
    echo "Git Pre-commit hook already exists"
    exit 1
fi

# Change to the .git/hooks directory
cd .git/hooks

# Create a symbolic link to the pre-commit script
ln -s ../../git_build_data.sh pre-commit

# Make the script executable
chmod +x pre-commit

# Change back to the original working directory
cd $PWD

# end of script