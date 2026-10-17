"""Module 04: Managing Data & Processes (Manual Practice / Scratchpad)
Run directly: python course_2_python_with_operating_system/modules/module_04_managing_data_and_processes/practice_manually.py
"""

"""

Most operating systems supply three different I/O streams by default
each with a different purpose.

When we use the input function to accept user input
in a Python script we're using the STDIN stream.

The standard output stream or STDOUT is a pathway between a program
and a target of output, like a display.

The standard error stream or STDERR is a stream for error messages and
diagnostic output.

"""

print("\n--> Module 04: Managing Data & Processes manual experiments\n")

# Seconds converter with input() function
print("\n--> Seconds converter with input() function\n")

"""
# Temporary silent bundle

name = input("Please enter your name: ")
print("Hello, " + name)

Activate a script using command line: ./hello.py

Answer of the script: Please enter your name: Roger
Output: Hello, Roger


def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue] ")

print("Goodbye!")

"""

# Streams
print("\n--> Streams\n")

"""

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)

./streams.py
This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks!

cat greeting.txt
Well hello there, STDOUT

cat greeting.txt
Well hello there, STDOUT

ls -z

"""

# Environment Variables
print("\n--> Environment Variables\n")

"""

echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cat variables.py
#!/usr/bin/env python3
import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

./variables.py 
export FRUIT=Pineapple
./variables.py 

"""

# Command-Line Arguments and Exit Status
print("\n--> Command-Line Arguments and Exit Status\n")

"""

Another common way of providing information to our programs is
through command line arguments.

In all Unix-like operating systems, the exit status of the process
is zero when the process succeeds and different than zero if it fails.

The actual number returned gives additional info on what kind of error
the program encountered.

cat parameters.py
#!/usr/bin/env python3
import sys
print(sys.argv)

./parameters.py
['./parameters.py']

./parameters.py one two three
['./parameters.py', 'one', 'two', 'three']


wc variables.py
7 19 174 variables.py
echo $?
0

wc notpresent.sh
wc: notpresent.sh: No such file or directory
echo $?
1

This script receives a file name as a command line argument.
It first checks whether the file name exists or not.
When the file doesn't exist, it creates it by writing a line to it.
When the file exists, our script print an error message and exits
with an exit value of one.

#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

./create_file.py example
echo $?
0

cat example
New file created
./create_file.py example
Error, the file example already exists!
echo $?
1

"""

# Running system commands in Python
print("\n--> Running system commands in Python  \n")

"""

import subprocess
subprocess.run(["date"])
subprocess.run(["sleep", "2"])
result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)

# import subprocess

p1 = subprocess.run(["date"]) # By default the Popen object is returned and it waits for the external command to complete
p2 = subprocess.run(["echo", "Hello from the OS!"],
    capture_output=True)

print("Return Code: ", p1.returncode)
print("STDOUT: ", p2.stdout.decode())

# You can use the same command that you use in the terminal
# and it will produce the same output
# The command is executed as an external program

# The input= argument can be used to pass input to the program:
p3 = subprocess.run(["wc", "-l"], input=b"line 1\nline 2")
print("Line count: ", p3.stdout.decode()) # The count is 2

# We can capture the standard output, standard error and return code:
p4 = subprocess.run(["ls", "-l"], capture_output=True)
print("STDOUT: ", p4.stdout.decode())

# The same for the error stream
p5 = subprocess.run(["ls", "nonexistent_file"], capture_output=True)
print("STDERR: ", p5.stderr.decode())
print("Return Code: ", p5.returncode)

# We can create a new Python program that wraps a system command
# but we need to make sure that it has the necessary permissions and location

"""

# Obtaining the output of a system command
print("\n--> Obtaining the output of a system command\n")

"""

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())

import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)

"""

# Advanced subprocess management
print("\n--> Advanced subprocess management\n")

"""

import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)

"""

"""

Subprocess is a powerful module that allows you to do anything you could in Python
from within the shell, then get information back into Python.
You’ll probably want to stick with OS for basic file and directory
operations or Pathlib for working extensively with file paths.
But when you interface with external processes, run complex shell commands,
or need precise control over input and output, the subprocess module is the way to go.

"""

# Filtering log files with regular expressions
print("\nFiltering log files with regular expressions\n")

"""

#!/bin/env/python3

import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    print(line.strip())



#!/bin/env/python3

import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    print(line.strip())



import re
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])



#!/bin/env/python3

import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((.+)\)$"
    result = re.search(pattern, line)
    print(result[1])


chmod +x check_cron.py
./check_cron.py syslog

"""

# Parsing the syslog
print("\nParsing the syslog\n")

import re
def show_time_of_pid(line):
  pattern = r"^([a-zA-Z]+\s+\d+\s+[\d:]+).*\[(\d+)\]"
  result = re.search(pattern, line)
  return "{} pid:{}".format(result[1], result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440


# Making sense out of the data
print("\nMaking sense out of the data\n")

usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) + 1
print(usernames)
usernames[name] = usernames.get(name, 0) + 1
print(usernames)

"""

#!/bin/env/python3

import re
import sys

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)

    if result is None:
      continue
    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1

print(usernames)


./check_cron.py syslog

"""

# Parse the error log
print("\nParse the error log\n")

"""

error_counts = {}

# Example log processing loop:
for error in log_errors:
    error_counts[error] = error_counts.get(error, 0) + 1

# Result: {'CRON ERROR': 4, 'TIMEOUT': 2, 'CONNECTION REFUSED': 1}

"""
