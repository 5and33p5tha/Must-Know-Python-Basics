# Python runs on interpreter whereas C was on Compiler. As it is Interpreter, we need to signify the type as .py at the end as extension
# Generally, Interpreters are faster than compilers.
# Programming languages like JavaScript, Python, Ruby use interpreters. Programming languages like C, C++, Java use compilers.

# Note:- In python, wee can always re-define a variable

text = "welcome to Dursikshya Education Network Pvt Ltd Python Programming Class"
print(text)

# To count the number of character in a string
# String may or maynot have spaces in between
# Sting may be anything inputable a keyboard i.e. may be number, special character, etc
# By Default, everything is string IN ANY PROGRAMMING LANGUAGE, ESPECIALLY IF INPUT BY USER WITHOUT DEFINING THE DATATYPE
print(len(text))

# STRING INDEXING (note:-This Starts from zero and always counts each letter/number/alphabet
print(text[0])

# To Print from certain index to certain index
# i.e print from index 0 to index 9 i.e Start from zero and print 10 items from that position
print(text[0:10])
# OR, we can do
print(text[:10])


# To Print all values, we can do
print(text[:])

# Similarly, to print all values from 5, we can do
print(text[5:])


# Basic String built in methods
# upper() - make uppercase
# lower() - make lowercase
# split() - split from every word and make a list i.e array in terms of python
# In python, list is array
print(text.upper())
print(text.lower())
print(text.split())
# All of THIS PRINT WORKS WITH LIST ASWELL

# formatting with placeholders
# Here, % is a placeholder to be formatted and s is string
print('we are here to learn %s programming' % 'python')
# %s as we have string in the placeholder
# This will replace %s with 'python'

# Now for double place holders
print('we are here to learn %s programming at %s' % ('python', 'Dursikshya'))
