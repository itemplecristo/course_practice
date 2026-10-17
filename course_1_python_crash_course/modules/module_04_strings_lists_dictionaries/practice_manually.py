"""Module 04: Strings, Lists & Dictionaries (Manual Practice / Scratchpad)
Run directly: python course_1_python_crash_course/modules/module_04_strings_lists_dictionaries/practice_manually.py
"""

print("\n---> Module 04: Strings, Lists & Dictionaries manual experiments\n")

# Core Knoledge Drills
print("\n--> Core Knoledge Drills\n")

# 1. Dictionary Keys & Output
# To extract the keys of a dictionary as an explicit Python list,
# pass the .keys() view object into list():
print("\n--> 1. Dictionary Keys & Output\n")

user_data = {"id": 101, "role": "admin", "status": "active"}

# .keys() returns a view object dict_keys(['id', 'role', 'status'])
keys_list = list(user_data.keys())
print(keys_list)

# 2. String Slicing Mechanics
# Python slice notation follows string[start:stop:step], where start
# is inclusive and stop is exclusive:
print("\n--> 2. String Slicing Mechanics\n")

phrase = "Automation"

# Index positions:
#  A  u  t  o  m  a  t  i  o  n
#  0  1  2  3  4  5  6  7  8  9

print(phrase[:4])
print(phrase[4:6])
print(phrase[6:])

# 3. List Insertion Behavior
# list.insert(index, element) shifts all elements at or after index
# one position to the right. It operates in place and returns None:
print("\n-->List Insertion Behavior\n")

servers = ["web-01", "db-01", "cache-01"]
servers.insert(1, "web-02")

print(servers)

# 4. Replacing Words with Uppercase
# Combine .replace() with .upper():
print("\n--> Replacing Words with Uppercase\n")

sentence = "The error code reported a critical bug."
target = "error"

updated_sentence = sentence.replace(target, target.upper())
print(updated_sentence)

# 5. Frequency Counter Pattern
# Count character frequencies by initializing counts dynamically using dict.get():
print("\n--> Frequency Counter Pattern\n")

def count_letters(text):
    frequencies = {}
    for char in text.lower():
        if char in text.lower():
            if char.isalpha():
                frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies

print(count_letters("Cloud Ops"))

# Drill A: Filter Specific Keys
print("\n--> Drill A: Filter Specific Keys\n")
# Output: {'c': 1, 'l': 1, 'o': 2, 'u': 1, 'd': 1, 'p': 1, 's': 1}

"""

Write a function that accepts any dictionary
and returns only keys whose length is greater
than 3 characters:

Here are two ways to solve this problem, following the Accumulator Blueprint
and the modern List Comprehension pattern taught in Module 4.

"""

# Method 1: The Accumulator Pattern (Explicit & Foundational)
# This follows the three-step accumulator cycle: initialize a tracker list,
# loop through keys with an if filter, and return the result.
print("\n--> Method 1: The Accumulator Pattern (Explicit & Foundational)\n")

def get_long_keys(data_dict):
    # 1. Initialize: Create an empty list to accumulate results
    long_keys = []

    # 2. Accumulate: Iterate through the dictionary keys
    for key in data_dict:
        # Check if the length of the key string is strictly greater than 3
        if len(key) > 3:
            long_keys.append(key)

    # 3. Return: Hand back the completed list
    return long_keys

test_dict = {"id": 101, "role": "admin", "status": "active"}
result = get_long_keys(test_dict)
print(result)

# Clean manuall code

def get_long_keys(data_dict):
    long_keys = []
    for key in data_dict:
        if len(key) > 3:
            long_keys.append(key)
    return long_keys

test_dict = {"id": 101, "role": "admin", "status": "active", "mission": 777}
result = get_long_keys(test_dict)
print(result)

# Method 2: List Comprehension with an if Condition (Idiomatic & Compact)
# In Course 1, Module 4, list comprehensions are introduced as a direct
# shortcut for accumulator loops:
print("\n--> Method 2: List Comprehension with an if Condition (Idiomatic & Compact)\n")
def get_long_keys(data_dict):
    # Syntax: [expression for item in collection if condition]
    return [key for key in data_dict if len(key) > 3]

# Test case
test_dict = {"id": 101, "role": "admin", "status": "active"}
print(get_long_keys(test_dict))
# Output: ['role', 'status']

# Clean manuall code

def get_long_keys(data_dict):
    return [key for key in data_dict if len(key) > 3]

