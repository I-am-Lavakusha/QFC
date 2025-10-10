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