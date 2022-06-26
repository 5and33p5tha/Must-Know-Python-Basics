# Python is a high level programming language
# High level programming = human readable
# Generally all programming languages are high level programming language
# Python Scope:-
# - Artificial Intelligence and Machine Learning
# - For Web = Django/Flask
# - For Data Science

# to check python version, type the following in command prompt or terminal
# for windows:- python --version
# for mac: python3 --version

# the extension for python is .py
# As this is high level language, it needs to be either compiled or interpreted to be machine readable
# Hence extensions are needed.
# In case of python, it runs via interpreter
# nterpreter translates just one statement of the program at a time into machine code. Compiler scans the entire program and translates the whole of it into machine code at once.
# Interpreters usually take less amount of time to analyze the source code. However, the overall execution time is comparatively slower than compilers. Compilers usually take a large amount of time to analyze the source code. However, the overall execution time is comparatively faster than interpreters.

# To Print String in python
print('initial hello world')  # Print string using single quotes
# Alternatively
print("hello world")  # Strings require quotes either single or double in python

# To Print Number in python
print(7)  # Numbers do not need any quotes

#To use comments, we use hashtag in python i.e #

# Variable is used to store value
# While defining a variable, we cannot use names of inbuilt punctions like print, we also cannot use space or start with a number or start with special characters
# For variable, we can use _ i.e underscore and that too after beginning with alphabet
# There are no let, const, var or anything in python, just basic common variable and that is it.

# defining a variable
x = 71  # Defining a variable
print(x)
# In python, we can redefine and redeclare the variables
# Hence, we can repeat x again and write x = 21

x = 99  # Defining value of x again for same variable
print(x)


# Arithmetic operators in Python
#   +, -, /, *, %, ** i.e power, // i.e floor division
# here, ** means power
#  floor division means while performing the division, remove the values after point in division

a = 20
b = 15
print(a/b)
# In Python, the indentation i.e the line should match
# if we print like the following, it will not work
# print(a/b), #As WE HAVE USED A SPACE HERE, THE LINE WHERE IT SHOULD START IS NO LONGER STARTING FROM THERE. HENCE IT DOES NOT WORK

# Using floor division
print(a//b)  # This will remove the point and everything after point


# type() , We USE TYPE TO DETERMINE THE DATA TYPES
print(type(a))  # Will show int i.e integer

print(type(2.5))  # Will show float

# Data Types in python
# int (For integer)
# float (For float)
# str (For String)
# list i.e array in python and we can modify it i.e mutable
# tuple i.e like array but we cannot modify it i.e immutable
# dict i.e in pythin, this is object
# set i.e  they are unordered collection of unique elements i.e all items sh
# bool i.e boolean i.e true/false

# Assignment Operator in Python
# Assignment operator i.e. assign values and ALSO< VALUE CHANGES
# x=10, 20, etc
# x+=y is same as x = x+y
# x-=y is same as x = x-y
# x*=y is same as x = x*y
# x/=y is same as x = x/y
# x//=y is same as x = x//y

x = 10  # This is variable declaration and also IS ASSIGNMENT OPERATOR AS X IS ASSIGNED THE VALUE 10
y = 5  # This is variable declaration and also IS ASSIGNMENT OPERATOR AS Y IS ASSIGNED THE VALUE 5
x += y
print(x)  # Will Show 15
# Working
# x = 10, y = 5
# x+=y i.e x = x+y i.e x = 10+5 i.e x = 15
# Final Value of x = 15
# Hence result = 15

x -= y
print(x)  # Will Show 10
# Here, final result is x = 15 and y = 5
# x = 15-5 =10
# Hence, new x = 10 and RESULT = 10

# Comparision operator in python
# < means something less than other thing (left -> right)
# > means something greater than other thing (left -> right)
# <= means something less than or equal to other thing (left -> right)
# >= means something greater than or equal to other thing (left -> right)
# == means something equals to another thing (left -> right)
# not equal to another thing (left -> right) i.e !=


# Logical operator in python
# or -> or       don't write||
# and -> and     don't write&&
# not -> !


# The Equality operator (==) is a comparison operator in Python that compare values of both the operands and checks for value equality. Whereas the ‘is’ operator is the  identity operator that checks whether both the operands refer to the same object or not (present in the same memory location).
