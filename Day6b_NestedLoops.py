color = ['red', 'green', 'orange', 'yellow']
fruits = ['mango', 'apple', 'litchi', 'cherry']

for looks in color:
    for name in fruits:
        print(looks, fruits)
# Concept here is that it is like a analogue clock. color is hour and fruits is minutes
# Starting with red, first it will show red ['mango', 'apple', 'litchi', 'cherry'] , then green ['mango', 'apple', 'litchi', 'cherry'] and so on.
# i.e untill red finishes all, green will not be displayed


# Range Function
for x in range(10):
    print(x)  # Will print Fron zero and print upto to terms i.e 0 1 2 ... 9

for y in range(10, 20):
    # Will print from 10 and one before 20 i.e 19, hence result it 10 11 12 ... 19
    print(y)
