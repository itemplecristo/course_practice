"""Module 03: Regular Expressions (Manual Practice / Scratchpad)
Run directly: python course_2_python_with_operating_system/modules/module_03_regular_expressions/practice_manually.py
"""

print("\n---[ Module 03: Regular Expressions manual experiments ]---\n")

# Why use regular expressions?
# Regular expressions allow us to search for patterns in strings.

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

# String index() method are not effective because they are not flexible
# They rely on specific characters which may not always be present.

print("\n--> Using string index():\n")

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])

# Regular expressions are more flexible and can be used to search for patterns in strings.
print("\n--> Using regular expressions:\n")

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# Here the re module is used which lets us use the search function
# to find regular expressions inside strings.
# Then, a regular expression is defined as
# r""\[(\d+)\]"" which means we are looking for a pattern that starts with "[",
# then one or more digits "\d+",
# then a closing square bracket "]"

r"\[(\d+)\]"

# Simple matching in Python
print("\n--> Simple matching in Python:\n")

# The rawstring and the normal string are exactly the same,
# but it's a good idea to always use rawstrings for regular expressions in Python.

import re
result = re.search(r"aza", "plaza")
print(result)

import re
result = re.search(r"aza", "bazaar")
print(result)

import re
result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))

import re
print(re.search(r"p.ng", "penguin"))

import re
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

import re
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

# Wildcards and Character Classes
print("\n--> Wildcards and Character Classes:\n")

import re
print(re.search(r"[Pp]ython", "Python"))

import re
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

import re
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

# Repetition Qualifiers .*
print("\n--> Repetition Qualifiers:\n")

import re
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

import re
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

import re
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

# Escaping Characters with symbol \
# When we see a pattern that includes a backslash,
# it could be escaping a special regex character
# or a special string character.

print("\n--> Escaping Characters:\n")

import re
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

# For example, \w matches any alphanumeric
# character including letters, numbers, and underscores.
# There's also \d for matching digits, \s for matching whitespace
# characters like space, tab or new line,
# \b for word boundaries and a few others.

import re
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

