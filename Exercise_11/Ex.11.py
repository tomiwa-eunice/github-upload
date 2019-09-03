# Numerical arrays and numpy
# ex.11.1
# building array handling
import numpy as np
# creating array from a list
my_num = np.random.randint(0,40,40)
arr1 = np.array(my_num)
print(arr1)              # prints array
print(arr1.shape)        # prints array shape
print(arr1.size)         # prints array size
print(arr1.ndim)         # prints array dimension


# ex.11.2
# create empty and fill array
arr2 = np.empty(20, dtype=np.float)
arr2.fill(42)
print(arr2)
set1 = arr2.reshape(4, 5)
print(set1)


# ex.11.3
# arranging and reshaping an array
arr3 = np.arange(1, 17).reshape(4,4)
print(arr3)

# slicing and indexing operations
print(arr3[:1, :1])
print(arr3[2:3, 3:])
print(arr3[2:3, 2:3])
print(arr3[1:2, 1:2])
print(arr3[1:2, :])
print(arr3[:, 2:3])
print(arr3[:, 3:4])
print(arr3[:, 0:1])
print(arr3[2:3, 1:])
print(arr3[0:3, 3:])
print(arr3[3:, :])
print(arr3[1:2, 2:])
print(arr3[0:2, 0:2])
print(arr3[0:3, 0:2])
print(arr3[0:2, 0:3])
print(arr3[0:, 0:2])
print(arr3[0:2, 0:])
print(arr3[0:3, 0:3])
print(arr3[0:3, 0:])
print(arr3[0:, 0:3])


# ex.11.4
# statistical operations using slices and indexes
my_num1 = np.random.randint(0, 100, 25)
print(my_num1)

array = np.array(my_num1)
print(array)

set2 = my_num1.reshape(5, 5)
print(set2)

# mean
print(set2.mean())
# standard deviation
print(set2.std())
# max
print(set2.max())
# min
print(set2.min())

print(set2.mean(axis=1))
print(set2.mean(axis=0))

c1 = set2[0:, 0:1]
print(c1)
print(c1.mean())

# alternative for mean of 1st col
print(set2.mean(axis=0)[0])
print(set2[:, 0].mean())

# std of 2nd row
print(set2[1, :].std())
print(set2.std(axis=1)[1])

# max of 3rd col
print(set2.max(axis=0)[2])
print(set2[:, 2:3].max())

# min of 4th row
print(set2.min(axis=1)[3])
print(set2[3:4, :].min())

# mean and std of 2*2 square
print(set2[1:3, 1:3].mean())
print(set2[1:3, 1:3].std())

# max of 2*3 square
print(set2[0:2, 0:3].max())

# min of 3*2 square
print(set2[0:3, 0:2].min())

# mean of 3*3
print(set2[0:3, 0:3].mean())

print(set2[0:3, 0:4].std())
print(set2[0:4, 0:4].max())
print(set2[0:4, 0:].min())


# ex.11.5
# statistical operations using axis
my_num2 = np.random.randint(0, 100, 25)
array = np.array(my_num2)
set3 = my_num2.reshape(5, 5)
print(set3)
print(set3.sum(axis=0))
print(set3.prod(axis=0))
print(set3.sum(axis=1))
print(set3.prod(axis=1))
print(set3[1:4, 1:4].sum(axis=0))
print(set3[1:5, 1:4].sum(axis=1))
print(set3[1:3, 1:5].sum(axis=0))
print(set3[0:, 1:5].sum(axis=1))


# ex.11.6
# stacking arrays
import numpy as np
import matplotlib.pyplot as plt


b1 = np.random.randint(0, 255, 900)
b2 = np.random.randint(0, 255, 900)
b3 = np.random.randint(0, 255, 900)

a1 = b1.reshape(30,30)
a2 = b2.reshape(30,30)
a3 = b3.reshape(30,30)

print(a1.shape)
print(a2.shape)
print(a3.shape)

# plotting  images using cmap parameter for colour scale
plt.subplot(2,2,1)
plt.imshow(a1, cmap='Greens', interpolation='nearest')

plt.subplot(2,2,2)
plt.imshow(a2, cmap='Blues', interpolation='bicubic')

plt.subplot(2,2,3)
plt.imshow(a3, cmap='Wistia', interpolation='bilinear')

# creating the stack using depth stack
d = np.dstack((a1, a2, a3))
print(d.shape)
plt.subplot(2,2,4)
plt.imshow(d.astype(np.uint8))
plt.show()


