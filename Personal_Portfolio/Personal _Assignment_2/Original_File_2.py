import csv
import matplotlib.pyplot as plt
import numpy as np
import os

#1
os.chdir(r"C:\Users\piscobexigacalistlf\Documents\ScientificGeocomputing\Assigments\2")

def read_csv_file(file_path):
    data = {'countries':[],'final_2016':[],'final_hh_2016':[],'final_hh_2000':}
    file = open(file_path)
    csv_reader = csv.DictReader(file,delimiter=';')
    for row in csv_reader:
        data['countries'].append(row['geo'])
        data['final_2016'].append(int(row['final_2016']))
        data['final_hh_2016'].append(int(row['final_hh_2016']))
        data['final_hh_2000'].append(int(row['final_hh_2000']))
    return data

#2
energy_dict = read_csv_file('assign2_data.csv')

#3
plt.subplot(1,3,1)
plt.barh(energy_dict['countries'],energy_dict['final_2016'], color="blue")
plt.title('Total energy consumption\n in 2016')
plt.xlabel('Oil equivalent (tons)')
plt.subplot(1,3,2)
plt.barh(energy_dict['countries'],energy_dict['final_hh_2016'], color="blue")
plt.title('Energy consumption \n per capita in 2016 ')
plt.xlabel('Oil equivalent (kg)')
plt.subplot(1,3,3)
plt.plot(energy_dict['countries'],energy_dict['final_hh_2000'], color="red", label='2000')
plt.plot(energy_dict['countries'],energy_dict['final_hh_2016'], color="blue", label='2016')
plt.Title('Energy consumption \n per capita ')
plt.ylabel('Oil equivalent (kg)')
plt.legend()
plt.xticks(energy_dict['countries'],rotation=45)
plt.show()

#4
energyDiference=[]
for i in range(len(energy_dict['final_hh_2016'])):
    value2016=energy_dict['final_hh_2016'][i]
    value2000=energy_dict['final_hh_2000'][i]
    energyDiference.append(value2016-value2000)

#5
plt.subplot(1,1,1)
plt.barh(energy_dict['countries'],energyDiference, color="blue")

test, testn, testp = {}, {}, {}

for i in energy_dict['countries']:
    for j in energyDifference:
        test[i] = j

for k,v in test.items():
    if v < 0:
        ncon.append(k)
        nval/
    else:
        testp[k]=v


plt.subplot(1, 1, 1)
plt.barh(testp.keys(), testp.values(), color='b', label='postive Energy Difference')    # list comprehension
# plt.barh(list(testn.keys()), list(testn.values()), color='r', label='negative Energy Difference')
plt.title('Energy Consumption Difference \n between 2000 and 2016')
plt.xlabel('Oil Equivalent (kg)')
plt.grid(linestyle=':')                             # adds grid with a different format
plt.show()                                          # plots the figure

