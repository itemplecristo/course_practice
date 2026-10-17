"""Module 06: Bash Scripting & Pipelines (Manual Practice / Scratchpad)
Run directly: python course_2_python_with_operating_system/modules/module_06_bash_scripting/practice_manually.py
"""

print("\n---> Module 06: Bash Scripting & Pipelines manual experiments\n")

# Basic Linux commands
print("\n---> Basic Linux commands\n")

"""

# The ls command
print("\n---> The ls command\n")

# List files and directories
# The ls command lists files and directories in the current directory.
# When used without options, ls lists only the names of files and directories in the current directory.

# The cat command
print("\n---> The cat command\n")

# The echo command
print("\n---> The echo command\n")

mkdir mynewdir
cd mynewdir/
/mynewdir$ pwd
/mynewdir$ cp ../spider.txt .
/mynewdir$ touch myfile.txt
/mynewdir$ ls -l
#Output:
#-rw-rw-r-- 1 user user   0 Mai 22 14:22 myfile.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt
/mynewdir$ ls -la
#Output:
#total 12
#drwxr-xr-x  2 user user  4096 Mai 22 14:17 .
#drwxr-xr-x 56 user user 12288 Mai 22 14:17 ..
#-rw-rw-r--  1 user user     0 Mai 22 14:22 myfile.txt
#-rw-rw-r--  1 user user   192 Mai 22 14:18 spider.txt
/mynewdir$ mv myfile.txt emptyfile.txt
/mynewdir$ cp spider.txt yetanotherfile.txt
/mynewdir$ ls -l
#Output:
#total 8
#-rw-rw-r-- 1 user user   0 Mai 22 14:22 emptyfile.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:23 yetanotherfile.txt
/mynewdir$ rm *
/mynewdir$ ls -l
#total 0
/mynewdir$ cd ..
rmdir mynewdir/
ls mynewdir
#ls: cannot access 'mynewdir': No such file or directory

"""

# Redirecting streams
print("\n--> Redirecting streams\n")

# Redirection is a process of sending a stream to a different destination.
# The w file mode used by the open function each time we perform of redirection of STD out, the destination is overwritten.

"""

cat stdout_example.py
#!/usr/bin/env python3
print("Don't mind me, just a bit of text here...")
./stdout_example.py
#Output: Don't mind me, just a bit of text here...
./stdout_example.py > new_file.txt
cat new_file.txt
#Output: Don't mind me, just a bit of text here...
./stdout_example.py >> new_file.txt
cat new_file.txt
#Output: Don't mind me, just a bit of text here...
 #Don't mind me, just a bit of text here...
cat streams_err.py
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")
./streams_err.py < new_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR
./streams_err.py < new_file.txt 2> error_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
cat error_file.txt
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR
echo "These are the contents of the file" > myamazingfile.txt
cat myamazingfile.txt
#These are the contents of the file

"""

# Pipes and pipelines
print("\n--> Pipes and pipelines\n")

# Pipes connect the output of one program to the input of another.

"""

ls -l | less
#(... A list of files appears...)
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
     # 7 the
     # 3 up
     # 3 spider
     # 3 and
     # 2 rain
     # 2 itsy
     # 2 climbed
     # 2 came
     # 2 bitsy
     # 1 waterspout.

     cat capitalize.py
#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip().capitalize())

    cat haiku.txt
#advance your career,
#automating with Python,
#it's so fun to learn.


cat haiku.txt | ./capitalize.py
#Advance your career,
#Automating with python,
#It's so fun to learn.

./capitalize.py < haiku.txt
#Advance your career,
#Automating with python,
#It's so fun to learn.

"""

# Signaling processes
print("\n--> Signaling processes\n")

# Signals are tokens delivered to running processes to indicate a desired action.

