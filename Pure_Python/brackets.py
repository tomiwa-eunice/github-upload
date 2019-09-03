# ex.3.6
def print_with_brackets(name):
    print("[[[ ", name, " ]]]")


print_with_brackets("Tomiwa")

# ex.3.7
def print_with_brackets(name):
    print ("[[[ ", name, " ]]]")

print_with_brackets("Peter")
print_with_brackets("Paul")
print_with_brackets("Mary")

def print_three_names(name, name2, name3):
    print_with_brackets(name)
    print_with_brackets(name2)
    print_with_brackets(name3)
print_three_names('Peter', 'Paul', 'Mary')

#def print_with_brackets(name):
#    return print_three_names('Peter', 'Paul', 'Mary')
#
#print_with_brackets(

#ex.3.8
print_with_brackets('GFM')
# print('GFM' + 10)
print('GFM' , 10)
# print_with_brackets('GFM') + 10
print('GFM' * 10)
print_with_brackets('GFM' * 10)
# print_with_brackets('GFM') * 10

#FUNCTION - AREA CIRCLE
import math
def squared(x):
    '''mowa is a yeye boy'''
    return x**2
def area_circle(radius):
    return squared(radius) * math.pi
print (area_circle(5))



