# a function is a useful feature that groups together a set of statements
# It is so that they can run more than once. They can also let us specify the parameters that can serve as input to function

# Functions in any program is not the primary program, it is secondary part that is called when needed.
# Example:- create = function to create a new order, Delete functions, etc

# Functions do not run on its own but run only when they are set to
# For example, a delete function set when clicking a delete button will let us call delete function

# Normally, while learning, we write values in the function but this is not a good practice, GENERALLY, THE SANDARD RULE IS WE NEED TO PASS THE VALUES TO A FUNCTION VIA PARAMETERS

# While defining a function, a paranthesis is a must

# IN Basic Python, GERERALLY WE WRITE HAVE TO DEFINE OUR FUNCTION BEFORE CALLING, IT BASICALLY HAS TO BE DEFINED ANYWHERE BUT SHOULD BE BEFORE CALLING


# Basic Syntax:-
# To define a function,
# def function_name():
#    ...statement...
# call the function
# function_name()


# Defining a function
def demoFunction():
    print("Hello World!")


# Calling a function
demoFunction()
# HERE, We first defined the function and then it will run when Called


# IN PyScript, WE CANNOT USE THE ABOVE METHOD TO PRINT DIRECTLY, WE NEED TO CALL USING RETURN TYPE AS THE ABOVE METHOD MAY NOT EXECUTE IN SOME CASES
# AS IN MOST CASES, WE NEED THE OUTPUTS TO BE SOMEWHERE SO IT IS A MUST TO USE THE RETURN TYPE.SOMETIMES, WE HAVE TO PASS THE VALUE OF A VARIABLE TO ANOTHER VARIABLE. HENCE THE FOLLOWING METHOD IS PREFERRED
# using return type
# Initially, defining a function


# result = add_num()
# print('The addition of 5 and 20 is',result)
# The above line shows that add_num() is not defined. Hence we should first define it as:-

def add_num():
    return 5+20  # WE USE RETURN SO THAT WHILE CALLING, WE CAN STORE THIS VALUE IN A VARIABLE
# GENERALLY, WE USE return so that we can have the ability to store the outputs


 # Now calling the function
result = add_num()
print('The addition of 5 and 20 is ', result)

# ARGUMENTS AND PARAMETERS


# Here, first_value and second_value are parameters. To be more clear, parameters = variables
def multiply_num(first_value, second_value):
    return first_value*second_value
# As parameters is used, this function can be reused


# Function Call With Argument
total = multiply_num(5, 4)  # Here, 5 and 4 are arguments
print('the multiplication is ', total)


# As we have used parameters, we can reuse the same function and pass another argument as:
total = multiply_num(10, 20)  # Here, 5 and 4 are arguments
print('the multiplication is ', total)