test_dict = {"id": 101, "role": "admin", "status": "active", "mission": 777}
print(get_long_keys(test_dict))


# Skill 1: String Parsing & Formatting
print("\n--> String Parsing & Formatting\n")

# Parse mixed server log strings, isolate numeric status codes
# from textual tokens, and format output:

"""

Because functions act as isolated "black boxes,"
the name outside does not need to match the name inside.
You could pass in log_line, server_message,
or entry_text—inside the function, it will always be
received and handled by the parameter name: raw_entry.

"""

def parse_log_entry(raw_entry):
    # Strip whitespace and break into tokens
    tokens = raw_entry.strip().split()

    words = []
    codes = []

    for token in tokens:
        # Check string classification
        if token.isalpha():
            words.append(token.lower())
        elif token.isnumeric():
            codes.append(token)

    summary_text = " ".join(words)
    primary_code = codes[0] if codes else "N/A"

    # Foematted using str.format()
    return "Status: {code} | Details: {details} (Length: {length})".format(
        code=primary_code, details=summary_text, length=len(summary_text))

log_line = "    Server 500 Internal FAILURE 01    "
print(parse_log_entry(log_line))

# Skill 2: In-Place List Mutation
print("\n--> Skill 2: In-Place List Mutation\n")

active_tasks = ["backup", "sync"]
new_tasks = ["cleanup", "audit"]

# Extend active_tasks in place with elements from new_tasks
active_tasks.extend(new_tasks)
print("After extend:", active_tasks)
# Output: ['backup', 'sync', 'cleanup', 'audit']

# Reverse queue order in place
active_tasks.reverse()
print("After reverse:", active_tasks)
# Output: ['audit', 'cleanup', 'sync', 'backup']

# Skill 3: List Comprehensions & Bounds
# Construct calculated lists using two-parameter
# ranges (lower, upper + 1) and conditional filtering:
print("\n--> Skill 3: List Comprehensions & Bounds\n")

lower_bound = 1
upper_bound = 10

# Formula calculation over range(lower, upper + 1)
squares = [x**2 for x in range(lower_bound, upper_bound + 1)]
print("Squares:", squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List comprehension with filtering condition (even squares only)
even_squares = [x**2 for x in range(lower_bound, upper_bound + 1) if x % 2 == 0]
print("Even Squares:", even_squares)
# Output: [4, 16, 36, 64, 100]

# Skill 4: Dictionary Transformation & Iteration
print("\nSkill 4: Dictionary Transformation & Iteration\n")

# Iterate over key-value pairs using .items(), create a isolated
# shallow copy with .copy(), and modify the clone in place:

resource_thresholds = {
    "cpu_limit": 70,
    "memory_limit": 80,
    "disk_limit": 85
}

# 1. Iterate and format keys/values
for resource, limit in resource_thresholds.items():
    print("Resource '{0}' threshold set to {1}%".format(resource, limit))

# 2. Copy and update values without mutating original
adjusted_thresholds = resource_thresholds.copy()

for key in adjusted_thresholds:
    # Scale values by 10%
    adjusted_thresholds[key] = int(adjusted_thresholds[key] * 1.10)

print("Original:", resource_thresholds)
# Output: {'cpu_limit': 70, 'memory_limit': 80, 'disk_limit': 85}

print("Adjusted:", adjusted_thresholds)
# Output: {'cpu_limit': 77, 'memory_limit': 88, 'disk_limit': 93}


# Challenge: Server Error Log Aggregator
print("\n--> Challenge: Server Error Log Aggregator\n")

def aggregate_service_errors(log_records):
    error_counts = {}

    for entry in log_records:
        tokens = entry.strip().split("-")
        if len(tokens) >= 3:
            service = tokens[0].strip().lower()
            status = tokens[1].strip().lower()
            if status == "error":
                error_counts[service] = error_counts.get(service, 0) + 1

    return error_counts

raw_logs = [
    "AUTH - INFO - User login successful",
    "  DATABASE  - ERROR - Connection timeout",
    "PAYMENT - WARNING - Retry attempt 1",
    "auth - ERROR - Invalid credentials",
    "database - ERROR - Query syntax error",
    "API - INFO - Request received 200 OK",
    "DATABASE - ERROR - Deadlock detected",
    " payment - ERROR - Gateway unreachable "
]

# Run your pipeline and format the output:

aggregated_errors = aggregate_service_errors(raw_logs)

print(aggregated_errors)
