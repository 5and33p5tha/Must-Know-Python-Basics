# While Loop General format
# While test/condition
# code statement
# else
# final code statement

x = 0
while x < 20:
    # In python, we cannot write x++
    print('x is currently ', x)  # i.e print upto 19
    x += 1  # This means x++ i.e x=x+1
else:
    print('done')
# print (x)
#  If we print x again at the end, it will print x = 20
# THIS IS BECAUSE IN WHILE CONDITION, WE HAVE X +=1 AND THE CONDITION IS X<20
# x will be false only after x<20 i.e 20<20
# hence, final x after loop break is 20


#Break and  Continue
y = 1
while y < 10:
    print('y is currently', y)
    print('y is still less than 10, adding 1 to 10')
    y += 1

    if y == 5:
        print('y==5')
        break  # This will break the loop at the condition y reaches 5.
    # If break is not written, it will run till the loop y<10 i,e y=9
    else:
        print('continuing')
        continue  # In built PYTHON loop Functions, break and continue
    # Continue will run our loop till the condition y<10 or before break in if condition
