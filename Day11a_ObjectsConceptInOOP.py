# OOP -> Object Oriented Programming
# It is not compulsory that akk programming language has OOP
# OOP advantage is that it makes the program shorter and efficient but most work can be done using the function aswell hence, OOP is not compulsory
# In python, everything is an object i.e we use type() method to check the type of objects
# i.e In Python, List, Tuple, Str, Dict, etc are all objects

print(type(20))
# These are built in python features , as int, list ,etc all have a property, they are said to be an object
print(type([1, 2, 3, 4, 5]))

# Now To create own object, we need to use the class keyword
# After writing class, the first letter after that MUST START WITH A CAPITAL LETTER

# class: user defined objects are created using the class keyword The class is the
# blueprint that defined the nature of future objects. From classes, we can construct instances.
# An instance is a specified object created from a particular class. For example, above we have created the object list which was an
# instance of list object

# Lets create a new object type called Demo


class Demo:  # As word class is used, this is user defined object and the first letter of Demo should be capital, HENCE Demo
    pass  # Passing a value , Here we have only used pass that signifies passing a value but we can do much more


# instance of demo, i.e result of the class Demo needs to be passed in specific variable X which is called instance of demo
# As the class Demo cannot be used directly, we have to write instance of class [i.e calling Demo() in x but in OOP, DO NOT USED THE TERM CALLING BUT SAY INSTANCE]
x = Demo()  # Here x is object
# Will show <class '__main__.Demo'> , HERE main signifies this is user defined
print(type(x))

# In above class Demo, we only have pass here but we can also define various attributes and methods.
# attribute = It is a characteristics of an object
# method = It is an operator we can perform with the object

# Example: We can create a class called Dog. An attribute of a dog may be its breed pr its name, while a method of dog may be defined by .bark() method which returns the sound it makes
