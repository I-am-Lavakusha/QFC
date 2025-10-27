# # frequency of words in a given sttring using dictionary
input1="india is good and people in india are also good"
input2=input1.split(" ")
dict1={}
for i in input2:
  if i in dict1:
    dict1[i]+=1
  else:
    dict1[i]=1
print(dict1)

# # 
# import re
dict1={}
text = "Contact us at support@example.com or sales@company.org for more info."
search=re.findall(r"\S+\@\S+", text)
search2=re.findall(r"\@\S+", text)
for i in range(len(search)):
  for j in range(i,len(search2)):
    dict1[search[i]]=search2[j]
    break
print(dict1)


# # {'support@example.com': 'example.com', 'sales@company.org': 'company.org'}

import re
dict2={}
text1 = "Alice met Bob. Alice and Bob went to Paris. Bob liked Paris."
pattern=re.findall(r"[A-Z]\w+", text1)
for i in pattern:
  if i in dict2:
    dict2[i]+=1
  else:
    dict2[i]=1

print(dict2)
# {'Alice': 2, 'Bob': 3, 'Paris': 2}



# Create a dictionary that maps numbers (1–5) to their squares using a loop.

result={}
for i in range(1,6):
  result[i]=i*i
print(result)

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Write a Python program that takes a paragraph as input and counts how many numeric values (like 123, 4.5, etc.) appear in it using regular expressions.
# Store the unique numbers as keys in a dictionary and their count of occurrences as values.

import re
res={}
text = "I bought 3 apples, 4.5 kg of mangoes, and 3 more oranges. Total: 7.5 kg."
search=re.findall(r"\d+\.\d+|\d+", text)
for i in search:
  if i in res:
    res[i]+=1
  else:
    res[i]=1
print(res)

# {'3': 2, '4.5': 1, '7.5': 1}

# You have a log text containing multiple user activities.
# Extract all usernames and their IP addresses using regex and store them in a dictionary,
# where each username maps to a list of unique IPs.

import re
dict1={}
log = """
User: alice IP: 192.168.1.10  
User: bob IP: 10.0.0.2  
User: alice IP: 192.168.1.11  
User: bob IP: 10.0.0.2
"""

find=re.findall(r"\S+\s+(\S+)\s+\S+\s+(\S+)", log)
for key, value in find:
  if key not in dict1:
    dict1[key]=[]
  if value not in dict1[key]:
    dict1[key].append(value)
  
print(dict1)


# Write a Python program that takes a list of names and creates a dictionary where each name is the key and the length of the name is the value.


names = ["Tom", "Jennifer", "Ali", "Chris"]
result={}
for i in names:
  result[i]=len(i)
print(result)

# {'Tom': 3, 'Jennifer': 8, 'Ali': 3, 'Chris': 5}




# Question:
# You are given a messy text containing phone numbers in different formats.
# Extract all valid 10-digit phone numbers and store them in a dictionary with the last 4 digits as the key and the full number as the value.


import re
text = "Call 9876543210 or 987-654-3210. Alternate: (91234 56780)"
res={}
search=re.findall(r"\d+\s\d+|\d{10}", text)
for i in search:
  key=i[-4:]
  res[key]=i
print(res)

# {'3210': '9876543210', '6780': '9123456780'}




# Question:
# You have a log file where each entry contains a date, user, and action.
# Extract the information and store it in a nested dictionary where the user is the key, and the value is another dictionary mapping dates → actions performed.

dict3={}
log = """
[2025-10-05] User: alice Action: login
[2025-10-05] User: bob Action: upload
[2025-10-06] User: alice Action: logout
"""
pattern2=re.findall(r"\[(\S+)\]\s+\S+\s+(\S+)\s+\S+\s+(\S+)", log)
print(pattern2)

for date, user, action in pattern2:
  if user not in dict3:
    dict3[user]={date:action}
  else:
    dict3[user].update({date:action})

print(dict3)

# {
#   'alice': {'2025-10-05': 'login', '2025-10-06': 'logout'},
#   'bob': {'2025-10-05': 'upload'}
# }



# Given a text of student marks in this format:
# "Alice: 89, Bob: 76, Charlie: 92, Alice: 95, Bob: 82",
# write a program to create a dictionary where each student's name is the key, and the average mark is the value.

input1="Alice: 89, Bob: 76, Charlie: 92, Alice: 95, Bob: 82"
pattern=re.findall(r"\w+", input1)
dict3={}
for i in range (0,len(pattern), 2):
  if pattern[i] not in dict3:
    dict3[pattern[i]]=[int(pattern[i+1])]
  else:
    dict3[pattern[i]].append(int(pattern[i+1]))
for key, value in dict3.items():
  dict3[key]=sum(value)/len(value)

print(dict3)

# {'Alice': 92.0, 'Bob': 79.0, 'Charlie': 92.0}

import re
log = """
[2025-10-01] Module: auth Time: 2.5s
[2025-10-01] Module: db Time: 1.8s
[2025-10-01] Module: auth Time: 3.1s
[2025-10-02] Module: db Time: 2.0s
"""
dict1 = {}
first = re.findall(r"\[(\S+)\]\s+Module:\s+(\S+)\s+Time:\s+(\d+\.\d+)s", log)

for date, work, time in first:
    time = float(time)  
    if date not in dict1:
        dict1[date] = {}
    if work not in dict1[date]:
        dict1[date][work] = []
    dict1[date][work].append(time)
for date in dict1:
    for work in dict1[date]:
        times = dict1[date][work]
        avg_time = sum(times) / len(times)
        dict1[date][work] = avg_time

print(dict1)


import re
text = "Alice(PERSON) works at Google(ORG) in California(LOC). Bob(PERSON) joined Amazon(ORG)."

match=re.findall(r"(\S+)\((\S+)\)", text)
print(match)
dict1={}
for value, key in match:
  if key not in dict1:
    dict1[key]=[]
  if value not in dict1[key]:
    dict1[key].append(value)
print(dict1)





# Given a system log file, extract all IP addresses and classify them as public or private, storing the results in a dictionary.

import re
log = """
Connected to 192.168.1.10
Request from 8.8.8.8
User 10.0.0.2 logged in
Contacted 172.16.0.5 and 203.0.113.45
"""

dict2={"private":[],
       "public":[]
       }

