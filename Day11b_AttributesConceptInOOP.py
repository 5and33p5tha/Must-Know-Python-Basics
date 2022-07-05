# The syntax for creating an attribute is

# self.attribute = something

# There is a special method called:
# __init__()


# x = Dog(breed="German Shephard")  #AS DOG IS NOT DEFINED IT, WE HAVE TO DEFINE IT, SO BEFORE THIS, WE DO

class Dog:
    # Self signifies it will belong to same class, MUST KEEP SELF AS THIS IS COMPULSORY
    def __init__(self, breed):
        # self.breed = breed #CAN ALSO WRITE self.abc = breed
        # Instead of self, we can also write xyz.abc = breed BUT MOST TEXT EDITORS MAY NOT READ xyz is same as self SO BETTER WRITE self
        # self.abc = breed #This Also Works, BUT BETTER TO WRITE
        # nOTE, the breed after __init__(self,breed), self.abc = breed  and below Dog(breed = ...); ALL breed MUST MATCH ie NAME AS WELL AS SPELLING SHOULD BE THE SAME
        self.breed = breed


x = Dog(breed="German Shephard")
print(x)  # Will show <__main__.Dog object at 0x1029f2fb0> BUT THIS IS NOT THE TRUE OUTPUT AS WE STILL DO NOT HAVE BREED PRINTED

# __init__(): This is a special method which is called automatically right after the object has been created.
# This Means
# While  x = Dog [This Dog is class] is called, the functions set to the class Dog is called automatically
# i.e here,
# def __init__(self, breed):
#self.breed = breed
# This is called automatically via __init__() method. BUT WE NEED TO WRITE __init__() first.


# def __init__(self, breed)
# Each attribute in a class definition begins with a reference to the instance of object, by convention named self
# This breed is an argument. The argument value is passed during class instantation self.breed= breed


# We created instance of Dog class and we can access the attribute from class like this
# This will show the output German Shephard and is our true output.
print(x.breed)
# Here, print(x.breed), the breed here is the bree of self.breed
# IF WE HAD WRITTEN self.abc then in print, we should write print(x.abc)
