# Inheritance is to form a new class from the class that has been already defined.
# The newely formed classes are caled derived classes, the classes that we derive from are called base classes
# The derive class override or extends the functionality of base class.
# Basically, inheritance means that the subclass are created from the parent class and subclass can use the functions of the parent class


class Animal:
    # AS THE PROPERTY OR METHOD BELONG TO A CLASS, TO SHOW THIS, WE USE (self)
    # HENCE WE CAN SEE self IN MULTIPLE CASES BELOW
    # In other programming language, we had this, In Python IT IS self
    # The following def __init__(self) is not a method but a function

    # WE CAN SKIP THIS DEF __INIT__(SELF) COMPLETELY ASWELL AS WE DO NOT NEED THIS COMPULSORILY
    # __INIT__ ONLY IS WRITTEN IN A CODE IF WE WANT SOMETHING TO RUN AUTOMATICALLY
    def __init__(self):
        # Above def __init__(self)  Signifies a function that is called automatically whenever class Animal is called or MORE SPECIFICALLY, WHENEVER THE INSTANCE OF ANIMAL IS CALLED OR WORKED ON.
        print("Animal class created")

    # Now Creating a method
    # Any function that is created inside any class is called Method
    def WhoIs(self):
        print('Animal')

    # Defining another method
    def eat(self):
        print('Animal Who Eats')


# nOTE:- NEW CLASS SHOULD BE IN A NEW OUTSIDE INDENTATION. AS LONG AS IT IS INSIDE, IT WILL BELONG TO THE CLOSEST CLASS AND HENCE SHOW ERROR
# Now Creating a child class
# If done in C, we used the keyword extends but here it is simple.
class Dog(Animal):
    # Here, (Animal) after class Dog signifies that it is a child class
    # THE FOLLOWING PRINTS THE PROPERTY OF PARENT CLASS ASWELL AND THEN PRINTS ITS CODE

    # nOTE:- THIS  DEF __INIT__(SELF CAN BE SKIPPED AS WELL) WE DO NEED COMPULSORILY NEED THE INIT PORTION IN CLASS
    def __init__(self):

        # __INIT__ ONLY IS WRITTEN IN A CODE IF WE WANT SOMETHING TO RUN AUTOMATICALLY

        # THE FOLLOWING IS JUST TO PRINT THE INIT OF THE PARENT CLASS AND NOTHING MORE
        Animal.__init__(self)  # To take the init of the parent class animal.
        # The above line helps to inherit the property of the parent class
        print('Dog Class Created')

    # NOW TO OVERRIDE THE METHOD OF A PARENT CLASS (NOT THE DEF __init__(self) BUT OTHER METHODS)
    # WE ARE OVERRIDING THE OUTPUT OF DEF WHOIS(SELF)

    def WhoIs(self):
        # This changed the print of WhoIs() from   print('Animal') to the one written here
        print('Animal Type Dog')

    def speak(self):
        print('Dog Barks')


a = Animal()  # Here, x is the instance of Animal.
print(a)

# Calling a method
a.WhoIs()  # Since it print directly AND HAVE NOT ASSIGNED ATTRIBUTE, we can directly call the function

# To Print Child Class
b = Dog()  # B is instance of Dog().
print(b)  # As We have print in our function, we can print the function itself


# To Print The New Over-Written Method of parent class
b.WhoIs()

# EXTEND: i.e print eat of parent class from child class- This is done as:-
b.eat()


# EVEN CHILD CLASS CAN CREATE A NEW METHOD. THIS IS POSSIBLE AS DEFINING NEW FUNCTION IN CHILD CLASS
b.speak()