match3=re.findall(r"\S+\d+", log)
print(match3)
for i in match3:
  if i not in dict2 and (i[0:2]==str(10) or i[0:3]==str(192) or i[0:3]==str(172)):

    dict2['private'].append(i)
  else:
    dict2['public'].append(i)
print(dict2)


{
  'private': ['192.168.1.10', '10.0.0.2', '172.16.0.5'],
  'public': ['8.8.8.8', '203.0.113.45']
}


# Question:
# Given a text of product reviews like this:
import re
str1="Laptop: ⭐⭐⭐⭐, Phone: ⭐⭐⭐, Laptop: ⭐⭐⭐⭐⭐, Tablet: ⭐⭐"

dict4={}
match2=re.findall(r"(\S+)\:\s(\S+\⭐)",str1)
print(match2)
for i, j in match2:
  if i not in dict4:
    dict4[i]=[len(j)]
  else:
    dict4[i].append(len(j))

for k, l in dict4.items():
  dict4[k]=sum(l)/len(l)
print(dict4)



{'Laptop': 4.5, 'Phone': 3.0, 'Tablet': 2.0}


# **************************Day-05********************************************88

# Question 1:
# Create a dictionary that stores the ASCII value of each character in a given string.

text = "Code"
dict1={}
for i in text:
  if i in dict1:
    continue
  else:
    dict1[i]=ord(i)
print(dict1)

{'C': 67, 'o': 111, 'd': 100, 'e': 101}


#🟡 Level: Medium (Regex + Dictionary)

# Question 2:
# You are given a text that contains dates in various formats.
# Extract all valid dates and store them in a dictionary with their index as the key and the date string as the value.

import re
text = "Meetings are on 2025-10-06, 10/07/2025, and 08-Nov-2025."
dict2={}
search1=re.findall(r"\S+\d+", text)
print(search1)
num=0
for i in range(len(search1)):
  dict2.update({num:search1[i]})
  num+=1
print(dict2)



# 🔴 Level: Hard (Regex + Dictionary Aggregation)

# Question 3:
# Extract domain names from a text of email addresses and count how many times each domain appears.

import re
dict3={}
text = "mike@gmail.com, anna@yahoo.com, bob@gmail.com, tom@outlook.com, jane@yahoo.com"
search2=re.findall(r"\S+\@(\S+)", text, re.MULTILINE)
print(search2)
for i in search2:
  print(i)
  if i in dict3:
    dict3[i]+=1
  else:
    dict3[i]=1

print(dict3)

{'gmail.com': 2, 'yahoo.com': 2, 'outlook.com': 1}



# 🔴 Level: Hard (Nested Dictionary + Regex)

# Question 4:
# You are given logs of students and their scores in various subjects.
# Extract data and store it in a nested dictionary where the key is the student name and the value is another dictionary of subject: score.

import re
log = """
Student: Alice Subject: Math Score: 89
Student: Bob Subject: Physics Score: 76
Student: Alice Subject: English Score: 92
"""

search3=re.findall(r"\S+\s+(\S+)\s+\S+\s+(\S+)\s+\S+\s+(\S+)", log)
print(search3)
dict4={}
for i, j, k in search3:
  if i not in dict4:
    dict4[i]={}
  dict4[i][j]=k

print(dict4)

# 🔴 Level: Hard (Regex Data Grouping + Dictionary of Lists)

# Question 5:
# Given a chat log containing messages with usernames and timestamps, extract each user and the messages they sent in a dictionary format.

import re
chat = """
[10:01] Alice: Hi Bob!
[10:02] Bob: Hey Alice!
[10:03] Alice: How are you?
"""
dict4={}
search4=re.findall(r"\S+\s+(\S+)\:\s+(.+)", chat)
for i, j in search4:
  if i not in dict4:
    dict4[i]=[j]
  else:
    dict4[i].append(j)

print(dict4)

# {
#   'Alice': ['Hi Bob!', 'How are you?'],
#   'Bob': ['Hey Alice!']
# }

<<<<<<< HEAD
#  Question 1:
=======
**************************************Day-06****************************************************8888

 Question 1:
>>>>>>> 94b28085c89f0d6bf8b891a4d9f107491adcc7a5
# You are given a list of temperatures in Celsius.
# Write a program to convert them to Fahrenheit and store the results in a dictionary where key = Celsius value and value = Fahrenheit value.

temps = [0, 20, 37, 100]
dict1={}
for i in temps:
  dict1[i]=(i*9/5)+32
print(dict1)

{0: 32.0, 20: 68.0, 37: 98.6, 100: 212.0}


# 🟡 Level: Medium — Regex Mapping and Replacement

# Question 2:
# You are given a paragraph containing text-based emojis.
# Create a dictionary mapping each emoji symbol to its word meaning (like ":)" → "smile") using regex, then replace all emojis in the text with their meanings.
import re
text = "Hey :) How are you :( I missed you <3"
words=[]
s=text.split(" ")
for i in s:
  if i==":)":
    words.append("smile")
  elif i==":(":
    words.append("sad")
  elif i=="<3":
    words.append("love")
  else:
    words.append(i)
words=(" ").join(words)
dict2={}
search1=re.findall(r"\<\d|\:\(|\:\)", text)
for i in search1:
  if i==":)":
    dict2[i]="smile"
  elif i==":(":
    dict2[i]="sad"
  else:
    dict2[i]="love"

print(dict2)
print(words)


{':)': 'smile', ':(': 'sad', '<3': 'love'}
# Modified text: "Hey smile How are you sad I missed you love


# 🔴 Level: Hard — Regex + Dictionary Reverse Index

# Question 3:
# You are given a paragraph of text.
# Write a program to create a reverse index dictionary where:

# Each word (case-insensitive) is a key

# The value is a list of sentence numbers where the word appears

import re

text = "Python is great. I love Python programming. Great tools exist for Python."
search2 = re.split(r'\.\s*', text)
print(search2)
result = {}

i = 1
for j in search2:
    print(j)
    count = re.findall(r'\b\w+\b', j.lower())
    print(count)
    for key in count:
        if key not in result:
            result[key] = [i]
        elif i not in result[key]:
            result[key].append(i)
    i += 1

print(result)