import re
def check_character_groups(text):
  result = re.search(r"\w ", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

# Regular Expressions in Action
print("\n--> Regular Expressions in Action:\n")

import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

import re
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

""" Regex examples
r”\d{3}-\d{3}-\d{4}”  This line of code
matches U.S. phone numbers in the format 111-222-3333.

r”^-?\d*(\.\d+)?$”  This line of code
matches any positive or negative number,
with or without decimal places.

r”^/(.+)/([^/]+)/$” This line of code
is often used to extract specific parts
of URLs or file paths, such as the directory names or filenames.
"""

# Practicing Regex examples

# Validating Web Addresses
print("\n--> Regex examples - Web Address:\n")

import re
def check_web_address(text):
  pattern = r"^[\w\. \-\+]+\.[a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

"""
r" ^ [\w\.\-\+]+ \. [a-zA-Z]+ $ "
     │ └─────────┘ │  └───────┘ │
     │      │      │      │     └── 5. End of string anchor
     │      │      │      └──────── 4. 1+ alphabetic characters (TLD)
     │      │      └─────────────── 3. Literal dot separating name & TLD
     │      └────────────────────── 2. 1+ valid domain characters
     └───────────────────────────── 1. Start of string anchor

"""

# Validating Time (12-hour format)
print("\n--> Regex examples - Time:\n")

import re
def check_time(text):
  pattern = r"^(1[0-2]|[1-9]):[0-5][0-9]\s?[aApP][mM]$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

"""

r" ^ (1[0-2]|[1-9]) : [0-5][0-9] \s? [aApP][mM] $ "
   │ └────────────┘ │ └────────┘  │  └─────────┘ │
   │       │        │     │       │       │      └── 6. End-of-string anchor
   │       │        │     │       │       └───────── 5. Case-insensitive AM/PM
   │       │        │     │       └───────────────── 4. Optional space
   │       │        │     └───────────────────────── 3. Minutes: 00 to 59
   │       │        └─────────────────────────────── Literal colon delimiter
   │       └──────────────────────────────────────── 2. Hours: 1-12 (no leading 0)
   └──────────────────────────────────────────────── 1. Start-of-string anchor

"""

# Checking for Acronyms
print("\n--> Regex examples - Acronyms:\n")

import re
def contains_acronym(text):
  pattern = r"\([A-Z0-9][a-zA-Z0-0]+\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

"""
\( and \): Literal parentheses surrounding the acronym.
Unescaped ( and ) create capturing groups, so they must be
escaped with \ to match literal ( and ).

[A-Z0-9]: Ensures the first character inside the parentheses
is an uppercase letter or a digit (handling alphanumeric acronyms
like (4GL) and standard uppercase ones like (IM) or (Scuba)).

[a-zA-Z0-9]+: Matches the remaining characters (letters or digits).
Using the + quantifier (one or more) guarantees that combined with
the first character, the acronym contains 2 or more characters.

(Note: In the Coursera grading suite, r"\([A-Z0-9][a-zA-Z0-9]*\)"
or r"\([A-Z1-9][a-zA-Z0-9]*\)" are also commonly accepted solutions
depending on how they test single vs. multiple subsequent characters).

"""

# Checking for valid ZIP Codes (US)
print("\n--> Regex examples - ZIP Codes:\n")

import re

def correct_function(text):
  result = re.search(r" +[0-9]{5}(-[0-9]{4})?", text)  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

"""
  + [0-9]{5} : Matches a space followed by exactly five digits.
  (-[0-9]{4})?: Optionally matches a hyphen followed by exactly four digits.

r"  +   \d{5}   ( - \d{4} )?  "
     │      │     └─────┬────┘
     │      │           └── 3. Optional 4-digit extension with hyphen
     │      └────────────── 2. Exactly 5 digits
     └───────────────────── 1. At least one space (not at text start)

"""

# Capturing Groups
print("\n--> Capturing Groups:\n")

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")

# printing for a terminal result and not for a function example
# Option 1: Print directly
print(rearrange_name("Lovelace, Ada"))

# Option 2: Store in a variable first, then print
formatted_name = rearrange_name("Lovelace, Ada")
print(formatted_name)

# Example with "Ritchie, Dennis"

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Ritchie, Dennis")

# printing for a terminal result and not for a function example
print(rearrange_name("Ritchie, Dennis"))

# Example with "Hopper, Grace M."

import re
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Hopper, Grace M.")

# printing for a terminal result and not for a function example
print(rearrange_name("Hopper, Grace M."))

# Matching a middle name or initial
print("\n--> Matching a middle name or initial:\n")

import re
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

"""

r" ^ ( [\w \.-]* ) ,   ( [\w \.-]* ) $ "
   │ └─────┬─────┘ │ │ └─────┬─────┘ │
   │       │       │ │       │       └── 5. End of string anchor
   │       │       │ │       └────────── 4. Group 2 (Given / Middle Names)
   │       │       │ └────────────────── Single space literal
   │       │       └──────────────────── Comma literal separator
   │       └──────────────────────────── 2. Group 1 (Surname)
   └──────────────────────────────────── 1. Start of string anchor

"""

# More on repetition qualifiers
print("\n--> More on repetition qualifiers:\n")

import re
print(re.search(r"[a-zA-Z]{5}", "a ghost"))

import re
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

import re
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

import re
re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")

import re
print(re.findall(r"\w{5,10}", "I really like strawberries"))

import re
print(re.findall(r"\w{5,}", "I really like strawberries"))

import re
print(re.search(r"s\w{,20}", "I really like strawberries"))

# Extracting a PID using regexes in Python
print("\n--> Extracting a PID using regexes in Python:\n")

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

"""

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
print(result[1])
#Note that this print command results in an error as shown in the video.

"""

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))

# PID (Process ID) and a log (e.g. ERROR, INFO, etc.)
print("\n--> PID (Process ID) and a log (e.g. ERROR, INFO, etc.):\n")

import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]:\s+([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

"""

r" \[ (\d+) \] : \s+ ([A-Z]+) "
   │  └──┬─┘ │ │  │  └───┬──┘
   │     │   │ │  │      └── Group 2: One or more uppercase letters (ERROR, RUNNING)
   │     │   │ │  └───────── One or more whitespace characters
   │     │   │ └──────────── Literal colon
   │     │   └────────────── Literal closing bracket
   │     └────────────────── Group 1: One or more digits (PID)
   └──────────────────────── Literal opening bracket

"""

# Splitting and Replacing
print("\n--> Splitting and Replacing:\n")

import re
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

import re
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

import re
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))

