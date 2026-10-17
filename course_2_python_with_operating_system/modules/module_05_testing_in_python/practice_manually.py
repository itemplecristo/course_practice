"""Module 05: Testing in Python (Manual Practice / Scratchpad)
Run directly: python course_2_python_with_operating_system/modules/module_05_testing_in_python/practice_manually.py
"""

print("\n---> Module 05: Testing in Python manual experiments\n")

"""

import re

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))

# Testing with from command line

"""

"""

#!/usr/bin/env python3
import re
def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])
from rearrange import rearrange_name

rearrange_name("Lovelace, Ada")

"""

# Writing unit tests in python
print("\n--> Writing unit tests in python\n")

"""

#!/usr/bin/env python3

import re

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  return "{} {}".format(result[2], result[1])



#!/usr/bin/env python3

import unittest

from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):

  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

# Run the tests
unittest.main()



chmod +x rearrange_test.py
./rearrange_test.py

"""

# Edge case
print("\n--> Edge case\n")

# Edge cases are inputs to our code that produce unexpected results,
# and are found at the extreme ends of the ranges of input we imagine
# our programs will typically work with.

"""

def test_empty(self):
  testcase = ""
  expected = ""
  self.assertEqual(rearrange_name(testcase), expected)


#!/usr/bin/env python3

import re

def rearrange_name(name):
  result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
  if result is None:
    return ""
  return "{} {}".format(result[2], result[1])

./rearrange_test.py

"""

# Here is a function designed for log parsing and automation.
# We will look at its IPO contract, review a test suite generated for it,
# and audit it for flaws.

# Step 1: The Function Under Test
# This function extracts the process ID (PID) from standard syslog lines:

print("\n--> The Function Under Test:\n")

"""

import re

def extract_pid(log_line):

    # Extracts a numeric PID enclosed in brackets from a log line.
    # Example: 'Jul 26 14:05:01 server CRON[12345]: (root) CMD' -> '12345'

    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result.group(1)

"""

"""

The IPO Contract:Input: A string (log_line) representing a single line from a log file.
Process: Use regex to search for one or more digits inside literal brackets [...]
and extract the capturing group.   Output: The extracted PID as a string, or an empty string ""
if no bracketed number is found.

"""

# Step 2: The Generated Unit Test Suite
# Here is a typical test suite produced for this function:
print("\n--> The Generated Unit Test Suite:\n")

"""

import unittest
from log_helper import extract_pid

class TestExtractPid(unittest.TestCase):

    def test_basic_cron(self):
        testcase = "Jul 26 14:05:01 server CRON[12345]: (root) CMD"
        expected = "12345"
        self.assertEqual(extract_pid(testcase), expected)

    def test_another_service(self):
        testcase = "Aug 10 09:12:00 myhost systemd[999]: Started Session."
        expected = "999"
        self.assertEqual(extract_pid(testcase), expected)

    def test_no_pid(self):
        testcase = "Aug 10 09:12:00 myhost systemd: Started Session."
        expected = ""
        self.assertEqual(extract_pid(testcase), expected)

if __name__ == "__main__":
    unittest.main()

"""

# Step 3: The Audit
# Running this test suite yields all green checks:
print("\n--> The Audit:\n")

"""

...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

However, as the verification lead auditing this code:
False Positive / Brittle Regex: What happens if a log line contains bracketed
text with numbers that isn't the PID earlier in the line
(e.g., "Sep 12 [2026] CRON[54321]: message")? Which value does re.search() grab first?
Missing Edge Cases: What happens if someone passes an empty string ""?
Or a line with empty brackets []?Data Type Contracts: What happens if a caller passes
None or an integer instead of a string? Does re.search() return "", or will it crash
with an unhandled TypeError?   Your Turn to Audit:Looking at those gaps,
how should we test the line "Sep 12 [2026] CRON[54321]: message"? Would extract_pid return "2026" or "54321"?

"""