{
  'python': [1, 2, 3],
  'is': [1],
  'great': [1, 3],
  'i': [2],
  'love': [2],
  'programming': [2],
  'tools': [3],
  'exist': [3],
  'for': [3]
}



# Question 4:
# Write a Python program that analyzes a server log file and categorizes log entries into a dictionary based on log level (INFO, ERROR, DEBUG, etc.).
import re
log = """
[INFO] System started
[DEBUG] Loading configuration
[ERROR] Connection failed
[INFO] Retrying connection
"""

search3=re.findall(r"\[(\S+)\]\s+(.*)", log)
print(search3)
result={}
for i, j in search3:
  if i not in result:
    result[i]=[j]
  else:
    result[i].append(j)
print(result)

{
  'INFO': ['System started', 'Retrying connection'],
  'DEBUG': ['Loading configuration'],
  'ERROR': ['Connection failed']
}


# ---

# 🔴 Level: Hard — Dictionary Merging + Regex Parsing

# Question 5:
# You are given two product data strings from different systems.
# Each contains product IDs and prices.
# Use regex to extract the data and merge into a single dictionary —
# if the same product appears in both, keep the average price.


import re
data1 = "ID101: $50, ID102: $75, ID103: $100"
data2 = "ID102: $65, ID104: $120, ID101: $55"
result5={}
search4=re.findall(r"(\S+)\:\s+\$(\d+)", data1)
search5=re.findall(r"(\S+)\:\s+\$(\d+)", data2)

for i, j in search4:
  if i not in result5:
    result5[i]=[int(j)]
  else:
    result5[i].append(int(j))

for i, j in search5:
  if i not in result5:
    result5[i]=[int(j)]
  else:
    result5[i].append(int(j))

for i, j in result5.items():
  result5[i]=sum(j)/len(j)
print(result5)


{
  'ID101': 52.5,
  'ID102': 70.0,
  'ID103': 100.0,
  'ID104': 120.0
}
<<<<<<< HEAD

# ion 1:

# Write a Python program that takes a list of fruits and their prices in two separate lists and combines them into a dictionary mapping fruit → price.

fruits = ["apple", "banana", "cherry"]
prices = [100, 40, 150]
dict1={}
for i  in range(len(fruits)):
  for j in range(len(prices)):
    dict1[fruits[i]]=prices[i]
    break
print(dict1)
# {'apple': 100, 'banana': 40, 'cherry': 150}

 

# 🟡 Medium (Regex Extraction + Dictionary)

# Question 2:

# Given a paragraph containing product names followed by IDs in brackets, extract all pairs and store them in a dictionary with product name as key and ID as value.

import re
text = "Laptop (P123), Mouse (P456), Keyboard (P789)"
search1=re.findall(r"(\S+)\s+\((\S+)\)", text)
dict2={}
for i, j in search1:
  dict2[i]=j
print(dict2)

{'Laptop': 'P123', 'Mouse': 'P456', 'Keyboard': 'P789'}



# 🔴 Hard (Regex + Data Grouping)

# Question 3:

# You have a set of system event logs.

# Extract all timestamps, usernames, and actions, and create a dictionary where each username maps to a list of tuples — each tuple containing timestamp and action.
import re
log = """

[2025-10-06 10:00] user=alice action=login

[2025-10-06 10:05] user=bob action=upload

[2025-10-06 10:15] user=alice action=logout

"""
search2=re.findall(r"\[(\S+\s+\S+)\]\s+\S+\=(\S+)\s+\S+\=(\S+)", log)
dict3={}
for i, j, k in search2:
  if j not in dict3:
    dict3[j]=[(i, k)]
  else:
    dict3[j].append((i, k))
print(dict3)

{

  'alice': [('2025-10-06 10:00', 'login'), ('2025-10-06 10:15', 'logout')],

  'bob': [('2025-10-06 10:05', 'upload')]

}

# 🔴 Hard (Regex + Dictionary Aggregation)

# Question 4:

# You are given survey results containing ratings per department.

# Extract each department and its numeric ratings, and compute the average rating per department using a dictionary.

import re
text = "HR: 4, IT: 5, HR: 3, Finance: 4, IT: 4"
search3=re.findall(r"(\S+)\:\s*(\d+)", text)
dict4={}
for i, j in search3:
  if i not in dict4:
    dict4[i]=[int(j)]
  else:
    dict4[i].append(int(j))
for i, j in dict4.items():
  dict4[i]=sum(j)/len(j)
print(dict4)
# {'HR': 3.5, 'IT': 4.5, 'Finance': 4.0}


# 🔴 Hard (Regex + Nested Dictionary)

# Question 5:

# Given a text containing employee details, extract the department, employee name, and salary, and store the information in a nested dictionary grouped by department.
import re
data = """

Dept: HR Name: Alice Salary: 50000

Dept: IT Name: Bob Salary: 60000

Dept: HR Name: Carol Salary: 52000

"""
search5=re.findall(r"\S+\s+(\S+)\s+\S+\s+(\S+)\s+\S+\s+(\d+)", data)
dict5={}
for i, j, k in search5:
  if i not in dict5:
    dict5[i]={j:k}
  else:
    dict5[i].update({j:k})
print(dict5)

# {

#   'HR': {'Alice': 50000, 'Carol': 52000},

#   'IT': {'Bob': 60000}

# }

# ******************************Day-07****************************************

# Create a class StudentRecord that takes a block of text containing student details.
# Use regex to extract student name, ID, and marks and store them in a dictionary as:
# {student_id: {"name": name, "marks": marks}}
import re
data = """
  ID: S101 Name: Alice Marks: 89
  ID: S102 Name: Bob Marks: 76
  ID: S103 Name: Carol Marks: 91
"""
class StudentRecord:
  def __init__(self, data):
    self.data=data

  def get_all(self):
    
    search=re.findall(r"\S+\s+(\S+)\s+\S+\s+(\S+)\s+\S+\s+(\d+)", data)
    dict1={}
    for i, j, k in search:
      if i not in dict1:
        dict1[i]={"name":j, "marks":k}
      else:
        dict1[i].update({"name":j, "marks":k})
    print(dict1)


record = StudentRecord(data)
record.get_all()

# {
#   'S101': {'name': 'Alice', 'marks': 89},
#   'S102': {'name': 'Bob', 'marks': 76},
#   'S103': {'name': 'Carol', 'marks': 91}
# }


