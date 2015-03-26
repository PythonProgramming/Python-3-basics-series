'''
Python is a very popular programming language for data processing of many types
With data processing, a lot of math is used often times. So, besides the basic
math, we should cover some more in depth operations. Luckily for us, python 3
has some great built in modules that we can utilize. 
'''

import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

x = statistics.mean(example_list)
print(x)

y = statistics.median(example_list)
print(y)

z = statistics.mode(example_list)
print(z)

a = statistics.stdev(example_list)
print(a)

b = statistics.variance(example_list)
print(b)



