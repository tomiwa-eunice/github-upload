# ex.3.1
print(len('How many characters do i have?'))

# ex.3.2
x = 'I see skies of blue and clouds of white'
n=str(len(x))
print(n+" - "+x)
# this converts the length of x into a string and also separates the n from
# printing the variable x with a "-"

x = 'The bright blessed day, the dark sacred night'
n=str(len(x))
print(n+" - "+x)

x = 'And I said to myself:'
n=str(len(x))
print(n+" - "+x)

x = ' "What a wonderful world!" '
n=str(len(x))
print(n+" - "+x)

# alternative 2
x = 'I see skies of blue and clouds of white'
n=str(len(x))
print(n+" = "+x)
# this converts the length of x into a string and also separates the n from
# printing the variable x with a "=", it also writes the lyrics to a song.

x = 'The bright blessed day, the dark sacred night'
n=str(len(x))
print(n+" = "+x)

x = 'And I said to myself:'
n=str(len(x))
print(n+" = "+x)

x = ' "What a wonderful world!" '
n=str(len(x))
print(n+" = "+x)

# ex.3.4
# Syntax Errors are defined as the most basic type of error.
# They arise when the Python parser is unable to understand a line of code.
# In IDLE, it will highlight where the syntax error is.
# Most syntax errors are typos, incorrect indentation,
# or incorrect arguments.

# Semantic Error: If there is a semantic error in your program,
# it will run successfully in the sense that the computer will not generate
# any error messages. However, your program will not do the right thing.
# It will do something else. Specifically, it will do what you told it to do.

# Alternative 3 with a function
# My first Function
def wonder_print(s):
    n = str(len(s))
    print(n + " - " + s)


wonder_print('I see skies of blue and clouds of white')
wonder_print('The bright blessed day, the dark sacred night')
wonder_print('And I said to myself:')
wonder_print(' "What a wonderful world!" ')
# this is called Refactoring. which means trying to simplify the code
# by re-using similar pieces of code.
# It reduces repetition and also improves readability of one's program.