# 🔴 Hard Question 2 — Class + Regex Log Analyzer

# Create a class LogAnalyzer that can parse a log file using regex.
# Each log entry contains a timestamp, level, and message.
# The class should store logs in a dictionary grouped by log level and provide methods:

import re
log = """
[2025-10-06 10:00] INFO Server started
[2025-10-06 10:05] ERROR Connection failed
[2025-10-06 10:10] INFO Retrying connection
[2025-10-06 10:12] DEBUG Retrying sequence
"""
dict2={}
class LogAnalyzer:
  def __init__(self, log):
    self.log=log
  
  def get_errors(self):
    search1=re.findall(r"^\S+\s+\S+\s+(\S+)", log, re.MULTILINE)
    for i in search1:
      if i in dict2:
        dict2[i]+=1
      else:
        dict2[i]=1
  
  def count_by_level(self):
    print(dict2)


log1=LogAnalyzer(log)
log1.get_errors()
log1.count_by_level()


# Expected Output:

{
  'INFO': 2,
  'ERROR': 1,
  'DEBUG': 1
}


# 🔴 Hard Question 3 — Class + Regex Validation + Dictionary

# Create a class UserValidator that reads user registration data from text and validates using regex.
# Each user record contains a username, email, and phone.
# The class should store valid users in a dictionary with username as key and (email, phone) as value.
# Invalid entries should be ignored.

# Example Input:
import re
dict3={}
data = """
Username: john Email: john@example.com Phone: 9876543210
Username: anna Email: anna@@example Phone: 12345
Username: mark Email: mark@gmail.com Phone: 9123456789
"""
class UserValidator:
  def __init__(self, data):
    self.data=data
  
  def valid(self):
    search=re.findall(r"^\S+\s+(\S+)\s+\S+\s+(\S+\@{1}\S+\.\S+)\s+\S+\s+(\d{10})", data, re.MULTILINE)
    for i, j, k in search:
      # if i not in dict3:
      dict3[i]=(j, k)
    return dict3

user=UserValidator(data)
print(user.valid())
    

# Expected Output:

# {
#   'john': ('john@example.com', '9876543210'),
#   'mark': ('mark@gmail.com', '9123456789')
# }


# 🔴 Hard Question 4 — Regex + Nested Dictionary Builder (Inventory System)

# You are given a text that represents a warehouse stock log.
# Each entry includes a category, item name, and quantity.
# Write a program (or class) to extract this information using regex and store it as a nested dictionary in the form {category: {item: quantity}}.

# Example Input:
import re
data = """
Category: Electronics Item: Laptop Qty: 10
Category: Electronics Item: Phone Qty: 25
Category: Furniture Item: Chair Qty: 15
Category: Furniture Item: Table Qty: 5
"""
dict4={}
class Shop:
  def __init__(self,data):
    self.data=data
  def stock(self):
    search=re.findall(r"\S+\s+(\S+)\s+\S+\s+(\S+)\s+\S+\s+(\d+)",data)
    for i, k, j in search:
      if i not in dict4:
        dict4[i]={k:j}
      else:
        dict4[i].update({k:j})
    print(dict4)

items=Shop(data)
items.stock()

# {
#   'Electronics': {'Laptop': 10, 'Phone': 25},
#   'Furniture': {'Chair': 15, 'Table': 5}
# }


# 🔴 Hard Question 5 — Class + Regex Log Summary Generator

# Create a class AccessLog that takes in a server access log text.
# Use regex to extract IP addresses, endpoints, and status codes, then:

# Store the results in a dictionary grouped by IP address.

# Add a method summary() that prints the count of requests per IP and the most common status code for that IP.


# Example Input:
import re

log = """
192.168.1.10 - GET /home 200
192.168.1.10 - POST /login 403
10.0.0.2 - GET /home 200
192.168.1.10 - GET /dashboard 200
"""

dict5 = {}

class Accesslog:
  def __init__(self, log):
    self.log = log

  def summary(self):
    search5 = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+-\s+\S+\s+(\/\S+)\s+(\d+)", self.log)

    for i, j, k in search5:
      if i not in dict5:
        dict5[i] = [{"endpoint": j, "status": int(k)}]
      else:
        dict5[i].append({"endpoint": j, "status": int(k)})

    print(dict5)

    for ip, records in dict5.items():
      status_list = [rec["status"] for rec in records]
      status_counts = {}
      for s in status_list:
        status_counts[s] = status_counts.get(s, 0) + 1
      most_common_status = max(status_counts, key=status_counts.get)
      print(f"{ip} → {len(records)} requests, Most common status: {most_common_status}")


obj = Accesslog(log)
obj.summary()

# {
#   '192.168.1.10': [
#       {'endpoint': '/home', 'status': 200},
#       {'endpoint': '/login', 'status': 403},
#       {'endpoint': '/dashboard', 'status': 200}
#   ],
#   '10.0.0.2': [
#       {'endpoint': '/home', 'status': 200}
#   ]
# }

# and

# Summary:
# 192.168.1.10 → 3 requests, Most common status: 200  
# 10.0.0.2 → 1 request, Most common status: 200

# *********************************(Day-09)*******************************

# Hard Question 1 — Class + Regex Template Engine

# Create a class TemplateEngine that replaces placeholders in a text using a dictionary of variables.
# Placeholders are written in double curly braces {{variable_name}}.
# Use regex to identify and replace them dynamically.

# Example Input:

# text = "Hello {{name}}, your order {{order_id}} will be delivered by {{date}}."
# data = {"name": "Ravi", "order_id": "A1023", "date": "2025-10-06"}

# Expected Output:

# "Hello Ravi, your order A1023 will be delivered by 2025-10Python', 'ML', ], }"

import re
class Change:
    def __init__(self, text):
        self.text = text
    def Parse(self, data):
        pattern = re.findall(r"\{\{(\w+)\}\}", self.text)
        res = self.text
        for key in pattern:
            if key in data:
                res = res.replace(f"{{{{{key}}}}}", str(data[key]))
        return res
text = "Hello {{name}}, your order {{order_id}} will be delivered by {{date}}."
data = {"name": "Ravi", "order_id": "A1023", "date": "2025-10-06"}
engine = Change(text)
print(engine.Parse(data))

# Expected Output:

{
  'name': 'Alice',
  'age': 25,
  'skills': ['Python', 'ML']
}

