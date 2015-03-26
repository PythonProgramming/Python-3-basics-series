'''
Welcome to another python 3 basics video, in this video we're going to now
discuss the concept of global and local variables.

When users begin using functions, they can quickly become confused when it comes
to global and local variables... getting a the dreaded variable is not defined
even when they clearly see that it is... or so they think.

These terms of global and local
correspond to a variable's reach within a script or program.

A global variable is one that can be accessed anywhere

A local variable is the opposite, it can only be accessed within its frame.

The difference is that global variables can be accessed locally, but not modified
locally  inherently.

A local variable cannot be accessed globally, inherently.
Now, dont worry about committing
that to memory right now, I think it makes a lot more sense when you just
see and do it, so let's do that. 

'''
# this variable has no parent function, but is actually NOT a global variable.
# it just so happens that it is committed to memory before the function is called
# so we are able to iterate, or call it out, but we cannot do much else.

x = 6

def example():
    # z, however, is a local variable.  
    z = 5
    # this works
    print(z)
    
example()
# this does not, which often confuses people, because z has been defined
# and successfully even was called... the problem is that it is a local
# variable only, and you are attempting to access it globally.

print(z)

# next up is an example that i've seen cause even more trouble, and that's
# the attempt to play with a global variable locally. The reason why this
# is so troubling is because you can access it... you just cannot play
# with it, and this often frustrates people for a while.


x = 6

def example2():
    # works
    print(x)
    print(x+5)

    # but then what happens when we go to modify:
    x+=6

    # so there we attempted to take the x var and add 6 to it... but now
    # we are told that we cannot, as we're referencing the variable before
    # its assignment.

'''
So now you know the rules, what can we do about it?
'''
x = 6

def example3():
    # what we do here is defined x as a global variable. 
    global x
    # now we can:
    print(x)
    x+=5
    print(x)




'''
So that is all for global and local, though I will show 1 last thing.

Sometimes you want a sort of global variable as a starting point, but
you do not actually wish to modify the "global" variable outside of the
functions themselves. You can just do the following:
'''

def example4():
    globx = x
    # now we can:
    print(globx)
    globx+=5
    print(globx)


# and that's it!

# hopefully that will help some of you from pulling your hair out for 30 minutes
# trying to figure out what the heck is going on to reality. This is something
# that snagged me pretty good when i was starting out. 
