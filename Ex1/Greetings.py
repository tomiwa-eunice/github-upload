'''
name = input("What is your name? ")
print(name)
print(type(name))
'''

name = input("What is your name? ")
print("Your name is , name")
print("Hello, " + name + "! How are you?")

x = 'hello'
x
print(x)
print(x, x)
print(x, x, sep='+')
print(x, x, sep=',')
help(print)

print('"Hello World"')
print('Hello \nWorld')
print('Hello' + "World!")
print('Hello', 'World!')
print('Hello' + '  ' + 'World!')
print('Hello' ,'World!', sep='  ')
print('He' + 2 * 'l' + 'o Wo' + 'rld!')
print(3* 'Hello, ' + 'World!')

print ('Hello','world',end='.')
print ('Hello','world',end=',')
print('Hello','world',end='Finish')
print('Hello','world',end='\n')
print('Hello','world',end='\n\n')

a = 3 - 4 + 10
print(a)
b = 5 * 6
print(b)
c = 7.0 // 8.0
print(c)
a = a + 1
print(a)
d = a + b + c
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))