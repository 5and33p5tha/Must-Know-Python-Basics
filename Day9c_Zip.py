my_list = [1, 2, 3, 4, 5]
my_list2 = ['a', 'b', 'c', 'd', 'e', 'f']

x = list(zip(my_list, my_list2))
# ZIP PUTS EVERYTHING TOGETER. IT JOINS TWO VALUES OF MY_LIST AND MY_LIST2 AND JOINS THEM UNTILL COMMON NUMBER OF ELEMENTS
print(x)  # AS THERE IS UNCOMMON NUMBER OF ELEMENTS, THE LAST ELEMENT OF MY_LIST2 IS SKIPPED I.E F IS NEGLECTED


my_list = (1, 2, 3, 4, 5)
my_list2 = ('a', 'b', 'c', 'd', 'e', 'f')
# Here, item1 will hold values of my_list and item2 will hold values of my_list2
for item1, item2 in zip(my_list, my_list2):
    print('For this tuple, the first element is {} and the second element is {}'.format(
        item1, item2))  # AS THERE IS UNCOMMON NUMBER OF ELEMENTS, THE LAST ELEMENT OF MY_LIST2 IS SKIPPED I.E F IS NEGLECTED
