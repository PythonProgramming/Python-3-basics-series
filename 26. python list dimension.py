'''
Lists that we have covered so far have all been 1 dimensional,
but you can have lists within lists within lists within lists if you want.

Often times, if you want to have lists within lists, your superior choice
will be something like dictionaries, which we'll get to, but
there will be times when a multi dimensional list is the best choice.
'''

x = [[2,6],[6,2],[8,2],[5,12]]

# so we already know how to reference elements in a list, we can do:

print(x[2])

# but we can also take this deeper since we have more dimensions now:

print(x[2][1])

# this can go on indefinitely with very thick lists.
# you might see how this can quickly get messy, let's consider
# how to properly display lists in code that have multiple dimensions.
# you might not typically hard code multi dimensional lists,
# but it's good to know how to do it:


y = [[5,2],
     [6,2],
     [3,1],
     [12,6]
    ]

# this is slightly cleaner, and python automatically understands it:

print(y)










