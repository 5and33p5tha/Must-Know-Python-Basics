# loop = iteration/repeatation

mylist = [2, 5, 9, 7, 12, 15, 18, 20]

for num in mylist:
    # This is like map in JS, here, the values of mylist is assigned in num
    # i.e, it creates a new variable called num where all the values of mylist is assigned
    # Instead of num, we can write anything.
    # Example for xyz in mylist
    print(num)
# This will print all the nubers

# Print only even numbers
for num in mylist:
    if num % 2 == 0:
        print(f'{num} is even')
    elif num % 2 != 0:
        print(num, 'is odd')
    else:
        print(num, 'Is Zero')


# to find the total sum of array
total_sum = 0
for num in mylist:
    total_sum += num
   # print(total_sum), This sum is considered inside the for loop. So This will show each sum among ongoing elements
# Instead, we print outside the loop just to print the final sum
print(total_sum)


# for loop for a string
text = "High Level Programming Language"
for letter in text:
    print(letter)
# This will separate each character one line at a time


# for loop for a tuple
fruits = ('mango', 'orange', 'apple', 'banana', 'cherry')
for healthy_snacks in fruits:
    print(healthy_snacks)  # This will print each element in each separate line


# for loop in dictionary
student = {"First_name": "Sandeep", 'Last_name': 'Shrestha',
           "Age": "24", "Citizen": "Nepali"}
for person in student.keys():
    print(person)  # This will print only the keys
    # By default, FOR DICTIONARY, IT WILL PRINT THE KEYS
# EXAMPLE
for person in student:
    print(person)  # By default, this will print the keys only

# To use for loop to print value only
for people in student.values():
    print(people)

# To use for loop to print both keys and values
for index, data in student.items():  # Here index and data are just our custom variable name, instead we can write x,y  a,z or any two variable name
    print(index, data)
