import csv
import matplotlib.pyplot as plt
import numpy as np
import os

# 1
# Defining a function
os.chdir(r"C:\GeoComProjects\Personal_Portfolio\Personal _Assignment_2")

def read_csv_file(file_path):
    """
    The "read_csv_file" function reads the csv file selected as the parameter
    and converts the file into a dictionary by iterating through the file
    and appending the content of the file into the dictionary created.
    It returns the dictionary with it's assigned keys and values.
    """
    data = {'countries': [], 'final_2016': [], 'final_hh_2016': [], 'final_hh_2000': []}    # create a dictionary.
    file = open(file_path)                              # open the filepath.
    csv_reader = csv.DictReader(file,delimiter=';')     # read and create a dictionary from csv file.
    for row in csv_reader:                              # iterate over the row in the file.
        data['countries'].append(row['geo'])            # append values to the keys in the dictionary.
        data['final_2016'].append(int(row['final_2016']))
        data['final_hh_2016'].append(int(row['final_hh_2016']))
        data['final_hh_2000'].append(int(row['final_hh_2000']))
    return data


# 2
# assign the function to a variable
energy_dict = read_csv_file('assign2_data.csv')     # calling the function created in block 1.


# 3
# representing information in charts
plt.subplot(1, 3, 1)                                  # subplot will be in a 1x3 plot , at position 1, at the left.
plt.barh(energy_dict['countries'], energy_dict['final_2016'], color="blue")  # creates a horizontal bar chart.
plt.title('Total energy consumption\n in 2016')
plt.xlabel('Oil equivalent (tons)')
plt.subplot(1, 3, 2)                                  # subplot will be in a 1x3 plot , at position 2, at the middle.
plt.barh(energy_dict['countries'], energy_dict['final_hh_2016'], color="blue")   # representing the energy consumption.
# per capita in 2016 in a horizontal bar
plt.title('Energy consumption \n per capita in 2016 ')
plt.xlabel('Oil equivalent (kg)')                   # adds x label
plt.subplot(1, 3, 3)                                  # subplot will be in a 1x3 plot , at position 3, at the right.
plt.plot(energy_dict['countries'], energy_dict['final_hh_2000'], color="red", label='2000')
plt.plot(energy_dict['countries'], energy_dict['final_hh_2016'], color="blue", label='2016')
plt.title('Energy consumption \n per capita')       # adds title
plt.ylabel('Oil equivalent (kg)')                   # adds y label
plt.legend()                                        # generates the figure legend
plt.xticks(energy_dict['countries'], rotation=45)   # representation of the x-axis, rotate the labels.
plt.show()


# 4
# subtraction using numpy library
array_2016 = np.array(energy_dict['final_hh_2016'])  # creates a numpy array
array_2000 = np.array(energy_dict['final_hh_2000'])
energyDifference = np.subtract(array_2016, array_2000)  # subtract array_2000 from array_2016
print(energyDifference)                                 # print the array

# 5
# charting the energy difference
plt.subplot(1, 1, 1)
plt.barh(energy_dict['countries'], energyDifference, color="blue", label='Energy Difference')
plt.title('Energy Consumption Difference \n between 2000 and 2016')
plt.xlabel('Oil Equivalent (kg)')
plt.legend()
plt.grid(linestyle=':')                             # adds grid with a different format
plt.show()                                          # plots the figure


energyDifference2=[]
for i in range(len(energy_dict['final_hh_2016'])):
    value2016=energy_dict['final_hh_2016'][i]
    value2000=energy_dict['final_hh_2000'][i]
    energyDifference2.append(value2016-value2000)

nlist = [0 if i < 0 else i for i in energyDifference2]
plist = [i if i >= 0 else 0 for i in energyDifference2]

# 6
# create a horizontal boxplot for visualizing the energy difference
print(energy_dict['final_2016'])
magenta_diamond = dict(markerfacecolor='m', marker='D')     # define the marker type
plt.boxplot(energy_dict['final_2016'], vert=False, flierprops=magenta_diamond)      # create a horizontal boxplot
plt.title('Statistical Values showing \n Total Energy Consumption in 2016')
plt.xlabel('Range of Oil Equivalent (tons)')
plt.grid(linestyle=':')
plt.show()