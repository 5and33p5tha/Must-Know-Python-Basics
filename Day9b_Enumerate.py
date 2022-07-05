# Enumerate is useful in showing what value is in what place
for i, letter in enumerate('abcdef'):
    # .format will signify placeholder i in first {} and letter in second {}
    print("At index {} we have the letter is {}".format(i, letter))
    # The above is new method to read variable, .format will signify placeholder i in first {} and letter in second {}
    # Enumerate means it automatically sets what is where i.e what element is in which position

x = list(enumerate('abcdef'))

# Optionally,
print(x)  # If we print x, we get multiple tuples.