# ⚡ Hard Question 2 — Regex + Dictionary + File Metadata Parser

# You’re given multiple lines describing file details in a log.
# Each line contains a filename, extension, size (in KB), and modified date.
# Use regex to parse and store the data in a dictionary grouped by file extension.

# Example Input:
import re
data = """
file1.txt size:12KB modified:2025-10-05
report.pdf size:230KB modified:2025-09-30
notes.txt size:8KB modified:2025-10-06
image.png size:1024KB modified:2025-08-20
"""
pattern = re.findall(r"(\w+)\.(\w+)\s+\S+:(\d+)\S+\s+\S+:(\d{4}-\d{2}-\d{2})", data)
dic = {}
for i, j, k,l in pattern:
    if j not in dic:
        dic[j] = []
    dic[j].append({"name": i,"size": int(k),"modified": l})
print(dic)
# Expected Output:

{
  'txt': [{'name': 'file1', 'size': 12, 'modified': '2025-10-05'},
          {'name': 'notes', 'size': 8, 'modified': '2025-10-06'}],
  'pdf': [{'name': 'report', 'size': 230, 'modified': '2025-09-30'}],
  'png': [{'name': 'image', 'size': 1024, 'modified': '2025-08-20'}]
}

# ⚡ Hard Question 3 — Class + Nested Dictionary + Regex Config Loader

# Write a class ConfigParser that reads configuration data formatted like:

# [Database]
# host=localhost
# port=5432
# [Server]
# debug=True
# port=8000

# Use regex to extract section headers ([Section]) and key-value pairs.
# Store the data as a nested dictionary, e.g.

# {
#   'Database': {'host': 'localhost', 'port': '5432'},
#   'Server': {'debug': 'True', 'port': '8000'}
# }

# Add a method get(section, key) that retrieves a specific configuration value.


import re
class ConfigParser:
    def __init__(self, data):
        self.data = data
        pattern = re.findall(r'\[(\S+)\]\s+(\S+)\=(\S+)\s+(\S+)\=(\S+)', data)
        self.pattern = pattern
        self.dic = {}
        for section, host, i, port, j in pattern:
            self.dic[section] ={host: i,port: j}
    def get(self, section, key):
        return self.dic.get(section, {}).get(key)
data = """
[Database]
host=localhost
port=5432
[Server]
debug=True
port=8000
"""
cfg = ConfigParser(data)
print(cfg.dic)
print(cfg.get("Database", "host"))
print(cfg.get("Server", "port"))



# ⚡ Hard Question 4 — Class + Regex + Dictionary Merging

# Create two dictionaries from separate text logs using regex extraction,
# then merge them intelligently based on a shared key (user_id).
# The class DataMerger should handle conflicts by choosing the latest timestamp entry.

# Example Input:
import re
class DataMerger:
    def __init__(self, log1, log2):
        self.log1 = log1
        self.log2 = log2

    def merge(self):
        data = {}
        logs = self.log1 + "\n" + self.log2
        pattern = r"user:(\d+)(?:\s+name:(\w+))?(?:\s+age:(\d+))?\s+time:(\d{2}:\d{2})"
        matches = re.findall(pattern, logs)
        for i, j, k, l in matches:
            if i not in data:
                data[i] = {}
            if j:
                data[i]['name'] = j
            if k:
                data[i]['age'] = int(k)
            if 'time' not in data[i] or l > data[i]['time']:
                data[i]['time'] = l

        return data
log1 = """
user:101 name:Ravi time:10:00
user:102 name:Kumar time:10:10
"""
log2 = """
user:101 age:30 time:10:05
user:102 age:28 time:09:50
"""
dm = DataMerger(log1, log2)
print(dm.merge())

# ⚡ Hard Question 5 — Regex-Based JSON Cleaner (Class Implementation)

# Write a class JSONSanitizer that takes a messy string containing pseudo-JSON data
# and uses regex to clean it up into a valid JSON-like dictionary.
# The input may contain extra spaces, single quotes, or trailing commas.

# Example Input:
import re
import json

class JSONSanitizer:
    def __init__(self, text):
        self.text = text
    def clean(self):
        t = self.text
        t = re.sub(r"'", '"',t)
        t = re.sub(r",\s*([}\]])", r"\1", t)
        return json.loads(t)
text = "{ 'name': 'Alice', 'age': 25, 'skills': ['Python', 'ML', ], }"
sanitizer = JSONSanitizer(text)
print(sanitizer.clean())
# Expected Output:

{
  'name': 'Alice',
  'age': 25,
  'skills': ['Python', 'ML']
}



# **********************************Day-10*********************************

# Hard Question 1 — Class Inheritance + Regex Log Routing System

# Design a base class BaseLogParser that defines a method parse_line(line) (to be overridden).
# Create subclasses ErrorLogParser, InfoLogParser, and DebugLogParser — each uses a different regex to extract data.
# Finally, write a LogRouter class that routes each log line to the correct subclass based on the log level and returns a combined dictionary of parsed data.

# Example Input:
import re

class BaseLogParser:
    def parse_line(self, line):
        pass
class ErrorLogParser(BaseLogParser):
    def parse_line(self, line):
        m = re.match(r"\[(.*?)\]\s*ERROR\s*(.*)", line)
        if m:
            return {'timestamp': m.group(1), 'msg': m.group(2)}
class InfoLogParser(BaseLogParser):
    def parse_line(self, line):
        m = re.match(r"\[(.*?)\]\s*INFO\s*(.*)", line)
        if m:
            return {'timestamp': m.group(1), 'msg': m.group(2)}


class DebugLogParser(BaseLogParser):
    def parse_line(self, line):
        m = re.match(r"\[(.*?)\]\s*DEBUG\s*(.*)", line)
        if m:
            return {'timestamp': m.group(1), 'msg': m.group(2)}
class LogRouter:
    def __init__(self):
        self.parsers = {
            'ERROR': ErrorLogParser(),
            'INFO': InfoLogParser(),
            'DEBUG': DebugLogParser()
        }

    def route_logs(self, logs):
        result = {}
        for line in logs:
            for level, parser in self.parsers.items():
                if level in line:
                    data = parser.parse_line(line)
                    if data:
                        result.setdefault(level, []).append(data)
                    break
        return result

