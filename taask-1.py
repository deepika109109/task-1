1.# Delete a list of keys from a dictionary
# sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
# # Keys to remove
# keys = ["name", "salary"]

sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
for x in keys:
 sample_dict.pop(x)
print(sample_dict)

output:{'age': 25, 'city': 'New york'}

# 2.Count the frequency of each character in a given string using a dictionary

x='strings'
c={}
for i in x:
  if i not in c:
    c[i]=1 
else:
    c[i]+=1
print(c)

output:{'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}

# 3.Swap keys and values in a dictionary.

q={'a':1,'b':2,'c':3,'d':4}
tem={}
for a,b in q.items():
 tem[b]=a
print(tem)

output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# output:{'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}

# # 4.Write a program to sum all the values in a dictionary.

# a={'s': 45, 't': 140, 'r': 25, 'i': 50}
# sum=0
# for i in a.values():
#     sum+=i
# print(sum)

output:260

# # 5.Create a nested dictionary for student details (name, roll, marks).
    
res=[]
for i in range(2):
    tem={}
    tem['name']=input('enter name:')
    tem['roll']=input('enter roll:')
    tem['marks']=input('enter marks:')
    res.append(tem)
print(res)

output:enter name:deepika
enter roll:405
enter marks:75
enter name:pavan
enter roll:409
enter marks:60
[{'name': 'deepika', 'roll': '405', 'marks': '75'}, {'name': 'pavan', 'roll': '409', 'marks': '60'}]

# 6.Convert a dictionary to a list of tuples.

d={'name': 'deepika', 'roll': '405', 'marks': '75'}
for x in d.items():
  print(x)

output:('name', 'deepika')
('roll', '405')
('marks', '75')

# 7.Write a program to store names as keys and their lengths as values.

k=['deepika','lavanya','thriveni']
tem={}
for x in k:
 tem[x]=len(x)

print(tem) 

# output:{'deepika': 7, 'lavanya': 7, 'thriveni': 8}

# 8.Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and "odd" if the number is odd

v={}
for x in range(1,6):
    if x%2==0:
        v[x]="even"
    else:
        v[x]="odd"
print(v)

output:{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

# 9.Create Reverse Word Dictionary
# Given list of words: words = ["cat", "dog", "bat"]
# Create a dictionary with words as keys and their reversed strings as values

k=["cat", "dog", "bat"]
x={}
for i in k:
    x[i]=i[::-1]
print(x)

output:{'cat': 'tac', 'dog': 'god', 'bat': 'tab'}