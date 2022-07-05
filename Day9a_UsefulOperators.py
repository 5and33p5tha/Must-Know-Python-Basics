# MIN AND MAX
from random import shuffle  # To import shuffle
from random import randint
import imp


my_list = [10, 12, 5, 9, 22, 30, 4, 8, 15]
print(min(my_list))  # WILL PRINT MINIMUM AMONG THE GIVEN VALUES
print(max(my_list))  # WILL PRINT MAXIMUM AMONG THE GIVEN VALUES


# RANDOM
# Will shuffle my_list EVERYTIME WE PRINT, NEW ORDER OFF MY_LIST IS PRINTED AS THE VALUES IS SHUFFLED
shuffle(my_list)
print(my_list)  # Will print shuffled my_list, EVERYTIME WE PRINT, NEW ORDER OF MY_LIST IS PRINTED AS THE VALUES IS SHUFFLED


# Printing random integer
print(randint(0, 100))  # Random integer is printed between 0 and 100


# IN OPERATOR
demo = 'x' in ['x', 'y', 'z', 'hello']
print(demo)  # Will Print TRUE as x exists

demo = 'a' in ['x', 'y', 'z', 'hello']
print(demo)  # Will Print FALSE as a does not exists


# NOT IN
demo_list = ['x', 'y', 'z', 'hello']
result = 'y' not in demo_list
print(result)  # Will Print FALSE as y exists

demo_list = ['x', 'y', 'z', 'hello']
result = 'b' not in demo_list
print(result)  # Will Print TRUE as b does not exists
