'''
So now that you know how to write and append files, we can learn how
to read from files! 
'''

# similar syntax as you've seen, 'r' for read. You can just throw a .read() at
# the end, and you get:
readMe = open('exampleFile.txt','r').read()
print(readMe)


'''
Now that is great and useful, but a lot of times people want to read by line.
There are a few things you can do here, but probably the easiest is to:
'''

# this will instead read the file into a python list. 
readMe = open('exampleFile.txt','r').readlines()
print(readMe)