"""

ping www.example.com
#PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes

Press Control C:

--- www.example.com ping statistics ---

9 packets transmitted, 9 received, 0% packet loss, time 8013ms

rtt min/avg/max/mdev = 93.587/93.668/93.719/0.149 ms


ping www.example.com
#PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes


  Press Control Z: the program stops.

  fg
#ping www.example.com
#64 bytes from 2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946): icmp_seq=5 ttl=51 time=93.6 ms

Press Control C:

--- www.example.com ping statistics ---

9 packets transmitted, 9 received, 0% packet loss, time 8013ms

rtt min/avg/max/mdev = 93.587/93.668/93.719/0.149 ms

"""

# Creating Bash scripts
print("--> Creating Bash scripts\n")

"""

#!/bin/bash
echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "Finishing at: $(date)"

./gather-information.sh

#!/bin/bash

echo "Starting at: $(date)"; echo

echo "UPTIME"; uptime; echo

echo "FREE"; free; echo

echo "WHO"; who; echo

echo "Finishing at: $(date)"

./gather-information.sh

"""

# Using variables and globs
print("--> Using variables and globs\n")

"""

example=hello
echo $example

example = hello

Command ‘example’ not found, did you mean:

	Command ‘gexample’ from deb pvm-examples (3.4.6-2build1)

Try: sudo apt install <deb name>

#!/bin/bash

line="-------------------------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"

./gather-information.sh


echo *.py

When we write star dot py [*.py], the shell turns it into a list containing all filenames that end with py in the current directory. We can also put the star at the end of an expression to get a list of all files that start with a certain prefix.

Code output:

action_deprecation.py areas.py capitalize.py charfreq.py  check_deprecation.py health_checks.py hello.py mycheck.py seconds.py  stdout_example.py streams.py test.py validations.py

echo c*

c* allows us to get all the files in the current directory that start with c.

Code output:

capitalize.py charfreq.py check_localhost.sh

echo *

(... all the files ...)

echo ?????.py


The question mark symbol can be used to match exactly one character, instead of any amount of characters.We can repeat it as many times as we need. In this example, we can get the Python files with five characters in their name by using five question marks together.

Code output:

areas.py hello.py

"""

# Conditional execution in Bash
print("--> Conditional execution in Bash\n")

"""

cat check_localhost.sh


About this code
Here  we’ll start with the if  keyword, followed by the grep command. This is how we’ll check for success. At the end of the command, we have a semicolon [;], followed by the word then. After that comes the body of the conditional.

Code output:

#!/bin/bash

if grep "127\.0\.0\.1" /etc/hosts; then

	echo "Everything ok"

else

	echo "ERROR! 127.0.0.1 is not in /etc/hosts"

fi

./check_localhost.sh


  Code output:

127.0.0.1	localhost

Everything ok



if test -n "$PATH"; then echo "Your path is not empty"; fi

Code output:

Your path is not empty

1



if [ -n "$PATH" ]; then echo "Your path is not empty"; fi

Your path is not empty

"""

# While loops in Bash scripts
print("--> While loops in Bash scripts\n")

"""

n=1
while [ $n -le 5 ]; do
  echo "Iteration number $n"
  ((n+=1))
done

Iteration number 1
Iteration number 2
Iteration number 3
Iteration number 4
Iteration number 5


import sys
import random

value = random.randint(0, 3)
print("Returning: " + str(value))
sys.exit(value)

Code output:

Returning: 1


retry.sh:

#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;


./retry.sh ./random-exit.py

Returning: 1
Retry #1
Returning: 3
Retry #2
Returning: 1
Retry #3
Returning: 0

"""

# For loops in bash scripts
print("--> For loops in bash scripts\n")

