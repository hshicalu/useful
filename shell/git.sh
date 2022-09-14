#!/bin/sh

# Shell script for git push.
echo
git add $1
git commit -m "$2"
git push
