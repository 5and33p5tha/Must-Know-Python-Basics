# To Open a file via python
my_file = open('Day10_Files.txt')  # By Default, this is in read mode
print(my_file)  # This print will just print the status of file

# Normally, WE CANNOT DIRECTLY READY THE CONTENTS OF THIS FILE
# SO, WE DO
print(my_file.read())  # This will read the contents of this files

# Now to Print From the particular position
# That is start from index 5. "Here, this  will show from "is the first..." skipping "this "
my_file.seek(5)
print(my_file.read())


# To Read From a Particular Line
my_file.seek(0)  # ) Signifies to read from 0 i.e the very beginning
print(my_file.readlines())

# Note:- \n = next line in python


# Now Writing To A File
# Open() -> Opening the file
# passing w+ = Lets us read and write to the file
# open('abc.txt', 'w+') = Will truncate the original file, i.e it will delete all the content which exists previously in the file

# Write Mode
# This will show w+ i.e write mode. THIS WILL REMOVE THE PREVIOUS CONTENTS ASWELL
op_file = open('Day10_Files.txt', 'w+')
# This W+ will only work once as to remove contents again, we need to use it again
print(op_file)

op_file.write('This is the FIRST line written using the write mode')
op_file.seek(0)
print(op_file.read())

# To add new line
op_file.write('\n This is the SECOND line written using the write mode')
op_file.seek(0)
print(op_file.read())

# Appending to this file
# ALTHOUGH HELLO.TXT IS NOT CREATED, THIS LINE WILL CREATE THE FILE NAMED DAY10_HELLO.TXT AUTOMATICALLY
newfile = open('Day10_Hello.txt', 'a+')
print(newfile)
newfile.write('This is written from Append Method')
newfile.seek(0)
print(newfile.read())

newfile.close()
# ALL OPENED FILES MUST BE CLOSED
# SOME OPENED FILES IN ABOVE ARE NOT CLOSED
