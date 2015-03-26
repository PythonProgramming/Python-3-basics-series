'''
Welcome to another python 3 basics video, in this video we will carryon with
functions. In the last video you were shown a very basic function, without
any parameters

In this video, lets include a parameter, and give this function more...
functionality. 
'''


# changed name to simple math, to better describe our intentions
'''
Now we've specified 2 parameters for our function, calling them num1
and num2, for number 1 and number 2.

Now, we carry on writing our function, where we can specify what we
desire to do with num1 and num2.

in our case, we want to do simple addition.
'''
def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is', num1)
    # so here the answer variable will be filled with whatever
    # num 1 plus num 2 is.
    print(answer)
    # then at the end, we want to print out the answer to the client


'''
so now we run this, and when we want to do some simple_addition...
'''

simple_addition(5,3)
# here we will do 5 + 3, for an answer of 8

'''
There is no limit to the amount of variables you can have. The only thing
you will want to look out for at this point is the order of the variables,

as well as the quantity.

You can protect yourself from order by doing the following in your calling:
'''

simple_addition(num1=3,num2=5)
# or more clearly #
simple_addition(num2=3,num1=5)

# in this case, if you are clear in your specification, it does not matter
# the order. Most people, however, do not write out the variables like that,
# they just maintain the order.


#finally, it is important to use the proper quantity of variables.

# will not work, too many vars
simple_addition(3,5,6)

# will not work, too few vars
simple_addition(3)




'''
That's it for this video, in the next video I willbe covering default variable
assignments. 

'''






