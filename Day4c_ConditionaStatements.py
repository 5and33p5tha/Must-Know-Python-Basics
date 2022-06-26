# Python runs on interpreter whereas C was on Compiler. As it is Interpreter, we need to signify the type as .py at the end as extension
# Generally, Interpreters are faster than compiler in case of analyzing the codes but slower when executing the program
# Programming languages like JavaScript, Python, Ruby use interpreters. Programming languages like C, C++, Java use compilers.

# WHILE WRITING CONDITIONAL STATEMENTS, WE SHOWULD MATCH THE EXACT INDENTATION I.E EXACT FORMAT
# AS WE DO NOT HAVE ANY CURLY BRACES{} OR ANY BRACES WHILE CHECKING THE STATEMENTS, WE HAVE TO MATCH THE EXACT FORMAT

# Program to check odd or even
x = 15
if x % 2 == 0:
    # THIS print should be a line or two away from the if statement and should be in another line, It can or cannot match the other print spacings
    print('even number')
# This else should be in exact same line (Vertical line) below the if case
else:
    print('odd number')

# Program to check leap year
year = 2022
# We cannot use && , || in python. Instead we have to write and , or directly
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    # Conditions:- MUST CONDITION IS (any year divided by 4 should give 0 AND any year divided by 100 should not give 0) and OPTIONAL CONDITION HERE IS any year divided by 400 = 0
    # i.e 5 = mod i.e modulus that checks remainders. If mod == 0 i.e exactly equals to 0 and mod 100!=0, it is a leap year  ALSO, if mod 400 ==0, it is also a leap year
    print('leap year')
else:
    print('not a leap year')
