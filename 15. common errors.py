'''
Hello and welcome to another python 3 basics video.

In this video we'll be discussing some of the basics to
debugging. In my videos, I get a lot of questions for
help where people have errors and are not sure what
the problem is. If they used some extremely simple debugging,
they'd realize how obvious the answer is.

Most of the time, the problem is a typo, followed closely by
a misunderstanding of indentation and standards.

so standards how are how organize your code. With python,
unlike most languages, you define blocks of code like
functions by indentation. Most python editors will automatically
indent for you where it is necessary. With this, if you are ever
coding along and find python automatically indenting you where
you don't think it should, this should raise a flag for you to
figure out.


(show a basic function... )

There are some more in-depth common-issues that you'll
find from time to time, you can find more debugging videos
by searching for debuggin in my channel. For now I will just
keep these ones basic.

The first error we'll discuss is the NameError: is not defined

'''

'''
As obvious as this might appear to you, this gets people amazingly
frequently. Just learn to recognize the "is not defined"

chances are you typoed the definition of the variable or when you
are referring to it. 
'''
variable = 55
#print(varaible)


'''
Next up, we have indentation issues.

You will see "expected an indented block" as a
popup when you never enter an indented block for
something that requires it, like a function.
'''

'''
def task1():


def task2():
    print('more tasks')

'''


'''
unexpected indent...
'''

def task():
    print ('stuff')

print('more stuff')

    print('stuff')



'''
EOL while scanning string literal
'''


def task():
    print('some people find themselves committing this too


    print('ouch...')



          
