"""Module 01: Introduction to Version Control (Manual Practice / Scratchpad)
Run directly: python course_3_git_and_github/modules/module_01_intro_to_version_control/practice_manually.py
"""

print("---> Module 01: Introduction to Version Control manual experiments")

# diff and patch
print("\n---> diff and patch\n")

# "diff -u" creates a unified diff
# "diff -N" treats missing files as empty
# "patch" applies the diff

"""

Using diff -u
You use the diff -u command to compare two files, line by line, and have the differing
lines compared side-by-side in the same output. For an example of what this looks like,
see below:

~$ cat menu1.txt
Menu1:

Apples
Bananas
Oranges
Pears

~$ cat menu2.txt
Menu:

Apples
Bananas
Grapes
Strawberries

~$ diff -u menu1.txt menu2.txt
--- menu1.txt   2019-12-16 18:46:13.794879924 +0900
+++ menu2.txt   2019-12-16 18:46:42.090995670 +0900
@@ -1,6 +1,6 @@
-Menu1:
+Menu:

 Apples
 Bananas
-Oranges
-Pears
+Grapes
+Strawberries


The patch command
The patch command is useful for applying file differences. See the example below,
which compares two files.
The comparison is saved as a .diff file, which is then patched to the original file!

~$ cat hello_world.txt
Hello World
~$ cat hello_world_long.txt
Hello World

It's a wonderful day!
~$ diff -u hello_world.txt hello_world_long.txt
--- hello_world.txt     2019-12-16 19:24:12.556102821 +0900
+++ hello_world_long.txt        2019-12-16 19:24:38.944207773 +0900
@@ -1 +1,3 @@
 Hello World
+
+It's a wonderful day!
~$ diff -u hello_world.txt hello_world_long.txt > hello_world.diff
~$ patch hello_world.txt < hello_world.diff
patching file hello_world.txt
~$ cat hello_world.txt
Hello World

It's a wonderful day!

"""

# Git & GitHub Terminal Commands Quick-Reference
print("\n--> Git & GitHub Terminal Commands Quick-Reference\n")

"""

```bash
# ==============================================================================
# 1. SETUP & CONFIGURATION
# ==============================================================================
# Set global identity (recorded on every commit)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default pull behavior to standard merge (avoids pull rebase warnings)
git config --global pull.rebase false

# Inspect all active configuration settings
git config --list

# ==============================================================================
# 2. STARTING A REPOSITORY
# ==============================================================================
# Initialize a new local Git repository in the current directory
git init

# Clone an existing remote repository from GitHub to your machine
git clone https://github.com/<username>/<repository-name>.git

# Connect a local repository to a new GitHub remote
git remote add origin https://github.com/<username>/<repository-name>.git

# Verify connected remote URLs (fetch and push)
git remote -v

# ==============================================================================
# 3. DAILY WORKING WORKFLOW (STAGE & COMMIT)
# ==============================================================================
# Check status of working directory and staged changes
git status

# Stage specific files for commit
git add <filename>

# Stage all modified and new files in the project
git add .

# View differences in unstaged files compared to last commit
git diff

# View differences that have been staged for the next commit
git diff --staged

# Commit staged snapshot with a descriptive message
git commit -m "Add descriptive commit message"

# Reference and automatically close a GitHub issue upon PR merge
git commit -m "Fix bug in calculation logic. Closes #14"

# ==============================================================================
# 4. BRANCHING & MERGING
# ==============================================================================
# List all local branches (* marks the active branch)
git branch

# Create a new branch
git branch <branch-name>

# Switch to an existing branch
git checkout <branch-name>
# (Or using modern switch syntax):
git switch <branch-name>

# Create and switch to a new branch in one step
git checkout -b <branch-name>
# (Or using modern switch syntax):
git switch -c <branch-name>

# Merge changes from another branch into your currently checked-out branch
git merge <branch-name>

# Delete a branch locally (safe check: only if merged)
git branch -d <branch-name>

# ==============================================================================
# 5. SYNCHRONIZING WITH GITHUB (REMOTES)
# ==============================================================================
# Download remote commits, branches, and tags without merging
git fetch origin

# Fetch and merge changes from the remote branch into your local branch
git pull origin <branch-name>

# Push your local commits to GitHub and set upstream tracking (first time)
git push -u origin <branch-name>

# Standard push once upstream branch tracking is set
git push

# Push all tags to GitHub
git push origin --tags

# ==============================================================================
# 6. HISTORY, INSPECTION & LOGS
# ==============================================================================
# View commit history
git log

# View visual graph of commits across all branches in a compact format
git log --graph --oneline --all

# Inspect details and diff of a specific commit
git show <commit_id>

# Display command execution log (useful for recovering lost commits)
git reflog

# ==============================================================================
# 7. CLEANUP, REBASING & UNDOING CHANGES
# ==============================================================================
# Discard unstaged modifications in a specific file (revert to last commit)
git restore <filename>

# Unstage a file while keeping its code changes in working directory
git restore --staged <filename>

# Start an interactive rebase for the last N commits (squash, fixup, reword)
git rebase -i HEAD~<number-of-commits>

# Create a new commit that reverts the changes of an earlier commit
git revert <commit_id>

# Force push local state to remote (overwrites remote; use caution)
git push --force-with-lease origin <branch-name>

# Temporarily shelve uncommitted working directory changes
git stash

# Restore shelved changes
git stash pop
'''

"""
