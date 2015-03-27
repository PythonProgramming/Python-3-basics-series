'''
Now that we've used a module, statistics, it would be a good time to
explain some import practices. As with many things in programming, there
are many ways to import modules, but there are certainly some best
practices.

So first, when you import a module, you are basically loading that
module into memory. Think of a module like a script. Many if not most modules
are just a single python script. So, when you go to import it, you use the file
name. This can help keep code clean and easy to read. Many python developers
just program everything in 1 script. Other developers, say from a language like
java are going to be very used to doing lots of imports with a file for each
type of job that's happening. Just like there are many ways to import, there
are many more ways to program.

So let's talk about basic importing:
'''

# here, we have imported the entire statistics module, and we can reference
# any of the functions within it.
# this loads that entire module, and will run any code that is
# set to run in the module
# remember if name == main? Again, that's what we use to stop code
# from running when we just want to import. 
import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

# now, to use our import above, since we just imported statistics,
# we must preceed any funciton wi thin statistics with a statistics.
# so, for example, to access the mean() function within statistics:

print(statistics.mean(example_list))


# and that's it. Let's look briefly at the statistics module and the mean
# function...c:/python34/lib/statistics  (not in site-packages)
# take note of the package's location, we will talk more on that soon.
# so now you see that statistics is just a python script, and mean is
# just another function.

# sometimes, you will see people who import things "as". This
# helps to keep typing to a minimum. For example

import statistics as s

# above we've imported statistics as s, so when we want to reference something
# within statistics, we just need to do s. now.

print(s.mean(example_list))

# What if you don't even want to type that S though? Well there's an app for that!
# you can just import all of the functions like so:

from statistics import mean

# so here, we've imported the mean function only.

print(mean(example_list))

# and again we can do as

from statistics import mean as m

print(m(example_list))

# what if we want to import other functions?

from statistics import mean, median

# here we imported 2 functions.

print(median(example_list))

# what if we want to use the as as well????

from statistics import mean as m, median as d

print(m(example_list))
print(d(example_list))


# What if we want to just import everything from statistics like we did initially
# but we dont want to type the statistics because we have
# fat fingers and this will just slow us down?.

from statistics import *

print(mean(example_list))
