'''
Hello everyone and welcome to another python 3 basics video. In this video we
will be discussing the basics of a function.

The idea of a function is to assign a set of code, and possibly variables,
known as parameters, to a single bit of text. You can think of it a lot like
why you choose to write and save a program, rather than writing out the
entire program every time you want to execute it.
'''

# To begin a function, the keyword 'def' is used to notify
# python of the impending function definition, which is what def
# stands for.

# from there, you type out the name you want to call your function.
# it is important to choose a unique name, and also one that wont conflict
# with any other functions you might be using. For example, you wouldn't
# want to go calling your function print. 


# so here we've called our function example. After the name of the function,
# you specify any parameters of that function within the parenthesis
# parameters act as variables within the function, they are not necessary
# to create a function, so first let's just do this without any parameters. 

def example():
    # functions just run whatever code is encased with them.
    print('this code will run')
    z = 3 + 9
    print(z)

# now if we just run this, we see nothing happens. We have to actually call
# this function to execute, because all we've done so far is just define the
# function and what it does. To run it, you can either type out the function in
# the console like so:

# or you can add it to the actual script itself:

example()

