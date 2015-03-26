'''
Hello and welcome to another python 3 basics tutorial video.

In this video we're going to cover the basics of writing to a file.

It should be noted that there are two methods for saving data to a file, and
those are writing and appending. Writing to a file will write that bit
of data, whatever it is, solely, to the file. This means if there was anything
there before, it will be gone if you use write.

If you use append, then you will basically add to whatever is previously there.

I will be showing both methods, but write first. 
'''


# so here we have some simple text, but we also threw in a \n to
# denote a new line, this will start a newline in the file that we write to
text = 'Sample Text to Save\nNew line!'

# notifies Python that you are opening this file, with the intention to write
saveFile = open('exampleFile.txt','w')
# actually writes the information
saveFile.write(text)
# It is important to remember to actually close the file, otherwise it will
# hang for a while and could cause problems in your script
saveFile.close()


