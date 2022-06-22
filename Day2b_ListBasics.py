# Python runs on interpreter whereas C was on Compiler. As it is Interpreter, we need to signify the type as .py at the end as extension
# Generally, Interpreters are faster than compilers.
# Programming languages like JavaScript, Python, Ruby use interpreters. Programming languages like C, C++, Java use compilers.

# list are similar to array in other programming languages and list are mutable i.e elements inside list can be changed
fruits = ["apple", "mango", "litchi", "grapes", "papaya"]
print(fruits)

# indexing
print(fruits[0])  # as at 0 index, we have apple, so this will print apple

# To Print from certain index to certain index
# UNLIKE OTHER, HERE IT WILL SHOW ANYTHING FROM ONE END TO OTHER END
# I.E FOR PRINT(FRUIT[2:4]) IT WILL PRINT FROM 2 I.E LITCHI AND EVERYTHING BETWEEN 2 AND 4, 4 IS PAPAYA AND THIS WILL EXCLUDE 4
print(fruits[0:])  # this will print all the elements from 0 index to end
print(fruits[0:3])  # this will print all the elements from 0 index to 3 index
print(fruits[2:4])  # this will print all the elements from 2 index to 4 index

# WE CAN DO ALL INDEXING SIMILARLY TO AS IN STRING INDEXING IN Day2a_string.py

# append() = to add new elements in te list
# By default, this will add it to last as in any array
fruits.append("orange")
print(fruits)


# pop() = to remove last element from list, By default, this wil remove it from the last element and to remove element from specific portion, we use indexing i.e pop(0)
fruits.pop()
print(fruits)

# To remove from specific position
fruits.pop(2)  # i.e remove litchi
print(fruits)


# len() = to count the number of elements in the list
print(len(fruits))  # Count the length of the list
