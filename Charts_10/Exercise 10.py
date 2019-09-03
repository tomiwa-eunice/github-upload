# charting by coding
# ex.10.1
import matplotlib.pyplot as plt

my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.plot(my_list1)    # to plot the list

plt.title('My List')    # add title to plot
plt.grid()               # add grid to plot
plt.xlabel('X-axis')          # add labels to the axes
plt.ylabel('Y-axis')

plt.show()              # to visualize charts


# ex.10.2
# changing the markers
# dashed line marker
plt.plot(my_list1, '--')
plt.show()

# point marker
plt.plot(my_list1, '.')
plt.show()

# circle marker
plt.plot(my_list1, 'o')
plt.show()

# star marker
plt.plot(my_list1, '*')
plt.show()


# ex.10.3
# changing the color of the markers
# magenta using abbreviations
plt.plot(my_list1, color='m')
plt.show()

# green using full name
plt.plot(my_list1, color='green')
plt.show()

# using the colour wheel
# hexadecimal representation
plt.plot(my_list1, color='#0DB7E8')
plt.show()

# RGB representation
plt.plot(my_list1, color=[13/255, 183/255, 232/255])
plt.show()


# ex.10.4
# combine list
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

plt.plot(my_list1, '--', color='g')
plt.plot(my_list2, ':', color='orange', linewidth=3)

plt.show()


# ex.10.5
# charting random data using numpy
import numpy as np
random_list1 = np.random.randint(0, 25, 100)
random_list2 = np.random.randint(0, 25, 100)

plt.plot(random_list1)
plt.plot(random_list2)

plt.show()


# charting using subplots
import numpy as np

import matplotlib.pyplot as plt

random_list1 = np.random.randint(0, 25, 100)
random_list2 = np.random.randint(0, 25, 100)
random_list3 = np.random.randint(0, 25, 100)
random_list4 = np.random.randint(0, 25, 100)

plt.subplot(2, 2, 1)
plt.plot(random_list1, '-', color='g', linewidth=4)
plt.subplot(2, 2, 2)
plt.plot(random_list2, '--', color='b')
plt.subplot(2, 2, 3)
plt.plot(random_list1, 'o', color='r')
plt.subplot(2, 2, 4)
plt.plot(random_list2, '*', color='orange', linewidth=2)

plt.show()


# ex.10.6a
# creating artificial x-axis using np.linspace
import numpy as np
random_list1 = np.random.randint(0, 25, 11)
xlinspace = np.linspace(0, 10, 11)
plt.plot(xlinspace, random_list1)

# ex.10.6b
# creating artificial x-axis using np.linspace
import numpy as np

xlinspace = np.linspace(0, 1, 20)
random_list1 = np.random.randint(0, 25, 20)
plt.plot(xlinspace, random_list1)


# ex.10.7
# charting strings
labels = ['sophia', 'tomiwa', 'getachew', 'yun', 'mohan']
ages = [22, 23, 24, 25, 26]
xlinspace2 = np.linspace(0, 1, 5)
plt.plot(xlinspace2, ages, 'o')
plt.xticks(xlinspace2, labels, rotation=30)         # label rotation
plt.grid()
plt.title('Classmates and their Ages')
plt.xlabel('Classmate Names')
plt.ylabel('Ages')
# plt.plot(labels, ages, 'o')
plt.show()


# ex.10.8
# proper visualization
# my own code
labels = ['sophia', 'tomiwa', 'getachew', 'yun', 'mohan']
ages = [22, 23, 24, 25, 26]
heights = [125, 126, 127, 128, 129]

plt.plot(xlinspace2, ages, label="Ages")
plt.plot(xlinspace2, heights, label="Heights")
plt.legend(loc="upper right")

# corrected code
labels = ['sophia', 'tomiwa', 'getachew', 'yun', 'mohan']
ages = [22, 23, 24, 25, 26]
heights = [125, 126, 127, 128, 129]

plt.plot(xlinspace2, ages, label="Ages")
plt.xticks(xlinspace2, labels, rotation=30)
plt.plot(xlinspace2, heights, label="Heights")
plt.grid(True)
plt.title('Ages and Heights of my Classmates')
plt.xlabel('Classmate Names')
plt.ylabel('Ages and Heights')
plt.legend(loc="upper right")
plt.show()


# ex.10.9
# creating bar charts
import numpy as np
import matplotlib.pyplot as plt

labels = ['sophia', 'tomiwa', 'getachew', 'yun', 'mohan']
ages = [22, 23, 24, 25, 26]
xlinspace2 = np.linspace(0, 25, 5)

plt.bar(xlinspace2, ages, color='g')
plt.xticks(xlinspace2, labels, rotation=30)
plt.grid(True)          # ask about the true value
plt.title('Bar chart showing Classmates and their Ages')
plt.xlabel("Classmates")
plt.ylabel("Ages")

plt.show()


# ex.10.10
# creating histogram function
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0, 20, 100)
bins = 20

