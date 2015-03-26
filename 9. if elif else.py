'''
What is going on everyone welcome to my if elif else tutorial video.

The idea of this is to add yet another layer of logic to the pre-existing if else statement.

See with our typical if else statment, the if will be checked for sure, and the

else will only run if the if fails... but then what if you want to check multiple ifs?

You could just write them all in, though this is somewhat improper. If you actually desire to check every single if statement, then this is fine.

There is nothing wrong with writing multiple ifs... if they are necessary to run, otherwise you shouldn't really do this.

Instead, you can use what is called the "elif" here in python... which is short for "else if"


'''

x = 5

y = 10

z = 22

# first run the default like this, then
# change the x > y to x < y...

# then change both of these to an  == 
if x > y:
    print('x is greater than y')
elif x < z:
    print('x is less than z')

else:
    print('if and elif never ran...')
