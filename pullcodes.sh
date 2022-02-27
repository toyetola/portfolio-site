#!/bin/sh
set -e

echo "copying codes ..."

# Update codebase
    git fetch origin master
    git reset --hard origin/master

echo "copying ended ..."