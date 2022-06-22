# Python runs on interpreter whereas C was on Compiler. As it is Interpreter, we need to signify the type as .py at the end as extension
# Generally, Interpreters are faster than compilers.
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
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('leap year')
else:
    print('not a leap year')
