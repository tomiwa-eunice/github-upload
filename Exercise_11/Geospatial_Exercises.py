# import numpy as np
# import os
#
#
# def read_one(path):
#     band = np.loadtxt(path, delimiter=";")
#     return band


# def read_many(path):
#     lband = []
#     for root, dirs, files in os. walk(path):
#         for file in files:
#             tmp = path + "\\" + file
#             band = read_one(tmp)
#             lband.append(band)
#     stack = np.dstack(np.array(lband))
#     return stack


# path_in = r"C:\GeoComProjects\Exercise_11"
# stack = read_many(path_in)
# print(stack.shape)

# ex.11.7
import numpy as np
import matplotlib.pyplot as plt


def read_one(path):
    band = np.loadtxt(path, delimiter=";")
    return band

path = r'C:\GeoComProjects\Exercise_11\csv_numpy\2014_DOY_180.csv'
image = read_one(path)
print(image)

print('shape = ', image.shape)
print('dimension = ', image.ndim)
print('size =', image.size)

print('lowest temperature = ', image.min())
print('highest temperature = ', image.max())
print('index of lowest temperature =', np.where(image == image.min()))
print('index of highest temperature =', np.where(image == image.max()))


# ex.11.8
plt.subplot(2,2,1)
plt.imshow(image)
plt.colorbar()

plt.subplot(2,2,2)
plt.imshow(image, cmap="Greens", interpolation='None')
plt.colorbar()

plt.subplot(2,2,3)
plt.imshow(image, cmap="Blues", interpolation='nearest')
plt.colorbar()

plt.subplot(2,2,4)
plt.imshow(image, cmap="Wistia", interpolation='spline16')
plt.colorbar()

plt.show()


# ex.11.9
import numpy as np
import matplotlib.pyplot as plt


def read_one(path):
    band = np.loadtxt(path, delimiter=";")
    return band


path_1 = r'C:\GeoComProjects\Exercise_11\csv_numpy\2014_DOY_180.csv'
path_2 = r'C:\GeoComProjects\Exercise_11\csv_numpy\2014_DOY_182.csv'

band_1 = read_one(path_1)
band_2 = read_one(path_2)

print(band_1.size)
print(band_2.size)

band_3 = np.subtract(band_2, band_1)

plt.subplot(1,3,1)
plt.imshow(band_1)
plt.colorbar()
plt.title('Temperature values for \n June, 2014')

plt.subplot(1,3,2)
plt.imshow(band_2)
plt.colorbar()
plt.title('Temperature values for \n July, 2014')

plt.subplot(1,3,3)
plt.imshow(band_3)
plt.colorbar()
plt.title('Temperature Difference for \n June and July, 2014')

plt.show()


# ex.11.10
import numpy as np
import matplotlib.pyplot as plt


def read_one(path):
    band = np.loadtxt(path, delimiter=";")
    return band


path = r'C:\GeoComProjects\Exercise_11\csv_numpy\2014_DOY_180.csv'

canvas = np.zeros((50, 100))
image1 = read_one(path)
# print(image1)
# print(canvas.shape)

lowest = image1.min()
highest = image1.max()
idx_lowest = np.where(image1 == lowest)
# print(idx_lowest)
idx_highest = np.where(image1 == highest)


rowpos_lo = idx_lowest[0]
# print(rowpos_lo)
# print(len(rowpos_lo))
colpos_lo = idx_lowest[1]
# print(colpos_lo)
rowpos_hi = idx_highest[0]
colpos_hi = idx_highest[1]

for i in range(len(rowpos_lo)):
    rowidx = rowpos_lo[i]
    colidx = colpos_lo[i]
    canvas[rowidx, colidx] = -1


for i in range(len(rowpos_hi)):
    rowidx = rowpos_hi[i]
    colidx = colpos_hi[i]
    canvas[rowidx, colidx] = 1


plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(image1, interpolation="None")

plt.subplot(1,2,2)
plt.title('Coldest and Hottest Spot')
plt.imshow(canvas, interpolation='None')

plt.show()


# ex.11.11










