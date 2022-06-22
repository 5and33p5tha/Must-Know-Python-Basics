# Python runs on interpreter whereas C was on Compiler. As it is Interpreter, we need to signify the type as .py at the end as extension
# Generally, Interpreters are faster than compilers.
# Programming languages like JavaScript, Python, Ruby use interpreters. Programming languages like C, C++, Java use compilers.

# set are unordered collection of unique elements i.e all items should be unique.
# set can be constructed by using set() function
# In sets, collection is unordered but result i.e while printing, it shows in order if single digit and unordered in case of multiple digit

# Defining set
xyz = set()  # Defining set
# To add to set, we use add() method
xyz.add(1)
print(xyz)
# Now, same element only shows once i.e
# xyz.add(1) #Even if this is done, as 1 already exists, it will only add it once
# But
xyz.add(2)  # As two is another unique item, it is added
print(xyz)


mylist = [1, 5, 3, 2, 1, 1, 7, 5, 9, 0]
a = set(mylist)  # Defining a as set that has mylist as collection
# This will show in order as set and then show only unique values i.e will show {0,1,2,3,5,7,9}
print(a)
# Will not repeat any elements

# Note, in Python, we can redeclare any variable All we have to note is that we cannot set python defined terms as variable like we cannot set print as variable
# We can do
a = [1, 2, 3, 4]
print(a)
# AND THEN again
a = [10, 20, 30, 40]
print(a)
# But
mylist = [70, 90, 69, 53, 45, 47, 20, 70]
b = set(mylist)
print(b)  # This will not repeat value but as it is multiple digit/character, it will be in unordered format


# Boolean
# Will Show True Or False
print(1 < 7)  # Will print True
print(7 < 1)  # Will print False