"""
1. The "Happy Path" (test_basic_cron):
   - Input: Standard syslog line with PID in brackets.
   - Output: The PID as a string.
   - Verdict: CORRECT. The regex \[(\d+)\] successfully captures the digits inside the brackets.

2. Variation in PIDs (test_another_service):
   - Input: A different service (systemd) with a different PID (999).
   - Output: The PID 999.
   - Verdict: CORRECT. The regex \[(\d+)\] is generic and matches any sequence of digits inside brackets.

3. Handling Missing Data (test_no_pid):
   - Input: A log line with no brackets or PID.
   - Expected Output: "" (empty string).
   - Verdict: CORRECT. The function correctly returns an empty string when re.search returns None.

4. Missing Test Cases (The Security Blind Spot):
   - The tests DO NOT cover:
     - Malicious strings (e.g., trying to extract surrounding text).
     - Malformed brackets (e.g., [123 or 123]).
     - Very large PIDs or non-decimal numbers if the system supported them.
   - Verdict: The tests are insufficient for a security-critical application, but sufficient for the specified task.
"""


# Test suites
print("\n--> Test suites:\n")

"""

import unittest
import os
import shutil

# Function to test
def simple_addition(a, b):
	return a + b

# Paths for file operations
ORIGINAL_FILE_PATH = "/tmp/original_test_file.txt"
COPIED_FILE_PATH = "/mnt/data/copied_test_file.txt"

# Global counter
COUNTER = 0

# This method will be run once before any tests or test classes
def setUpModule():
	global COUNTER
	COUNTER = 0

	# Create a file in /tmp
	with open(ORIGINAL_FILE_PATH, 'w') as file:
    	file.write("Test Results:\n")

# This method will be run once after all tests and test classes
def tearDownModule():
	# Copy the file to another directory
	shutil.copy2(ORIGINAL_FILE_PATH, COPIED_FILE_PATH)

	# Remove the original file
	os.remove(ORIGINAL_FILE_PATH)

class TestSimpleAddition(unittest.TestCase):

	# This method will be run before each individual test
	def setUp(self):
    	global COUNTER
    	COUNTER += 1

	# This method will be run after each individual test
	def tearDown(self):
    	# Append the test result to the file
    	with open(ORIGINAL_FILE_PATH, 'a') as file:
        	result = "PASSED" if self._outcome.success else "FAILED"
        	file.write(f"Test {COUNTER}: {result}\n")

	def test_add_positive_numbers(self):
    	self.assertEqual(simple_addition(3, 4), 7)

	def test_add_negative_numbers(self):
    	self.assertEqual(simple_addition(-3, -4), -7)

# Running the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleAddition)
runner = unittest.TextTestRunner()
runner.run(suite)

# Read the copied file to show the results
with open(COPIED_FILE_PATH, 'r') as result_file:
	test_results = result_file.read()

print(test_results)

"""

# Practice Notebook - Unit Tests and Edge Cases
print("\n--> Practice Notebook - Unit Tests and Edge Cases\n")

import re

my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))


import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

