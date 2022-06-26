# Python runs on interpreter whereas C was on Compiler. As it is Interpreter, we need to signify the type as .py at the end as extension
# Generally, Interpreters are faster than compiler in case of analyzing the codes but slower when executing the program
# Programming languages like JavaScript, Python, Ruby use interpreters. Programming languages like C, C++, Java use compilers.

# Elif = elseif statement in python programming
x = 20

if x < 0:
    print("Number is negative")
elif x > 0:
    print("Number is positive")
else:
    print("Value is zero")


x = 10
y = 20

if x < y:
    print("Y is greater than X")
elif x > y:
    print("X is greater than Y")
else:
    print("They are equal")


# To take user input
# Here, to take input, we write input. Int is written as the user input is always string, so Int converts string into integer
a = int(input("Enter the value of a : "))
# Just to take input, we can write
#a = input("ljdfllasfjl")
b = int(input("Enter the value of b : "))

if a > b:
    print(a, 'is greater')
    # Can also write     print(f'{a} is greater')
elif b > a:
    print(f'{b} is greater')
    # Instead, we can also write print(f'{b} is greater')
else:
    print(f"{a} and {b} are equal")
