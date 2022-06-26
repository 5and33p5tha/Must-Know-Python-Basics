# Python runs on interpreter whereas C was on Compiler. As it is Interpreter, we need to signify the type as .py at the end as extension
# Generally, Interpreters are faster than compiler in case of analyzing the codes but slower when executing the program
# Programming languages like JavaScript, Python, Ruby use interpreters. Programming languages like C, C++, Java use compilers.

# Dictionary are object in python
# Dictionary is a collection of key-value pairs i.e they come in value pairs

student = {"First_name": "Sandeep", 'Last_name': 'Shrestha',
           "Age": "24", "Citizen": "Nepali"}
# Here the fist pary is key and the last part is value i.e
# Key are First_name, Last_name, etc
# Value are Sandeep, Shrestha, etc
# In Python, the object is defined inside {} and in "":"" or '':'' format i.e {"":""}. This is like JSON format in javascript

# To print object
print(student)
print(student["First_name"])  # can also write print(student['First_name'])

item = {'val1': 1, 'val2': [2, 5, 7, 11], 'val3': [10, 20, 30]}
print(item['val2'])

# To print specific item in an object that has array
print(item['val2'][2])  # This will print 7 of arraay val2 inside object item

# To Create a new dictionary
d = {}  # defining a dictionary named d
# value assigning in dictionary d i.e WILL PUT THIS INSIDE DICTIONARY D
d['fruits'] = 'apple'
# value assigning in dictionary d i.e WILL PUT THIS INSIDE DICTIONARY D
d['vegetables'] = 'potato'
print(d)


# NESTING DICTIONARY
nest_dict = {'key1': {'nestkey': {'subnestkey': 'finalvalue'}}}
# Here, subnestkey which has value "Finalvalue" is inside nestkey, which is inside key1
print(nest_dict['key1']['nestkey']['subnestkey'])
# In Python, to go inside something of smething, we use [something1][something2]. In JS, we did something1.something2

# Dictionary Method
# key() - It will only return the keys of the dictionary

print(student.keys())

# values() - It will only return the values of the dictionary

print(student.values())

# In python, we can re-define the variable. In following case i.e in dictionary, while defining, it may not be in order
a = {1, 3, 5, 7}
print(a)

# In following case i.e in dictionary, while defining, it may not be in order
a = {2, 4, 6, 8}
print(a)
