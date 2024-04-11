#!/bin/bash
# Read commit message from the user
read -p "Enter commit message: " commit_msg

# Add all changes to the staging area
git add .

# Commit changes with the provided message
git commit -m "$commit_msg"

# Push changes to the remote repository
git push

