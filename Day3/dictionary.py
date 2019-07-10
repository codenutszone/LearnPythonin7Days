###################################################################
# Note : python compiler checks indentation first then syntax and then variables
####################################################################

# Create a dictionary
dict = {'name': 'sohan', 'id': 200, 'place': 'pune'}

# Print dictionary
print(dict)

# Access value of any key by selecting key name in square bracket
print("{} is living in {}".format(dict['name'], dict['place']))

# Note : Don't access dictionary using slicing or indexing like dict[1:3] ,
# it will give type error: unhashable type slice

###################################################################
# Basic Operations on dictionary
###################################################################

# Find the number of key value pair in the dictionary using len() function
print('length of dictionary is  :', len(dict))

# Change the value of any key by directly assigning
dict['id'] = 300
print(dict)

# Insert new key-value pair in the dictionary
dict['dept'] = 'siebel admin'
print(dict)

# check the key is available in the dictionary or not using in or not in operator ,
# it will give you True or False output
if 'id' in dict:
    print("key is present in dictionary")
else:
    print("key is not present in dictionary")

# Delete key-value pair using del statement
del dict['id']
print(dict)

# Check key using not in operator
if 'id' not in dict:
    print("key is not present in dictionary")
else:
    print("key is  present in dictionary")

# No duplicate keys, if we enter the data with same key it will be override
# 1 unique keys
dict['name'] = 'mohan'
print(dict)

# Keys should be immutable type . If you try to use list as keys , it will throw error like Type error : unhashable type
dictionary = {['rahul', 'modi']: 'officer'}

# Delete whole dictionary using the del statement
dictionary = {}
print(type(dictionary))

del dictionary
print(dictionary)


#########################################################################
# Dictionary methods
#########################################################################

# clear() method will make the dictionary empty
dic = {'name': 'sohan', 'id': 200, 'place': 'pune'}
dic.clear()
print(dic)

# get() method will give the value of the provided input key
# if name not found in the dictionary it will return -1 ,
# if you dont specify anything it will return None by default

dic = {'name': 'sohan', 'id': 200, 'place': 'pune'}
print(dic.get('abc', -1))
print(dic.get('abc'))
print(dic.get('name'))

# Take the new dictionary as input and iterate it through loop
d = eval(input("please enter the input in the {}:"))

print("the new dictionary is :", d)
for i in d:
    print(i)

# Access the keys of the dictionary using keys() method
print(d.keys())

# Access valeus of the dictionary using values() method
print(d.values())

# Access both key-value pairs of dictionary in the list of tuple format
print(d.items())

# Note : it will store the keys ,values and key-values in the
# dict_keys,dict_values and dict_items objects respectively
# when we use above method to acccess the dictionary element

# Update() : you can update the new key-values or dictionary using update method,
# you need to pass a dictionary as input
dic = {'name': 'sohan', 'id': 200, 'place': 'pune'}
dic.update({'dept': 'python'})
print(dic)

#################################################################
# Program for player names and their scores
#################################################################
dic = {}

n = int(input("enter the number of element you want ot insert:"))
for i in range(n):
    k = input("enter the player name:")
    v = int(input("enter the score:"))
    dic.update({k: v})
print(dic)

search = input("enter the player name you want to search:")
if search in dic:
    print("player found")

runs = dic.get(search, -1)
if (runs == -1):
    print("player not found")
else:
    print("the score of the player is :", runs)
#################################################################
# use loops in dictionary
#################################################################
print(dic)
for k, v in dic.items():
    print("key is {} and values is {}".format(k, v))

for i in dic.keys():
    print("values is ", dic[i])
################################################################
# Program to count the number of letter in string
################################################################
dic = {}
str = "sohanmohan"
for i in str:
    dic[i] = dic.get(i, 0) + 1

print(dic)

################################################################
# converting list into dictionary ******Not working
################################################################
l1 = ['sohan', 'mohan', 'manju']
l2 = [1, 2, 3]

z = dict(zip(l1, l2))
print(z)
#################################################################
# Program to convert string into dictionary
# We are using split function to break the string into list and
# then convert it into dictionary using dict() function
################################################################
lst = []
str = "sohan=1,mohan=2,manju=3"
for x in str.split(","):
    print(x)
    y = x.split('=')
    lst.append(y)
print(lst)
d = dict(lst)
print(d)


################################################################
# Program to pass dictionary to funtions : in this program
# we are converting the values of the dictionary into int format
# created in the above program
################################################################
def f(d):
    for k, v in d.items():
        d[k] = int(v)
    print(d.items())


f(d)
###############################################################
# Program to create ordered dictionary
# In dictionary order is not maintained so we can use orderedDict class to
# create ordered dictionary
###############################################################
dic = {}
n = int(input("enter the number of element you want ot insert:"))
for i in range(n):
    k = input("enter the player name:")
    v = int(input("enter the score:"))
    dic.update({k: v})
print(dic)

# To create the ordered dictionary we use OrderedDict class from collection module
from collections import OrderedDict

newd = OrderedDict()
for k, v in dic.items():
    newd[k] = v

print(newd)

################################################################
# Program to sort the elements of dictionary using lambadas
################################################################
print(dic.items())
# Note : By default sorted function will sort on the basis of keys if you don't specify it
dicnew = sorted(dic.items())

print(dicnew)

# You can specify keys using key parameter with lambda expression

dicnew = sorted(dic.items(), key=lambda t: t[1])
print(dicnew)