logs = [
    "[2025-10-06 09:10] ERROR Disk full at /var/log",
    "[2025-10-06 09:12] INFO Backup started",
    "[2025-10-06 09:14] DEBUG Checking permissions"
]

router = LogRouter()
print(router.route_logs(logs))



# Expected Output:

{
  'ERROR': [{'timestamp': '2025-10-06 09:10', 'msg': 'Disk full at /var/log'}],
  'INFO': [{'timestamp': '2025-10-06 09:12', 'msg': 'Backup started'}],
  'DEBUG': [{'timestamp': '2025-10-06 09:14', 'msg': 'Checking permissions'}]
}


# ---

# ⚔️ Hard Question 2 — Class + Regex Data Extraction + Transformation

# Create a class TransactionAnalyzer that reads a multiline string of transactions with varying formats (use regex to normalize).
# Then aggregate them by user_id in a dictionary.

# Example Input:

import re
class TransactionAnalyzer:
    def __init__(self,data):
        pattern= re.findall(r'\S+[-=:]\s*(\d+).*?[\$ ](\d+(?:\.\d+)?).*?(?:on|date\=)\s*(\d{4}[-/]\d{2}[-/]\d{2})',data)
        self.pattern=pattern
    def parser(self):
        dic = {}
        for i, amount, k in self.pattern:
            amount = float(amount)
            if i not in dic:
                dic[i] = {'total': 0.00, 'transactions': 0}
            dic[i]['total'] += round(amount,2)
            dic[i]['transactions'] += 1
        return dic
data = """
user-101: paid $45.60 on 2025/10/06
user=102 amount 120.00 date=2025-10-05
user:103 paid 60.5 on 2025-10-04
user=101 paid $10.40 on 2025-10-06
"""
d=TransactionAnalyzer(data)
print(d.parser())

# Expected Output:

# {
#   '101': {'total': 56.00, 'transactions': 2},
#   '102': {'total': 120.00, 'transactions': 1},
#   '103': {'total': 60.50, 'transactions': 1}
# }


# ---

# ⚔️ Hard Question 3 — Class + Regex Pattern Inheritance + Validation System

# Build a class hierarchy for input validation using regex:

# BaseValidator → defines an abstract method validate(value)

# EmailValidator, PhoneValidator, and PasswordValidator → each implements regex-based validation
# Then write a class UserInputChecker that takes a dictionary of inputs and validates each using the correct subclass.


# Example Input:
import re
class EmailValidator:
    def validate(self, value):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, value))
class PhoneValidator:
    def validate(self, value):
        pattern = r'^(?:\+?\d{1,3})?\d{10}$'
        return bool(re.match(pattern, value))
class PasswordValidator:
    def validate(self, value):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return bool(re.match(pattern, value))
class UserInputChecker:
    def __init__(self):
        self.validators = {
            'email': EmailValidator(),
            'phone': PhoneValidator(),
            'password': PasswordValidator()
        }
    def check_inputs(self, inputs):
        dic= {}
        for key, value in inputs.items():
            if key in self.validators:
                dic[key] = self.validators[key].validate(value)
            else:
                dic[key] = False
        return dic
inputs = {
    "email": "user@example.com",
    "phone": "+919876543210",
    "password": "Pass@123"
}

checker = UserInputChecker()
print(checker.check_inputs(inputs))


# Expected Output:

# {
#   'email': True,
#   'phone': True,
#   'password': True
# }


# ---

# ⚔️ Hard Question 4 — Regex + Dictionary-Based Dependency Graph

# Given a text describing module dependencies,
# use regex to extract relationships and build a dependency graph dictionary
# where keys are modules and values are lists of dependencies.

# Example Input:
import re

text = """
ModuleA depends on ModuleB, ModuleC
ModuleB depends on ModuleD
ModuleC depends on ModuleE, ModuleF
ModuleD depends on None
ModuleE depends on None
ModuleF depends on None
"""
pattern=re.findall(r"(\w+)\s+depends\s+on\s+(.*)",text)
d={}
for i,j in pattern:
    if i not in d:
        d[i]=[]
    if j!="None":
        for k in j.split(","):
            d[i].append(k)
print(d)


# Expected Output:

# {
#   'ModuleA': ['ModuleB', 'ModuleC'],
#   'ModuleB': ['ModuleD'],
#   'ModuleC': ['ModuleE', 'ModuleF'],
#   'ModuleD': [],
#   'ModuleE': [],
#   'ModuleF': []
# }


# ---

# ⚔️ Hard Question 5 — Class Composition + Regex Report Generator

# Create a class ReportBuilder that uses composition with another class RegexExtractor.
# RegexExtractor extracts dates, amounts, and IDs from text using regex.
# ReportBuilder organizes the extracted info into a summary dictionary and generates a formatted string report.

# Example Input:

import re

class RegexExtractor:
    def __init__(self, text):
        self.text = text
class ReportBuilder:
    def __init__(self, text):
        self.extractor = RegexExtractor(text)

    def build_summary(self):
        summary = {}
        pattern = r"Transaction ID:\s*(\w+)\s*\|\s*Date:\s*(\d{4}-\d{2}-\d{2})\s*\|\s*Amount:\s*\$([\d.]+)"
        for txn_id, date, amount in re.findall(pattern, self.extractor.text):
            amount = float(amount)
            if date not in summary:
                summary[date] = []
            summary[date].append({'id': txn_id, 'amount': amount})
        return summary

    def generate_report(self):
        summary = self.build_summary()
        lines = []
        for date, txns in summary.items():
            total = sum(txn['amount'] for txn in txns)
            lines.append(f"Date: {date} → Total: {total:.2f}")
        return "\n".join(lines)
data = """
Transaction ID: TXN101 | Date: 2025-10-06 | Amount: $450.75
Transaction ID: TXN102 | Date: 2025-10-07 | Amount: $320.00
Transaction ID: TXN103 | Date: 2025-10-07 | Amount: $100.50
"""

builder = ReportBuilder(data)

summary = builder.build_summary()
print(summary)

print(builder.generate_report())

# Expected Output:

# {
#   '2025-10-06': [{'id': 'TXN101', 'amount': 450.75}],
#   '2025-10-07': [
#       {'id': 'TXN102', 'amount': 320.00},
#       {'id': 'TXN103', 'amount': 100.50}
#   ]
# }

