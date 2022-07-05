# **kwargs -> Builds a dictionary of key/value pairs

def my_Function(**kwargs):
    if 'fruit' in kwargs:  # Here, this 'fruit becomes the key pair
        print(f"my favourite fruit is {kwargs['fruit']}")
        # Here, f is like .format, IN PYTHON WE HAVE MULTIPLE WAYS TO PUT THE VALUE IN VARIABLE
    else:
        print("Not a Fruit")


# ALL 'fruit' in if, inside kwargs[] and here, should match with each other
# Normally, fruit here is a variable but after passing this as argument as **kwargs, it becomes a key
my_Function(fruit='apple')
# Here, apple is the value pair of the key pair fruit


def fnc(**kwargs):
    if 'vegan' in kwargs:
        print('The diet for a vegan is arguably the {}'.format(
            kwargs['vegan']))
    else:
        print(f"Oh, so you're not vegan, then try some {kwargs['omnivore']}")
        # The above (f"...{kwargs[""]}") and the top ("...{}".format(kwargs[""])) are only some of unique ways to index values in the variable in python


fnc(vegan="Tofu", omnivore="Steak")
