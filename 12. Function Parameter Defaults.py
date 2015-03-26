'''
Hello again and welcome to another python 3 basics video. In this video we
will be covering default function parameters
'''

# so normally, you write a function like so:
def simple(num1,num2):
    pass

# What you can do, however is:

def simple(num1, num2=5):
    # what this does is specify a "default parameter" just in case
    # one is not specified.
    # this is useful so all parameters dont need to be called
    # every single time. Generally, this is used for modules.
    # an example would be a module that makes windows for users.
    pass


# so here, the user must specifiy width and height, but a font of times
# new roman, for example, is the default so they dont have to say that
# every single time.

def basic_window(width,height,font='TNR'):
    # let us just print out everything
    print(width,height,font)



# now, when we call basic_window, we can break a rule we established
# earlier:

# see, only two parameters, when we require 3
basic_window(350,500)

# we can do this because there is a default if font is not specified. Should
# a user wish to specify however, they can do

basic_window(350,500,font='courier')

# here, it is just important that you place any parameters with default values
# at the very end, to avoid trouble when calling the function down the road. 
