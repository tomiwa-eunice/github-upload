import os
from osgeo import gdal, ogr, gdal_array as gdarr
import matplotlib.pyplot as plt
import numpy as np

# import matplotlib.mpimg as img

dataDirecctory = r'C:\GeoComProjects\Image_Manipulation'

# initialize dataset variable
raster = None

os.chdir(dataDirecctory)

#open the raster
raster = gdal.Open('28H-1.tif')

# get one band
xoff = 0
yoff = 0

band1 = raster.GetRasterBand(1)
band2 = raster.GetRasterBand(2)
band3 = raster.GetRasterBand(3)
band4 = raster.GetRasterBand(4)


win_xsize = raster.RasterXSize     # no of rows
win_ysize = raster.RasterYSize      # no of columns
count = raster.RasterCount          # no of bands

print('Number of rows: ', win_xsize)
print('Number of columns: ',win_ysize)
print('Number of bands: ',count)


# showing the image in 2D array
im_arr1 = gdarr.BandReadAsArray(band1, xoff, yoff, win_xsize, win_ysize)
im_arr2 = gdarr.BandReadAsArray(band2, xoff, yoff, win_xsize, win_ysize)
im_arr3 = gdarr.BandReadAsArray(band3, xoff, yoff, win_xsize, win_ysize)
im_arr4 = gdarr.BandReadAsArray(band4, xoff, yoff, win_xsize, win_ysize)

d = np.dstack((im_arr1, im_arr2, im_arr3))
print(d)


# plots the tiff image
plt.imshow(d.astype(np.uint8))
plt.show()
print()


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
img_matrix1 = np.zeros((win_ysize, win_xsize), dtype=np.int)
img_matrix2 = np.zeros((win_ysize, win_xsize), dtype=np.int)
img_matrix3 = np.zeros((win_ysize, win_xsize), dtype=np.int)
img_matrix4 = np.zeros((win_ysize, win_xsize), dtype=np.int)
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