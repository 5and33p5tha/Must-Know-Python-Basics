# Python runs on interpreter whereas C was on Compiler. As it is Interpreter, we need to signify the type as .py at the end as extension
# Generally, Interpreters are faster than compilers.
# Programming languages like JavaScript, Python, Ruby use interpreters. Programming languages like C, C++, Java use compilers.

# Tuples are rarely used
# Tuple = similar to list but immutable i.e tuble cannot be changed
# Tuple is defined in parenthesis i.e (), not []
fruits = ('mango', 'orange', 'apple', 'banana', 'cherry')
print(fruits)

# Indexing
print(fruits[0])

# All Indexing used in list can be used here
print(fruits[2:4])  # i.e will return 2 and everything before 4 i.e 2 and 3

print(fruits[0:])  # Will print all

print(fruits[2:])  # Will return  everything from 2 and afterwards


# len() = count the number of elements in tuple, i.e count each item, not each word or character
print(len(fruits))

# Basic tuple method

# .index('')
# .index = use .index to enter a value and then return its index
# .index('orange') will search for the index of orange in the tuple
print(fruits.index('orange'))
# If something does not exist in tuple, it shows not in tuple
# print(fruits.index('guava'))


# .count('')
# .count = use .count to enter a value and see how many times it has appeared in the tuple
print(fruits.count('apple'))

# If something does not exist in tuple it will show zero
print(fruits.count('guava'))  # Will Show Zero
