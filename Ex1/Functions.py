#Built-in Functions
print(abs(-1))
print(min(23, 45))
print(max(100, 64))
print(pow(2,50))
print(2**50)

#Built-in Conversion
#string to integer
print(int("32"))
#string to integer
print(int("Hello"))
#float to integer
print(int(3.99998))
#float to integer
print(int(-2.3))
#integer to float
print(float(6))
#string to float
print(float('555'))
#integer to string
print(str(55))
#float to string
print(str(5.678))

def double_it(x):
    if x.__class__ is not 'a'.__class__:
        return None
    return (x*2)
print(double_it("Tom"))
