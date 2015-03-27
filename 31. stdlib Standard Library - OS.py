'''
Now we're going to cover the standard library, or stdlib

First up, os
'''

import os

'''
os can be used mostly for directory operations. Operations like
finding out where you are, changing that, making directories, and more.

Let's see some examples:
'''

# current working directory

curDir = os.getcwd()
print(curDir)



# make another directory:

os.mkdir('newDir')

# remove:
#

import time

time.sleep(2)
os.rename('newDir','newDir2')
time.sleep(2)
os.rmdir('newDir2')


'''
There are more things you can do, but these are some of the more basics.
'''