"""

for item in /etc/*.conf
do
	echo "Processing $item"
done

About this code
In the example above, the for loop goes through each of the files in the /etc/ folder that has the .conf extension and prints a line. Let’s check the output:

Processing /etc/NetworkManager/NetworkManager.conf

Processing /etc/NetworkManager/dispatcher.d/10-unattended-upgrades

... and so on



for i in 1 2 3; do echo $i; done;
1
2
3




bash scripts can do way more complex stuff. But the basics, such as using variables, conditional execution, and loops, are the foundation of everything else. Let’s try to put some of these pieces together.


#!/bin/bash

for file in *.HTM; do
        name=$(basename "$file" .HTM)
        mv "$file" "$name.html"
done

#!/bin/bash

for file in *.HTM; do
        name=$(basename "$file" .HTM)
        echo mv "$file" "$name.html"
done


/old_website$ chmod +x rename.sh
/old_website$ ./rename.sh


/old_website$ ./rename.sh
/old_website$
/old_website$ ls -l


ls -l

About this code
ls -l is a command in Linux and Unix systems used to list the contents of a directory in a long format. This format provides detailed information about each file

Code output:

total 4

-rw-r--r-- 1 user user  0 May 24 10:19 about.html

-rw-r--r-- 1 user user  0 May 24 10:20 contact.html

-rw-r--r-- 1 user user  0 May 24 10:20 footer.html

-rw-r--r-- 1 user user  0 May 24 10:20 header.html

-rw-r--r-- 1 user user  0 May 24 10:19 index.html

-rwxr-xr-x 1 user user 90 May 24 10:40 rename.sh


"""


# Advanced Command Interaction
print("--> Advanced Command Interaction\n")

"""


exit 0


sys.exit(1)



This is a Python program that returns the value 0.


Code output:


This is a Python program that returns the value 0.



This is a Python program that returns the value 1

This is a Python program that returns the value 1



This is a Python program that returns 1

This is a Python program that returns 1

1





cat /etc/hosts

About this code
The /etc/hosts file is a system file that maps hostnames to IP addresses. It is used by the operating system to resolve hostnames to IP addresses.

Code output:

127.0.0.1	localhost
::1		localhost



cat /etc/hosts | grep localhost

127.0.0.1	localhost
::1		localhost



+++

tail /var/log/syslog

Code output:

May 24 10:17:01 ubuntu.local CRON[257236]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)

May 24 10:18:41 ubuntu.local rsyslogd: -- MARK --

May 24 10:25:19 ubuntu.local systemd[1]: Reloading.


tail /var/log/syslog | cut -d' ' -f5-


Code output:

CRON[257236]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)

rsyslogd: -- MARK --

systemd[1]: Reloading.


cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head


Code output:

     41 systemd[1]: Starting Network Manager Script Dispatcher Service...

     41 systemd[1]: Started Network Manager Script Dispatcher Service.

     41 systemd[1]: NetworkManager-dispatcher.service: Succeeded.

     41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: start running ordered scripts...

     41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: new request (1 scripts)

     41 dhclient[757]: DHCPREQUEST for 192.168.122.103 on ens3 to 192.168.122.1 port 67 (xid=0x3a5ff7ed)

     41 dhclient[757]: DHCPACK of 192.168.122.103 from 192.168.122.1 (xid=0xedf75f3a)

     41 dbus-daemon[592]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'

     41 dbus-daemon[592]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.15' (uid=0 pid=599 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")

      9 systemd[1]: Started Run anacron jobs.


#!/bin/bash

for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done




About this code
This script is written in the Bash scripting language and designed to analyze log files. It analyzes each log file in the /var/log directory and displays the top 5 most frequently occurring messages along with their counts.



./toploglines.sh


Code output:

(...)

Processing: /var/log/user.log

     23 system-updater[199481]: DEBUG Command exited with status: 0

     19 system-updater[46682]: DEBUG Command exited with status: 0

     16 system-updater[175060]: DEBUG Command exited with status: 0

     11 /usr/bin/lock: called by /bin/bash for . uid 0, euid 0.

     11 network-manager-dhclient-hooks: Dispatching run of '/etc/dhcp/dhclient-exit-hooks.d/hostname' ...

Processing: /var/log/Xorg.0.log

     87 Printing DDC gathered Modelines:

     87 Modeline "1920x1080"x0.0  141.00  1920 1936 1952 2104  1080 1083 1097 1116 -hsync -vsync (67.0 kHz eP)

     87 EDID vendor "AUO", prod id 5949

     78 vendor "AUO", prod id 5949

     78 DDC gathered Modelines:

"""
