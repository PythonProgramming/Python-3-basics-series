# Some of the built in functions #

'''
I cannot cover them all in 1 video, but there are quite a few that I find
myself needing semi-regularly. Also, some we've already covered,
or are fairly complex, so I will cover them later. 

I will post a link in the description to the list of all built in functions.

https://docs.python.org/3/library/functions.html

With that, we'll go alphabetically. 
'''

### absolute value ###

'''
Absolute value bars just turn anything into the distance it is from 0. Basically,
it will take your negative numbers, if you have any, and make them positive.

I find myself using this for % change, esp when negative numbers are in question.
So say you go from -6 to -9. Typical % change will say this is a -33.33% change..
even though this was a positive movement.

There are many other uses for it though.
'''

exNum1 = -5
exNum2 = 5

print(abs(exNum1))

if abs(exNum1) == exNum2:
    print('True!')


### Help ###

'''
Probably one of the most under-utilized commands in Python, most people
do not even know it exists.... HELP! Here, you can
just type help() empty params... or put something in there. 
'''


'''
With empty parameters, it begins an interactive session, where you can
just type in the name of the function that you are looking for
'''
help()

'''
Or...
'''

import time
help(time)


### Max and Min ###

'''
How to find the maximum or highest number in a list...
or how to find the lowest or minimum number in a list. 
'''

exList = [5,2,1,6,7]

largest = max(exList)
print(largest)

smallest = min(exList)
print(smallest)


### Rounding ###
'''
This will round to the nearest whole. There are other commands
like ceiling and floor, if you require rounding up or down... but
for now, let's just round:
'''

x = 5.622
x = round(x)
print(x)

y = 5.256
y = round(y)
print(y)


### Converting data types! ###

'''
Many times, like reading data in from a file, you might find
the datatype is incorrect, like when we mean to have integers,
but they are currently in string form, or visa versa. 
'''

intMe = '55'
intMe = int(intMe)
print(intMe)


stringMe = 55
stringMe = str(stringMe)
print(stringMe)

floatMe = 55
floatMe = float(floatMe)
print(floatMe)

'''
You can also convert floats to strings, strings to floats... and more. Just make sure you do a valid operation.
You still cannot convert 'h' to a float. 
'''
