plt.hist(x, bins)
plt.xlabel('Random numbers')
plt.ylabel('Frequency')
plt.title('Distribution of numbers 1 - 20')
plt.grid(linestyle=':')         # dotted grid lines
plt.show()


# ex.10.11
# creating box plot
random_list5 = np.random.randint(10, 50, 300)

plt.boxplot(random_list5, vert=False)
plt.title('Box Plot of Random Numbers 10 - 50')
plt.ylabel('collection of numbers')
plt.xlabel('values')
plt.grid(linestyle=':')

plt.show()



# ex.10.12
# using iterations to create subplots
import matplotlib.pyplot as plt
import numpy as np

xlinspace = np.linspace(0, 1, 20)

for i in range(1, 5):
    plt.subplot(2, 2, i)
    list_numbers = np.random.randint(0, 25, 20)
    plt.plot(xlinspace, list_numbers, "--")
plt.show()

# 16 subplots
import matplotlib.pyplot as plt
import numpy as np

xlinspace = np.linspace(1, 100, 100)

for i in range(1, 17):
    plt.subplot(4, 4, i)
    list_numbers = np.random.randint(1, 100, 100)
    plt.plot(xlinspace, list_numbers, "o")
    plt.grid()
plt.show()



# advanced charting with files
# reading through a csv file
import csv
path = r'C:/GeoComProjects/Charts_10/temperature_cities.csv'
f = open(path)
reader = csv.reader(f, delimiter=';')
for line in reader:
    print(line)
f.close()

# reading a single line in a csv file
import csv
path = r'C:/GeoComProjects/Charts_10/temperature_cities.csv'
f = open(path)
reader = csv.reader(f, delimiter=';')
line = next(reader)
print(line)
f.close()


# ex.10.13
import matplotlib.pyplot as plt
import numpy as np
import csv

path = r'C:/GeoComProjects/Charts_10/temperature_cities.csv'
f = open(path)
reader = csv.reader(f, delimiter=';')
line = next(reader)
f.close()

print(line)

DH_list = []
city = line[0]
for element in line[1:]:    # converts elements to floats
    DH_list.append(float(element))
print(DH_list)
print(len(DH_list))

x = np.linspace(0, 364, 365)

plt.plot(x, DH_list, "-", label=city)
plt.title('Den Haag Temperature values')
plt.grid()
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.legend()
plt.show()


# ex.10.14
import matplotlib.pyplot as plt
import numpy as np
import csv

path = r'C:/GeoComProjects/Charts_10/temperature_cities.csv'
f = open(path)
reader = csv.reader(f, delimiter=';')
line1 = next(reader)
line2 = next(reader)
f.close()

print(line1)
print(line2)

# City of Den Haag
DH_list = []
city1 = line1[0]
for element in line1[1:]:    # converts elements to floats
    DH_list.append(float(element))
print(DH_list)
print(len(DH_list))

x = np.linspace(0, 364, 365)

# City of Enschede
EN_list = []
city2 = line2[0]
for element in line2[1:]:    # converts elements to floats
    EN_list.append(float(element))
print(EN_list)
print(len(EN_list))

x = np.linspace(0, 364, 365)

plt.plot(x, EN_list, "-", label=city2, color='r')
plt.plot(x, DH_list, "-", label=city1)
plt.title('City Temperature values')
plt.grid()
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.legend()
plt.show()


# ex.10.15
import matplotlib.pyplot as plt
import numpy as np
import csv

path = r'C:/GeoComProjects/Charts_10/temperature_cities.csv'
f = open(path)
reader = csv.reader(f, delimiter=';')

city_dict = {}

for row in reader:      # iterate over all lines
    city_list = []
    for element in row[1:]:
        city_list.append(float(element))

    city_dict[row[0]] = city_list
print(city_list)
print(city_dict)

f.close()


# ex.10.16
x = np.linspace(0, 364, 365)
counter = 1             # don't get this counter part...

for key in city_dict.keys():
    values = city_dict[key]
    print(key)
    print(values)
    plt.subplot(3, 2, counter)
    plt.plot(x, values, "o", label=key, linewidth=2, color='r')
    plt.title(key)
    plt.xlabel('Days')
    plt.ylabel('Temperature')
    plt.grid(linestyle=':')
    counter += 1
plt.show()


# ex.10.17
# histogram version
bins = 10
counter = 1             # don't get this counter part...

for key in city_dict.keys():
    values = city_dict[key]
    print(key)
    print(values)
    plt.subplot(3, 2, counter)
    plt.hist(values, bins, label=key, linewidth=2, color='r')
    plt.title(key)
    plt.xlabel('Days')
    plt.ylabel('Temperature')
    plt.grid(linestyle=':')
    counter += 1
plt.show()

# box plot version
counter = 1             # don't get this counter part...

for key in city_dict.keys():
    values = city_dict[key]
    print(key)
    print(values)
    plt.subplot(3, 2, counter)
    plt.boxplot(values)
    plt.title(key)
    plt.xlabel('Days')
    plt.ylabel('Frequency')
    plt.grid(linestyle=':')
    counter += 1
plt.show()