import os
from osgeo import gdal, ogr, gdal_array as gdarr
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage as nd


dataDirectory = r'C:\GeoComProjects\Exercise_18'

raster_jun = None

os.chdir(dataDirectory)

# June Data
raster_jun = gdal.Open('s2_20180608.tif')     # gets the June image data

# getting the bands
xoff_j = 0
yoff_j = 0
win_xsize_j = raster_jun.RasterXSize      # no of rows
win_ysize_j = raster_jun.RasterYSize      # no of columns
count_j = raster_jun.RasterCount          # no of bands
dataset_jun = gdarr.DatasetReadAsArray(raster_jun, xoff_j, yoff_j, win_xsize_j, win_ysize_j)


# get the red and near infrared bands
redB_jun = raster_jun.GetRasterBand(1)
greenB_jun = raster_jun.GetRasterBand(2)
blueB_jun = raster_jun.GetRasterBand(3)
nirB_jun = raster_jun.GetRasterBand(4)

# read the band as a numpy array
red_arr_jun = gdarr.BandReadAsArray(redB_jun, xoff_j, yoff_j, win_xsize_j, win_ysize_j)
nir_arr_jun = gdarr.BandReadAsArray(nirB_jun, xoff_j, yoff_j, win_xsize_j, win_ysize_j)
blue_arr_jun = gdarr.BandReadAsArray(blueB_jun, xoff_j, yoff_j, win_xsize_j, win_ysize_j)
green_arr_jun = gdarr.BandReadAsArray(greenB_jun, xoff_j, yoff_j, win_xsize_j, win_ysize_j)


# calculate NDVI using the matrix function
NDVI_jun = ((nir_arr_jun - red_arr_jun) / (nir_arr_jun + red_arr_jun))

# setting the threshold
NDVI_jun[NDVI_jun >= 0.3] = 1          # threshold for visualizing cropland areas
NDVI_jun[NDVI_jun < 0.3] = 0

# plot NDVI for jun
plt.subplot(2,2,1)
plt.imshow(NDVI_jun, cmap='gray')
plt.title('NDVI in June')



# October Data
raster_oct = gdal.Open('s2_20181006.tif')     # gets the October image data

# getting the bands
xoff_o = 0
yoff_o = 0
win_xsize_o = raster_oct.RasterXSize      # no of rows
win_ysize_o = raster_oct.RasterYSize      # no of columns
count_o = raster_oct.RasterCount          # no of bands
dataset_oct = gdarr.DatasetReadAsArray(raster_oct, xoff_o, yoff_o, win_xsize_o, win_ysize_o)


# get the red and near infrared bands
redB_oct = raster_oct.GetRasterBand(1)
greenB_oct = raster_oct.GetRasterBand(2)
blueB_oct = raster_oct.GetRasterBand(3)
nirB_oct = raster_oct.GetRasterBand(4)

# read the band as a numpy array
red_arr_oct = gdarr.BandReadAsArray(redB_oct, xoff_o, yoff_o, win_xsize_o, win_ysize_o)
nir_arr_oct = gdarr.BandReadAsArray(nirB_oct, xoff_o, yoff_o, win_xsize_o, win_ysize_o)
blue_arr_oct = gdarr.BandReadAsArray(blueB_oct, xoff_o, yoff_o, win_xsize_o, win_ysize_o)
green_arr_oct = gdarr.BandReadAsArray(greenB_oct, xoff_o, yoff_o, win_xsize_o, win_ysize_o)


# calculate NDVI using the matrix function
NDVI_oct = ((nir_arr_oct - red_arr_oct) / (nir_arr_oct + red_arr_oct))

# setting the threshold
NDVI_oct[NDVI_oct >= 0.4] = 1           # threshold for visualizing cropland areas
NDVI_oct[NDVI_oct < 0.4] = 0

# plot NDVI for oct
plt.subplot(2, 2, 2)
plt.imshow(NDVI_oct, cmap='gray')
plt.title('NDVI in October')


# getting annual croplands
NDVI_matrix = np.logical_and(NDVI_jun < 0.3, NDVI_oct > 0.4)

# plot NDVI for annual cropland
plt.subplot(2,2,3)
plt.imshow(NDVI_matrix, cmap='gray')
plt.title('Detection of annual crops \n with cloud cover')


# filtering out the cloud cover
median_filter = nd.median_filter(NDVI_matrix, size=5)
print(len(median_filter))
plt.subplot(2,2,4)
plt.imshow(median_filter, cmap='gray')
plt.title('Detection of annual crops \n without cloud cover')
plt.show()
print('Done')


# calculate the area of cropland in the median matrix
# count = 0
# for i in range(median_filter.shape[0]):
#     for j in range(median_filter.shape[1]):
#         if median_filter[i,j]==1:
#             count += 1
# print(count)

import itertools
counter = itertools.count(0)
area = [(next(counter)) for i in range(median_filter.shape[0]) for j in range (median_filter.shape[1]) if median_filter[i,j] == 1]
print("counter")


if raster_jun is not None:
    raster_jun = None
if raster_oct is not None:
    raster_oct = None
    print("file closed.")