# Map function here is similar to that is JavaScript except for definition part
# Map is used to define for all elements in an array (list or tuple in python)

# Program 1

def square(abc):
    return abc**2  # Here, ** means power and **2 = power 2


numbers = [2, 4, 6, 8, 10]
# testresult = map(square, numbers) #Here map is a function like in JS and square is another function inside map.
# As square is another function inside the function map(), it should not have any parenthesis
# As result is not shown, we perform typecasting into list
testresult = list(map(square, numbers))
print(testresult)

# Always remember to use standard practice of naming different variables

# In above programming, we can use
# def square (numbers):
#   return numbers**2
# AND WRITE SAME numbers below as well as
#numbers = [2, 4, 6, 8, 10]
#testresult = list(map(square, numbers))
# print(testresult)

# Notice Same numbers in function definition and work defined below

# BUT TRY NOT TO DO SO AS WE HAVE TO USE ARGUMENTS AND PARENTHESIS AS THIS IS STANDARD PRACTICE


# Program 2

def splice(mynames):
    if len(mynames) % 2 == 0:  # Here, len is used to count the length of the string in python
        # return (mynames," has Even Characters")

        # To show only even
        return (mynames)
    else:
        # return (mynames, " has Odd Characters")

        # To print only first character if odd
        return ("odd ", mynames[0])


names = ['Yogesh', 'Yanzi', 'Ganesh', 'Shiva', 'Rojust', 'Sachin']
# Typecasting into list as list(map(splice, names))  , Here, splice is our custom named variable
newlist = list(map(splice, names))
print(newlist)
