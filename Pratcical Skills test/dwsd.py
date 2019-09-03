import os
from osgeo import gdal, ogr, gdal_array as gdarr
import matplotlib.pyplot as plt
import numpy as np



# defining the median filter function

def find_median(image, center_X, center_Y):
    '''
    defining a median filter function
    :param image: this is the numpy array that will be read for value access
    :param center_X: this is the center of the X values in the median filter
    :param center_Y: this is the center of the Y values in the median filter
    :return: the median values for each center will be returned, populating the median filter matrix.
    '''

    my_val = image[center_X-1:center_X+2, center_Y-1:center_Y+2]
    sort_val = np.sort(my_val)
    median_val = np.median(sort_val)

    return median_val


# create a m_filtered image matrix
img_matrix1 = np.array[[115, 125, 140, 120], [119, 132, 139, 151], [101,134,124,122], [148,255,110,126]]. reshape(4,4)

# print(img_matrix)
# print(img_matrix.shape)


# looping through the image
# Band 1
for  i in range(1, win_ysize-1):
    for j in range(1, win_xsize-1):
        img_matrix1[i, j] = find_median(im_arr1, i, j)
print('first band is finished')
# plt.imshow(img_matrix1)
# plt.show()


# Band 2
for i in range(1, win_ysize-1):
    for j in range(1, win_xsize-1):
        img_matrix2[i, j] = find_median(im_arr2, i, j)
print('second band is finished')
# plt.imshow(img_matrix2)
# plt.show()

# Band 3
for  i in range(1, win_ysize-1):
    for j in range(1, win_xsize-1):
        img_matrix3[i, j] = find_median(im_arr3, i, j)
print('third band is finished')
# plt.imshow(img_matrix3)
# plt.show()

# Band 4
for  i in range(1, win_ysize-1):
    for j in range(1, win_xsize-1):
        img_matrix4[i, j] = find_median(im_arr4, i, j)
print('last band is finished')
# plt.imshow(img_matrix4)
# plt.show()

d = np.dstack((img_matrix1, img_matrix2, img_matrix3, img_matrix4))
print(d)
# plots the filtered image
# plt.imshow(d.astype(np.uint8))
# plt.show()



# closing file
if raster is not None:
    raster = None