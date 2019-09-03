# Dictionaries and Strings
# use of strings
# ex.7.1
my_fruit = "strawberries"
print(len(my_fruit))
print("<", my_fruit * 10, ">")

# ex.7.2
my_fruits = 'strawberries' + 'mango' + 'grapes' + 'apples'
print(my_fruits)
print(len(my_fruits))
print(my_fruits * 3)

# ex.7.3
my_fruits = 'strawberries' " " 'mango' " "  'grapes' " "  'apples' " " 'oranges'
print(my_fruits)
print(my_fruits[0:29:2])
print(my_fruits[0:29:4])
print(my_fruits[29:0:-2])
print(my_fruits[29:0:-4])

# ex.7.4
# truth value
'watermelon' == 'waterMelon'
'BANANA' == 'BANana'
'a' in 'cranberry'
'g' not in 'dragon fruit'
'berry' in 'blueberry'
"cherry".isupper()
"CHERRY".islower()
"pear***apple".isalnum()
"pear444apple".isalpha()

# ex.7.5
my_fruits = 'strawberries' " " 'mango' " "  'grapes' " "  'apples'
split_m_f = my_fruits.split(" ")
print(split_m_f)

my_fruits_str = "->".join(split_m_f)
print(my_fruits_str)

# ex.7.6
my_fruits = 'strawberries' " " 'mango' " "  'grapes' " "  'apples' " " 'oranges'
split_m_f = my_fruits.split(" ")
print(split_m_f)

my_fruits_str = "->".join(split_m_f)
print(my_fruits_str)

del(split_m_f[0])
print(split_m_f)

my_fruits_str = "*".join(split_m_f)
print(my_fruits_str)

F = my_fruits_str.replace("*", " ")
print(F)


# ex.7.7
# looping
my_fruits = 'strawberries', 'mango', \
            'grapes', 'apples', \
            'oranges', 'pineapple', \
            'coconut'
print(my_fruits)
fruits = list(my_fruits)
print(fruits)



















