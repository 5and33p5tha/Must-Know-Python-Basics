# *args -> when a function parameter starts with asterik it allows for an arbitary number of arguments and a function them in tuple of values

# def myFunction(a,b,c,d,e):
#     return a+b+c+d+e

# THIS CAN BE DONE IN STANDARD METHOD AS
def myFunction(*args):   # here, *args or we can write *abcd or anuthing, it is BUILT IN PYTHON FUNCTION THAT ENABLES US TO REPLACE ALL THE PARAMETERS THAT IS TO MATCH WITH ARGUMENTS AS AUTOMATED, I.E IT WILL CREATE REQUIRED NUMBER OF PARAMETERS ON ITS OWN
    # We can write anything after * but the standard is args, we can even write *wxyz
    # Sum is the built in funtion of python that gives a+b+c+... pto given terms
    return sum(args)


x = myFunction(10, 25, 30, 50, 100)
print(x)