import re
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))

# Quiz - Test your knowledge: Advanced regular expressions
print("\n--> Quiz - Test your knowledge: Advanced regular expressions\n")

# Question 1 (adding +1 to phone numbers)
print("\n--> Question 1 (adding +1 to phone numbers):\n")

import re
def transform_record(record):
  new_record = re.sub(r",([\d-]+),", r",+1-\1,", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer

"""

Pattern:      , ( [\d-]+ ) ,
              │ └────┬───┘ │
              │      │     └── Literal trailing comma
              │      └──────── Group 1: Matches all digits and hyphens in the phone number
              └─────────────── Literal leading comma

Replacement:  , +1- \1 ,
              │  │   │ └── Literal trailing comma
              │  │   └──── Backreference restoring the captured phone number
              │  └──────── International country prefix to insert
              └─────────── Literal leading comma

"""

# Question 2 (multi-vowel words)
print("\n--> Question 2 (multi-vowel words)\n")

import re
def multi_vowel_words(text):
  pattern = r"\b\w*[aeiou]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []

"""

r" \b \w* [aeiouAEIOU]{3,} \w* \b "
   │   │  └──────┬───────┘  │   └── 5. Word boundary (end of word)
   │   │         │          └────── 4. Zero or more trailing word characters
   │   │         └───────────────── 3. Exactly 3 or more consecutive vowels
   │   └─────────────────────────── 2. Zero or more leading word characters
   └─────────────────────────────── 1. Word boundary (start of word)

"""

# Question 4 (The transform_comments)
print("\n--> Question 4 (The transform_comments)\n")

import re
def transform_comments(line_of_code):
  result = re.sub(r"#+", r"//", line_of_code)
  return result

print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))
# Should be "  return(number)"

"""

Breakdown of the Arguments
Pattern (r"#+"):

#: Matches the literal hash character.

+: The repetition qualifier matching one or more consecutive occurrences.
This handles a single comment marker (#) as well as repeated headers
like ## or ###, treating them as a single matched unit.

Replacement (r"//"):

The entire sequence of one or more # characters is replaced with a single //.

String (line_of_code):

The target text being searched and transformed. If no # is found (like in
"return(number)"), re.sub() leaves the line unchanged and returns it as-is.

"""

# Question 5 (convert phone numbers)
print("\n--> Question 5 (convert phone numbers):\n")

import re
def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3}-\d{4})\b", r"(\1) \2", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))
# Phone number of Buckingham Palace is +44 303 123 7300

"""

Pattern:      \b ( \d{3} ) - ( \d{3}-\d{4} ) \b
              │  └───┬───┘ │ └──────┬──────┘ │
              │      │     │        │        └── 5. Trailing word boundary
              │      │     │        └─────────── 4. Group 2: remaining 3 digits, dash, 4 digits
              │      │     └──────────────────── 3. Literal hyphen separator
              │      └────────────────────────── 2. Group 1: initial 3-digit area code
              └───────────────────────────────── 1. Leading word boundary

Replacement:  ( \1 )   \2
              │  │  │  │
              │  │  │  └──── Re-inserts Group 2 (XXX-XXXX)
              │  │  └─────── Space separator
              └───────────── Wraps Group 1 in literal parentheses: (XXX)

"""

# re.sub() with flags (re.IGNORECASE)
print("\n--> re.sub() with flags (re.IGNORECASE)\n")

import re

def update_email_domain(email_record, old_domain, new_domain):
    # Match the username before @ and replace only the old domain at the end
    pattern = r'@' + re.escape(old_domain) + r'$'
    replacement = '@' + new_domain

    # re.sub searches for the pattern and substitutes it
    return re.sub(pattern, replacement, email_record)

# Example entries
records = [
    "alex.smith@legacycorp.com",
    "maria_k@legacycorp.com",
    "dev-team@otherdomain.org"
]

updated_records = [
    update_email_domain(user, "legacycorp.com", "moderncloud.io")
    for user in records
]

print(updated_records)
# Output:
# [
#   'alex.smith@moderncloud.io',
#   'maria_k@moderncloud.io',
#   'dev-team@otherdomain.org'
# ]
