# For single statements, we can keep the return in same line aswell
def square(num): return num**2


result = square(2)  # Storing the value of square with argument as 2 as value
print(result)

# LAMBDA IS JUST THE OPTIONAL TO FUNCTION
# Normally, use lambda for short programs but generally use function instead
# process, just add function name = lambda something: expression
# No return statements needed here


# CONVERTING INTO LAMBDA EXPRESSION
# cube = lambda xyz: xyz**2
cube = lambda xyz: xyz**2  # This is shortcut for function definition
# process, just add function name = lambda something: expression
# No return statements needed here


# Here, the xyz is the parameter and the 3 in cube(3) is the arguments which passes the value 3 to the parameter xyz
result = cube(3)
print(result)


# Program using lambda
#evnnum = lambda abc: abc % 2 == 0
evnnum = lambda abc: abc % 2 == 0
# Here, abc is the parameter and numbers is the arguments which pass the value to parameter


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenlist = list(filter(evnnum, numbers))
print(evenlist)