class TestCompiler2(unittest.TestCase):

    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
    def test_three(self):
        testcase = "In the beginning God created the heavens and the earth."
        expected = ['b', 'c', 'a', 'a', 'a', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

unittest.main(argv = ['first-arg-is-ignored'], exit = False)

# White-box Testing and Black-box Testing
print("\n--> White-box Testing and Black-box Testing\n")

"""

White-box testing also sometimes called clear-box or transparent testing relies on the
test creator's knowledge of the software being tested to construct the test cases.

On the other hand, in black-box testing, the software being tested is treated like an opaque box.

Black-box tests are written with an awareness of what the program is supposed to do, its
requirements or specifications, but not how it does it.

"""

# TDD

"""

A process called test-driven development or TDD calls for creating the test before writing the code.

When engineers submit their code, it's integrated into the main repository and tests are automatically
run against it to spot bugs and errors in a process called Continuous Integration.

Check out the following links for more information:

https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/

https://landing.google.com/sre/sre-book/chapters/testing-reliability/

https://testing.googleblog.com/2007/10/performance-testing.html

https://www.guru99.com/smoke-testing.html

https://www.guru99.com/exploratory-testing.html

https://testing.googleblog.com/2008/09/test-first-is-fun_08.html



"""

# The Try-Except concept
print("\n--> The Try-Except concept\n")

#!/usr/bin/env python3

def character_frequency(filename):
  """Counts the frequency of each character in the given file."""
  # First try to open the file
  try:
    f = open(filename)
  except OSError:
    return None

  # Now process the file
  characters = {}
  for line in f:
    for char in line:
      characters[char] = characters.get(char, 0) + 1
  f.close()
  return characters

"""

So when writing a try-except block, the important thing to remember
is that the code in the except block is only executed if one of the instructions
in the try block raises an error of the matching type.

"""

# Raising errors
print("--> Raising errors\n")

# The raise keyword can be used to raise errors in Python.
# The following code raises a ValueError exception:

"""

def check_positive(number):
    if number <= 0:
        raise ValueError("Number must be positive")
    return number

check_positive(-5   )

When an exception is raised, the normal flow of execution is stopped and Python
attempts to handle the exception by looking for a matching except block.
If no matching except block is found, the exception is propagated up the call stack
until it is handled or until the program terminates.

#!/usr/bin/env python3

def validate_user(username, minlen):
  if minlen < 1:
    raise ValueError("minlen must be at least 1")

  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True



from validations import validate_user
validate_user("", -1)

from validations import validate_user
validate_user("", 1)
validate_user("myuser", 1)

from validations import validate_user
validate_user(88, 1)

from validations import validate_user
validate_user([], 1)

from validations import validate_user
validate_user(["name"], 1)

#!/usr/bin/env python3

def validate_user(username, minlen):
  assert type(username) == str, "username must be a string"
  if minlen < 1:
    raise ValueError("minlen must be at least 1")

  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True


from validations import validate_user
validate_user([3], 1)


"""

# Testing for expected errors
print("--> Testing for expected errors\n")

"""

#!/usr/bin/env python3

import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):
  def test_valid(self):
    self.assertEqual(validate_user("validuser", 3), True)

  def test_too_short(self):
    self.assertEqual(validate_user("inv", 5), False)

  def test_invalid_characters(self):
    self.assertEqual(validate_user("invalid_user", 1), False)

  def test_invalid_minlen(self):
    self.assertRaises(ValueError, validate_user, "user", -1)


# Run the tests
unittest.main()

"""

# Exception handling
print("\n--> Exception handling\n")

"""

When performing exception handling, it is important to predict which exceptions can happen.
Sometimes, to figure out which exceptions you need to account for, you have to let your program fail.

The simplest way to handle exceptions in Python is by using the try and except clauses.

In the try clause, Python executes all statements until it encounters an exception.
You use the except clause to catch and handle the exception(s) that Python encounters in the try clause.

Here is the process for how it works:

Python runs the try clause, e.g., the statement(s) between the try and except keywords.

If no error occurs, Python skips the except clause and the execution of the try statement is finished.

If an error occurs during execution of the try clause, Python skips the rest of the try clause
and transfers control to the corresponding except block. If the type of error matches what is listed
after the except keyword, Python executes the except clause. The execution then continues on after
the try/except block.

If an exception occurs but it does not match what is listed in the except clause, it is passed onto
try statements outside of that try/except block. However, if a handler for that exception cannot be found,
the exception becomes an unhandled exception, the execution stops, and Python displays a designated error message.

Sometimes, a try statement can have more than one except clause so that the code can specify handlers
for different exceptions. This can help to reduce the number of unhandled exceptions.

You can use exceptions to catch almost everything. It is good practice as a developer or programmer to be
as specific as possible with the types of exceptions that you intend to handle, especially if you’re creating
your own exceptions.

Raise exceptions
As a developer or programmer, you might want to raise an error yourself. Usually, this happens when some
of the conditions necessary for a function to do its job properly aren't met and returning none or some
other base value isn't good enough. You can raise an error or raise an exception (also known as “throwing
an exception”), which forces a particular exception to occur, and notifies you that something in your code
is going wrong or an error has occurred.

Here are some instances where raising an exception is a useful tool:

A file doesn’t exist

A network or database connection fails

Your code receives invalid input

In the example below, the code raises two built-in Python exceptions:  raise ValueError and raise
ZeroDivisionError. You can find more information on these raises in the example below, along with
explanations of potential errors that may occur during an exception.

Example exception handling
Now that you have an understanding of try and except clauses, assert statements, and raising exceptions,
consider the following code examples which use all of these concepts together.

The basic structure of exception handling is as follows:

# File reading function with exception handling
def read_file(filename):
	try:
		with open(filename, 'r') as f:
			return f.read()
	except FileNotFoundError:
		return "File not found!"
	finally:
		print("Finished reading file.")

Imagine you have a function that reads data from a file and then divides
two numbers provided within that file.
There are some faults in it that you can catch with exceptions.

def faulty_read_and_divide(filename):
	with open(filename, 'r') as file:
		data = file.readlines()
		num1 = int(data[0])
		num2 = int(data[1])
		return num1 / num2

There are several potential issues here:

The file might not exist, causing a FileNotFoundError.

The file might not have enough lines of data, leading to an IndexError.

The data in the file might not be convertible to integers, raising a ValueError.

The second number might be zero, which would raise a ZeroDivisionError.

To address these potential issues, you can add the appropriate exception handling illustrated below:

def enhanced_read_and_divide(filename):
	try:
		with open(filename, 'r') as file:
			data = file.readlines()
       	 
        # Ensure there are at least two lines in the file
        if len(data) < 2:
            raise ValueError("Not enough data in the file.")
       	 
        num1 = int(data[0])
        num2 = int(data[1])
       	 
        # Check if second number is zero
        if num2 == 0:
            raise ZeroDivisionError("The denominator is zero.")
       	 
        return num1 / num2


	except FileNotFoundError:
    	     return "Error: The file was not found."
	except ValueError as ve:
    	     return f"Value error: {ve}"
	except ZeroDivisionError as zde:
    	     return f"Division error: {zde}"


Now, the function enhanced_read_and_divide is equipped to handle potential exceptions gracefully,
providing informative error messages to the caller. This way, the code will explain when it fails
since you have identified potential fault zones such as when dealing with unpredictable inputs or file content.

Notice how the exceptions are instantiated as objects (such as ValueError ve) that you can use to
further diagnose the issue by printing them out.


The errors should read:

File-level issues:

Value error: Not enough data in the file.

Error: The file was not found.

Data-level issues:

Value error: invalid literal for int() with base 10: 'apple'

Division error: The denominator is zero.


assert statements
assert statements help you to verify if a certain condition is met and throw an exception if it isn’t.
As is stated in the name, their purpose is to "assert" that certain conditions are true at specific
points in your program.

The assert statement exists in almost every programming language and has two main uses:

To help detect problems earlier in development, rather than later when some other operation fails.
Problems that aren’t addressed until later in the development process can turn out to be more time-intensive
and costly to fix.

To provide a form of documentation for other developers reading the code.

You can learn more about common assertions that you might use when handling errors in
Study guide: Unit test
.

Key takeaways
For a bit of light reading, or for more information on raising exceptions, assertions, the try clause,
exceptions, or handling errors, visit the following links:

https://doughellmann.com/posts/python-exception-handling-techniques

https://docs.python.org/3/tutorial/errors.html#raising-exceptions


https://realpython.com/python-exceptions/

https://realpython.com/python-raise-exception/#handling-exceptional-situations-in-python

"""
