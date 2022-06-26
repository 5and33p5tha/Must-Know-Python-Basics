# Python runs on interpreter whereas C was on Compiler. As it is Interpreter, we need to signify the type as .py at the end as extension
# Generally, Interpreters are faster than compilers# Generally, Interpreters are faster than compiler in case of analyzing the codes but slower when executing the program.
# Programming languages like JavaScript, Python, Ruby use interpreters. Programming languages like C, C++, Java use compilers.

# Nested List -> List Inside a List
list1 = [5, 10, 15, 20]
list2 = [2, 3, 7, 9]
list3 = [40, 50, 60, 70]

matrix = [list1, list2, list3]
# As list inside a list is an matrix, hence we have named the variable as matrix here

print(matrix)  # To print all matrix

# To print specific data of matrix, we use multiple indexing
# This will print 15 from matrix[0] which is list1 and list1[2] which is 15
print(matrix[0][2])
# In Python, to go inside something of smething, we use [something1][something2]. In JS, we did something1.something2