# and a report like:

# Date: 2025-10-06 → Total: 450.75
# Date: 2025-10-07 → Total: 420.50



# ****************************************Day - 11 *************************************8
#  Medium (Level 1) — Regex + Dictionary Formatter

# Write a program that extracts name, age, and city from a messy multiline text and stores it in a list of dictionaries.
import re
data = """
Name: John, Age=25; City-London
Name=Alice; Age:30 City:NewYork
City:Paris Name=Mike Age=22
"""
name=re.findall(r'Name[:=]\s*(\S+)',data)
print(name)
age=re.findall(r'Age[:=]\s*(\d+)',data)
print(age)
city=re.findall(r'City[-:=>]\s*(\S+)',data)
print(city)

result=[]
for name, age, city in zip(name, age, city):
    result.append({'name': name, 'age': int(age), 'city': city})
print(result)

# expected_output
[
  {'name': 'John', 'age': 25, 'city': 'London'},
  {'name': 'Alice', 'age': 30, 'city': 'NewYork'},
  {'name': 'Mike', 'age': 22, 'city': 'Paris'}
]



# 🔵 Hard (Level 2) — Class + Regex-Based Resume Parser

# Create a class ResumeParser that takes raw resume text and extracts:

# Name

# Email

# Phone number

# Skills list (comma-separated)


# Store each resume as a dictionary entry using the person’s name as the key.

# Example Input:
import re
data = """
Name: Ravi Kumar
Email: ravi.k@example.com
Phone: +919876543210
Skills: Python, Automation, Networking

Name: Priya Sharma
Email: priya.s@gmail.com
Phone: 9123456789
Skills: Data Analysis, SQL, Tableau
"""
class ResumeParser:
    def __init__(self, data):
        self.raw_text = data

    def parse(self):
        pattern=re.compile(r"Name: (.+)\n"r"Email: (.+)\n"r"Phone: (.+)\n"r"Skills: (.+)",re.MULTILINE)
        match=pattern.findall(data)
        result={}
        for name, email, phone, skills in match:
            skills_list=[skill.strip() for skill in skills.split(',')]
            result[name] = {
                'email': email,
                'phone': phone,
                'skills': skills_list
            }
        return result
parser = ResumeParser(data)
result = parser.parse()
print(result)
# Expected Output:

# {
#   'Ravi Kumar': {
#       'email': 'ravi.k@example.com',
#       'phone': '+919876543210',
#       'skills': ['Python', 'Automation', 'Networking']
#   },
#   'Priya Sharma': {
#       'email': 'priya.s@gmail.com',
#       'phone': '9123456789',
#       'skills': ['Data Analysis', 'SQL', 'Tableau']
#   }
# }


# ---

# 🔴 Very Hard (Level 3) — Inheritance + Regex + Dataclass Log Correlator

# Build a log correlation system using OOP and regex.
# Base class BaseLog defines structure using @dataclass with timestamp, level, and message.
# Subclasses SystemLog, AppLog, and SecurityLog each parse a different log format using regex.
# A LogCorrelator class merges parsed logs by timestamp into a dictionary timeline.


# Example Input:

# system_log = """
# [2025-10-06 09:10] SYSTEM: Boot completed
# [2025-10-06 09:12] SYSTEM: Network up
# """

# app_log = """
# 2025/10/06 09:10 - APP - Started main service
# 2025/10/06 09:13 - APP - Request received
# """

# security_log = """
# (2025-10-06 09:12) SECURITY ALERT: User login successful
# (2025-10-06 09:15) SECURITY ALERT: Unauthorized access attempt
# """

# Expected Output:

# {
#   '2025-10-06 09:10': [
#       {'source': 'SYSTEM', 'msg': 'Boot completed'},
#       {'source': 'APP', 'msg': 'Started main service'}
#   ],
#   '2025-10-06 09:12': [
#       {'source': 'SYSTEM', 'msg': 'Network up'},
#       {'source': 'SECURITY', 'msg': 'User login successful'}
#   ],
#   '2025-10-06 09:13': [{'source': 'APP', 'msg': 'Request received'}],
#   '2025-10-06 09:15': [{'source': 'SECURITY', 'msg': 'Unauthorized access attempt'}]
# }


# ---

# 🔴 Very Hard (Level 4) — Dynamic Regex Class Compiler

# Write a class PatternCompiler that:
# 1. Accepts a dictionary of pattern names → regex expressions.
# 2. Dynamically creates methods at runtime for each pattern name.
# 3. Each generated method should return all matches from a given text.

import re
class PatternCompiler:
    def __init__(self, patterns):
        self._patterns = patterns
        for name, pattern in patterns.items():
            def make_method(pat):
                def method(text):
                    return re.findall(pat, text)
                return method
            setattr(self, name, make_method(pattern))
patterns = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phones": r"\+?\d{10,12}",
    "dates": r"\d{4}-\d{2}-\d{2}"
}
compiler = PatternCompiler(patterns)
text = "Contact us at admin@mail.com or +919812345678 by 2025-10-06."
print(compiler.emails(text))
print(compiler.phones(text))
print(compiler.dates(text))


# Expected Output (when calling methods):

# compiler.emails(text) → ['admin@mail.com']
# compiler.phones(text) → ['+919812345678']
# compiler.dates(text) → ['2025-10-06']

# Hard Question 1 — Class + Regex + Multi-Level Dictionary (Access Control Parser)

# Create a class AccessControl that parses a text-based permission list and organizes it into a nested dictionary
# of {role: {user: [permissions]}}. Use regex to extract fields.

# Example Input:
import re
data = """
Role: Admin | User: Alice | Permissions: Read, Write, Delete
Role: User | User: Bob | Permissions: Read
Role: Moderator | User: Charlie | Permissions: Read, Write
Role: Admin | User: Dave | Permissions: Write, Delete
"""
dict1={}
class AccessControl:
  def __init__(self, data):
    self.data=data
  def res(self):
    pattern=re.findall(r"\S+\s+(\S+)\s+\|\s+\S+\s+(\S+)\s+\|\s+\S+\s+(.*)", data, re.MULTILINE)
    for i, j, k in pattern:
      if i not in dict1:
        dict1[i]={j:[k]}
      else:
        dict1[i].update({j:[k]})
    return dict1

