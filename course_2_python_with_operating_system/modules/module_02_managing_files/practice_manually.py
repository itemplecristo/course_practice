import csv

f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone,role))
f.close()

hosts = [["workstation.local", '192.168.25.46'],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

# Write name,version,status,users csv file

names = [{"name": "MailTree", "version": "5.34", "status": "production", "users": "324"}, 
{"name": "CalDoor", "version": "1.25.1", "status": "beta", "users": "22"}, 
{"name": "Chatty Chicken", "version": "0.34", "status": "alpha", "users": "4"}]
keys = ["name", "version", "status", "users"]
with open('software.csv', 'w') as software:
    writer = csv.DictWriter(software, fieldnames=keys)
    writer.writeheader()
    writer.writerows(names)

# Read name,version,status,users csv file and print the name and number of users
print("\n--> Reading name,version,status,users csv file \n")

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
      print(("{} has {} users").format(row["name"], row["users"]))

# Practice Quiz" Reading and Writing CSV files
print("\n--> Practice Quiz Reading and Writing CSV files\n")

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string
  
#Call the function
print(contents_of_file("flowers.csv"))