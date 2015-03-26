#! python3

'''
Hey everyone and welcome to another python 3 tutorial. This tutorial will be
covering the for loop. The for loop is used for many of the same tasks as the
while loop.

Typically, you will see the while loop  being used for finite tasks that have
predetermined length, and the for loop being used for tasks that have uncertain
and variable timeframes.

That said, the for loop can be used for the exact same tasks as the while loop.

for this reason, I prefer the for loop myself, but again, it comes down to
personal preference. I will show you why here. 

'''
import time

exampleList = [1,5,6,6,2,1,5,2,1,4]

for x in exampleList:
    print(x)



# usually people use for loops to iterate through something,
# and you can iterate for the same purposes as the previous
# while loop did, as more of a counter:


for x in range(1,11):
    print(x)


# Range is a built in python function, and it literally will make a range
# of numbers for you. In python 2.7, Python's 3.3 is the equivalent of
# 2.7's xrange... so this range is a generator function and will not
# blow out your memory like python 2.7's range.

time.sleep(555)