obj1=AccessControl(data)
print(obj1.res())
# Expected Output:

{
  'Admin': {
    'Alice': ['Read', 'Write', 'Delete'],
    'Dave': ['Write', 'Delete']
  },
  'User': {'Bob': ['Read']},
  'Moderator': {'Charlie': ['Read', 'Write']}
}


# ---

# ⚔️ Hard Question 2 — Class + Regex + Dynamic Grouping (Invoice Summarizer)

# You are given invoice details in text format.
# Build a class InvoiceSummarizer that:
# 1. Extracts Invoice ID, Customer Name, and Amount using regex.
# 2. Groups all invoices by Customer Name in a dictionary.
# 3. Provides a method total_by_customer() that returns each customer’s total billed amount.

# Example Input:
import re
data = """
Invoice: INV001 | Name: John | Amount: $250.50
Invoice: INV002 | Name: Alice | Amount: $300.00
Invoice: INV003 | Name: John | Amount: $120.75
"""
dict2={}
class InvoiceSummarizer:

  def __init__(self, data):
    self.data=data
  def total_by_customer(self):
    pattern=re.findall(r"\S+\s+(\S+)\s+\|\s+\S+\s+(\S+)\s+\|\s+\S+\s+\$(\S+)", data, re.MULTILINE)
    for i, j, k in pattern:
      if j not in dict2:
        dict2[j]={"invoices":[i], "total":float(k)}
      else:
        dict2[j]["invoices"].append(i)
        dict2[j]["total"]+=float(k)
    print(dict2)
obj2=InvoiceSummarizer(data)
obj2.total_by_customer()

# Expected Output:

# {
#   'John': {'invoices': ['INV001', 'INV003'], 'total': 371.25},
#   'Alice': {'invoices': ['INV002'], 'total': 300.00}
# }


# ---

# ⚔️ Hard Question 3 — Class + Regex Pattern Dispatcher (Custom Command Interpreter)

# Create a class CommandInterpreter that reads input lines representing shell-like commands
# and uses regex to identify command types and store execution metadata in a dictionary.
# Each command has one of these forms:
# The class should categorize commands by action and record their arguments.

import re
data="""
COPY source.txt destination/
MOVE file1.txt folderA/
DELETE temp.log
"""
dict3={}
class CommandInterpreter:
  def __init__(self, data):
    self.data=data
  
  def commands(self):
    pattern=re.findall(r"(\S+)\s+(\S+\.\S+)(?:\s+(.+))?", data, re.MULTILINE)
    for i, j, k in pattern:
      if i=="DELETE":
        dict3[i]=[{"file":j}]
      else:
        dict3[i]=[{"src":j, "dest":k}]
    print(dict3)
obj3=CommandInterpreter(data)
obj3.commands()
# Expected Output:

# {
#   'COPY': [{'src': 'source.txt', 'dest': 'destination/'}],
#   'MOVE': [{'src': 'file1.txt', 'dest': 'folderA/'}],
#   'DELETE': [{'file': 'temp.log'}]
# }


# ---

# ⚔️ Hard Question 4 — Regex + Class + Data Linking (Employee Hierarchy Builder)

# Given a company hierarchy text, create a class HierarchyBuilder
# that uses regex to build a manager–employee dictionary tree.

# Example Input:
import re
data = """
Manager: Alice -> Employees: Bob, Carol
Manager: Bob -> Employees: David, Emma
Manager: Carol -> Employees: Frank
"""
dict4 = {}

class Company:
    def __init__(self, data):
        self.data = data

    def managers(self):
        pattern = re.findall(r"\S+\s+(\S+)\s+\S+\s+\S+\s+(.+)", self.data)

        connection = {}
        for manager, employees in pattern:
            emp_list = [e.strip().strip(',') for e in employees.split()]
            connection[manager] = emp_list

        print(connection)

        for manager, emps in connection.items():
            if manager not in dict4:
                dict4[manager] = {}
            for emp in emps:
                dict4[manager][emp] = {}

        for manager in list(dict4.keys()):
            if manager not in dict4:
                continue
            for emp in list(dict4[manager].keys()):
                if emp in dict4:
                    dict4[manager][emp] = dict4[emp]
                    del dict4[emp]

        print(dict4)

obj4 = Company(data)
obj4.managers()


# Expected Output:

{
  'Alice': {
    'Bob': {'David': {}, 'Emma': {}},
    'Carol': {'Frank': {}}
  }
}

# (Nested structure: each manager key holds sub-dictionaries of their team.)


# ---

# ⚔️ Hard Question 5 — Class + Regex Validation + Custom Exception Handling

# Create a class FormValidator that validates a set of form entries from text.
# Each entry includes name, email, and phone.
# Use regex validation and raise a custom InvalidDataError for incorrect records.
# Store valid entries in a dictionary {name: {'email': ..., 'phone': ...}}.

# Example Input:

import re
class InvalidDataError(Exception):
    pass
class FormValidator:
    def __init__(self, data):
        self.data = data
        self.valid_entries = {}

    def validate(self):
        pattern = r"Name:\s*(\S+)\s*\|\s*Email:\s*([\w\.\@\+]+)\s*\|\s*Phone:\s*([\+\d]+)"
        entries = re.findall(pattern, self.data)
        e_pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
        p_pattern = re.compile(r"^(?:\+\d{12}|\d{10})$")

        for name, email, phone in entries:
            if not e_pattern.match(email) or not p_pattern.match(phone):
                raise InvalidDataError(f"Invalid email or phone for entry: {name}")
            self.valid_entries[name] = {'email': email, 'phone': phone}

        return self.valid_entries
data = """ 
Name: Ravi | Email: ravi@mail.com | Phone: 9876543210 
Name: Priya | Email: priya@@gmail | Phone: 999999 
Name: Arjun | Email: arjun.k@gmail.com | Phone: +919812345678
"""
try:
    validator = FormValidator(data)
    result = validator.validate()
    print(result)
except InvalidDataError as e:
    print(e)

# Expected Output:

# {
#   'Ravi': {'email': 'ravi@mail.com', 'phone': '9876543210'},
#   'Arjun': {'email': 'arjun.k@gmail.com', 'phone': '+919812345678'}
# }

# and raise an exception message for the invalid entry:
# InvalidDataError: Invalid email or phone for entry: Priya
