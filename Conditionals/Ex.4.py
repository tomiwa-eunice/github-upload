# Ex. 4.1
def is_even(x):
    return x % 2 == 0
a = is_even(22)
print(a)

b = is_even(21)
print(b)
# a return statement hands back it's value to it's caller.

# Ex. 4.4 Comparisons
input_mark = int(input("enter here mark: "))
if input_mark >= 55:
    print("pass the student")
else:
    print("fail the student")

# Ex.4.5
input_mark = int(input("enter here mark"))
if input_mark >= 55:
    print("pass the student")
    if input_mark < 80:
        print("average student")
    else:
        print("excellent student")
else:
    print("fail the student")

input_mark = int(input("enter here mark"))
if input_mark > 80:
    print("pass the student")
    print("excellent student")
elif input_mark >= 55:
    print("pass the student")
    print("average student")
else:
    print("fail the student")

# Ex.4.6
def day_of_week(day_of_week):
    if day_of_week == 0:
        print('Monday')
    elif day_of_week == 1:
        print('Tuesday')
    elif day_of_week == 2:
        print('Wednesday')
    elif day_of_week == 3:
        print('Thursday')
    elif day_of_week == 4:
        print('Friday')
    elif day_of_week == 5:
        print('Saturday')
    elif day_of_week == 6:
        print('Sunday')
    elif day_of_week >=7:
        raise Exception('day of the week should not exceed 6. The day of the week was {}'.format(day_of_week))

a=int(input("Day of the week"))
day_of_week(a)

