'''
Alright, so now we get to appending a file in python. I will just state again
that writing will clear the file and write to it just the data you specify in
the write operation. Appending will simply take what was already there, and add
to it.

That said, when you actually go to add to the file, you will still use
.write... you only specify that you will be appending instead of writing
when you open the file and specify your intentions.

'''


# so here, generally it can be a good idea to start with a newline, since
# otherwise it will append data on the same line as the file left off.
# you might want that, but I'll use a new line.
# another option used is to first append just a simple newline
# then append what you want. 
appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()

