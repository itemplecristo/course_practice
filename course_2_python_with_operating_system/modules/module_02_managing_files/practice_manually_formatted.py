"""
Module 02: Practice Manually (PEP 8 & Black formatted version)
Compare with practice_manually.py to see formatting differences.
"""

import csv

# 1. Reading basic CSV file
with open("csv_file.txt", "r", encoding="utf-8") as f:
    csv_f = csv.reader(f)
    for row in csv_f:
        name, phone, role = row
        print(f"Name: {name}, Phone: {phone}, Role: {role}")

# 2. Writing hosts CSV file
hosts = [
    ["workstation.local", "192.168.25.46"],
    ["webserver.cloud", "10.2.5.6"],
]
with open("hosts.csv", "w", newline="", encoding="utf-8") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

# 3. Writing by_department CSV file using DictWriter
users = [
    {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
    {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"},
]
keys = ["name", "username", "department"]
with open("by_department.csv", "w", newline="", encoding="utf-8") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

# 4. Writing software CSV file
names = [
    {"name": "MailTree", "version": "5.34", "status": "production", "users": "324"},
    {"name": "CalDoor", "version": "1.25.1", "status": "beta", "users": "22"},
    {"name": "Chatty Chicken", "version": "0.34", "status": "alpha", "users": "4"},
]
keys = ["name", "version", "status", "users"]
with open("software.csv", "w", newline="", encoding="utf-8") as software:
    writer = csv.DictWriter(software, fieldnames=keys)
    writer.writeheader()
    writer.writerows(names)

# 5. Reading software CSV file and printing user count
print("\n--> Reading name,version,status,users csv file\n")

with open("software.csv", "r", encoding="utf-8") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(f"{row['name']} has {row['users']} users")
