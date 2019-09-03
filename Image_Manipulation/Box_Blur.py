import os
from osgeo import gdal, ogr, gdal_array as gdarr
import matplotlib.pyplot as plt
import numpy as np

dataDirectory = r'C:\GeoComProjects\Image_Manipulation'

raster = None

os.chdir(dataDirectory)

raster = gdal.Open('SPOT270611.img')

# getting the bands
xoff = 0
yoff = 0
win_xsize = raster.RasterXSize      # no of rows
win_ysize = raster.RasterYSize      # no of columns
count = raster.RasterCount          # no of bands

print('Number of rows: ', win_xsize)
print('Number of columns: ',win_ysize)
print('Number of bands: ',count)

band1 = raster.GetRasterBand(1)
band2 = raster.GetRasterBand(2)
band3 = raster.GetRasterBand(3)
band4 = raster.GetRasterBand(4)

arr1 = gdarr.BandReadAsArray(band1, xoff, yoff, win_xsize, win_ysize)
arr2 = gdarr.BandReadAsArray(band2, xoff, yoff, win_xsize, win_ysize)
arr3 = gdarr.BandReadAsArray(band3, xoff, yoff, win_xsize, win_ysize)
arr4 = gdarr.BandReadAsArray(band4, xoff, yoff, win_xsize, win_ysize)

# stack the bands
d1 = np.dstack((arr1, arr2, arr3))

# plots the spot image
plt.imshow(d1.astype(np.uint8))
plt.show()
print()



# defining the Box Blur Filter function
def bb_filter(image, center_X, center_Y):
    my_val = image[center_X-1:center_X+2, center_Y-1:center_Y+2]
    sort_val = np.sort(my_val)
    mean_val = np.average(sort_val)

    return mean_val


# create a m_filtered image matrix
img_matrix1 = np.zeros((win_ysize, win_xsize), dtype=np.int)
img_matrix2 = np.zeros((win_ysize, win_xsize), dtype=np.int)
img_matrix3 = np.zeros((win_ysize, win_xsize), dtype=np.int)
img_matrix4 = np.zeros((win_ysize, win_xsize), dtype=np.int)


# looping through the image
# Band 1
for  i in range(1, win_ysize-1):
    for j in range(1, win_xsize-1):
        img_matrix1[i, j] = bb_filter(arr1, i, j)
print('first band is finished')
# plt.imshow(img_matrix1)
# plt.show()

# Band 2
for  i in range(1, win_ysize-1):
    for j in range(1, win_xsize-1):
        img_matrix2[i, j] = bb_filter(arr2, i, j)
print('second band is finished')
# plt.imshow(img_matrix2)
# plt.show()

# Band 3
for  i in range(1, win_ysize-1):
    for j in range(1, win_xsize-1):
        img_matrix3[i, j] = bb_filter(arr3, i, j)
print('third band is finished')
# plt.imshow(img_matrix3)
# plt.show()

# Band 4
for  i in range(1, win_ysize-1):
    for j in range(1, win_xsize-1):
        img_matrix4[i, j] = bb_filter(arr4, i, j)
print('last band is finished')
# plt.imshow(img_matrix4)
# plt.show()

d1 = np.dstack((img_matrix1, img_matrix2, img_matrix3, img_matrix4))

# plots the filtered image
plt.imshow(d1.astype(np.uint8))
plt.show()



# closing file
if raster is not None:
    raster = None