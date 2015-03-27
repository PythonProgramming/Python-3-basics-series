'''
Lets compare python lists and tuples. They are often confused.

A python tuple is immutable, meaning you cannot change it. That said,
less space is going to be required to generate a tuple, and you can use it
for things where you don't want the tuple to change. To define a tuple, you
either use round brackets, or no brackets. A popular use for this is multiple
variable assignments from a function return.

For example, you might see something like:
'''

def example():
    return 15, 12

x, y = example()
print(x,y)

# in the above case, we have used a tuple and cannot modify it... and
# we definitely do not want to!



'''
A python list is mutable, and can contain just about any python data. to
define a list, you use square brackets.

'''

x = [1,3,5,6,2,1,6]

'''
You can then reference the whole list like:
'''
print(x)

# or a single element by giving its index value.
# index values start at 0 and go up by 1 each time

print(x[0],x[1])



'''
So again, a python tuple is a colleciton of data that is immutable.
Generally the only time you will use this is when it is extremely
important that the tuple is immutable.

Then you have a python list, which is mutable and highly malleable.

A tuple is defined by no containing brackets, or round brackets. A list
is defined by square brackets. 
'''
