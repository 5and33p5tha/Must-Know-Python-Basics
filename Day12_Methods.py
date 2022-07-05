# Methods are function defined inside the body of class. They are used
# to perform operations with the attribute of our object. Method are key concept of
# OOP Paradigm. For Large applications, methods are essential.
# IN JS, Inbuilt functions were method. Here, any function defined within class is method

# Program to find area of circle without method

class Circle:
    # pass  #If no operation is done and only value is passed, we use pass
    pi = 3.14

    # Circle gets insantiated with a radius (default)
    # i.e as WE HAVE NOT SET THE RADIUS AND WE NEED TO PASS THE DEFAULT RADIUS, WE CAN PASS RADIUS AS DEFAULT I.E ANY VALUE FOR RADIUS AS:
    def __init__(self, radius=7):  # Here radius=7 means setting default for radius, Also, we have set default as no value is passed as argument aswell
        self.radius = radius
        # Here, pi is variable of class, so we cannot just take pi. Hence we need to use Class.variable_name i.e Circle.pi to take the value of pi of class Circle
        self.area = radius*radius*Circle.pi
# Whenever the object instance is created, init is called automatically


a = Circle()  # a is instance of class Circle, a is object
print("Area of Circle is ", a.area)


# Same Program to find area of circle using method

class Circle:
    # pass  #If no operation is done and only value is passed, we use pass
    pi = 3.14

    # Circle gets insantiated with a radius (default)
    # i.e as WE HAVE NOT SET THE RADIUS AND WE NEED TO PASS THE DEFAULT RADIUS, WE CAN PASS RADIUS AS DEFAULT I.E ANY VALUE FOR RADIUS AS:
    def __init__(self, radius=7):  # Here radius=7 means setting default for radius, Also, we have set default as no value is passed as argument aswell
        self.radius = radius
        # Here, pi is variable of class, so we cannot just take pi. Hence we need to use Class.variable_name i.e Circle.pi to take the value of pi of class Circle
        self.area = radius*radius*Circle.pi
# Whenever the object instance is created, init is called automatically

    # Now Method for resetting radius
# We must write this within class, as we are inside the class (known via indentation) we write it here
    def setRadius(self, newradius):
        self.radius = newradius
        # As this method is inside the class Circle, we keep self AS WE ARE ALREADY INSIDE THE CLASS
        self.area = newradius*newradius*self.pi

    def getCircumference(self):  # AS WE ALRADY HAVE RADIUS, WE ONLY USE SELF
        # AS WE HAVE ALL THE VALUES WE NEED ALREADY DEFINED, WE USE THIS
        return 2*self.pi*self.radius
    # AS WE HAVE USED RETURN, WE CAN NOW PRINT THE OUTPUT OF FUNCTION AS a.getCircumference()


a = Circle()  # a is instance of class Circle, a is object
print("Area of Circle is ", a.area)
a.setRadius(newradius=10)  # Passing value of newradius as 10 as an argument
print("The new radius is ", a.radius)
print("The new area is ", a.area)
# Here, a.getCircumference() as we have used return in getCircumference and hence we are printing the output
print("The Circumference is ", a.getCircumference())
