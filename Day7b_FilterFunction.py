# The filter funtion returns an ITERATOR yeilding those items of iterable for which  function (item) is true.
# This means we need to filter by a function that returns either true or false

# BASICALLY, THE USE OF FILTER FUNCTION IS TO FILTER


# defining the function check_even for calling
# As we will be passing values to this parameter from below arguments, WE CANNOT WRITE THE SAME NAME AS BELOW.
def check_even(xyz):
    return xyz % 2 == 0


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Here, filter is a function and check_even is another function inside the function filter but it does not need parenthesis AND WE ARE NOT ALLOWED TO DO SO ASWELL
newlist = list(filter(check_even, nums))

# Here, we have stored the return of above defined function check_even in variable newlist

# Here, list is TYPECASTING i.e converting all to list, similarly we can perform typecasting for INT, etc

print(newlist)
