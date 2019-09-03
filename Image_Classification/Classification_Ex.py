import os
from osgeo import gdal, ogr, gdal_array as gdarr
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

dataDirectory = r'C:\GeoComProjects\Image_Classification'

raster = None

os.chdir(dataDirectory)

raster = gdal.Open('s2_25_sept_2016.img')

# getting the bands
xoff = 0
yoff = 0
win_xsize = raster.RasterXSize      # no of rows
win_ysize = raster.RasterYSize      # no of columns
count = raster.RasterCount          # no of bands
dataset = gdarr.DatasetReadAsArray(raster, xoff, yoff, win_xsize, win_ysize)

# plt.show()
# print('Done')

print('Number of rows: ', win_xsize)
print('Number of columns: ',win_ysize)
print('Number of bands: ',count)

# get the red and near infrared bands
redB = raster.GetRasterBand(3)
nirB = raster.GetRasterBand(7)
blueB = raster.GetRasterBand(1)
greenB = raster.GetRasterBand(2)

# read the band as a numpy array
red_arr = gdarr.BandReadAsArray(redB, xoff, yoff, win_xsize, win_ysize)
nir_arr = gdarr.BandReadAsArray(nirB, xoff, yoff, win_xsize, win_ysize)
blue_arr = gdarr.BandReadAsArray(blueB, xoff, yoff, win_xsize, win_ysize)
green_arr = gdarr.BandReadAsArray(greenB, xoff, yoff, win_xsize, win_ysize)

# RGB_mat = np.zeros((win_ysize, win_xsize, 3), dtype=float)
#
# RGB_mat[:, :, 0] = red_arr / pow(2, 11)
# RGB_mat[:, :, 1] = green_arr / pow(2, 11)
# RGB_mat[:, :, 2] = blue_arr / pow(2, 11)

composite = np.dstack((red_arr, blue_arr, green_arr))
scale = composite/pow(2, 12)

plt.imshow((scale*255).astype(np.uint8))
plt.show()


# method 1
# calculate NDVI using the matrix function
NDVI = ((nir_arr - red_arr) / (nir_arr + red_arr))

# setting the threshold
NDVI[NDVI >= 0.7] = 1
NDVI[NDVI < 0.7] = 0

# plot NDVI
plt.imshow(NDVI, cmap='gray')
plt.show()
print('Done')


# method 2
# calculate NDVI using the iteration
# define the NVDI function
def ndviVal(R, NIR, X, Y):
    """

    :param R:
    :param NIR:
    :param X:
    :param Y:
    :return:
    """
    # my_vals = ((NIR[X,Y] - R[X,Y]) / (NIR[X,Y] + R[X,Y]))
    nir32 = NIR.astype(np.float32)
    r32 = R.astype(np.float32)
    my_vals = ((nir32[X, Y] - r32[X, Y]) / (nir32[X, Y] + r32[X, Y]))
    return my_vals


NDVI_mat = np.zeros((win_ysize, win_xsize), dtype=np.float32)
print(NDVI_mat)
print(NDVI_mat.shape)

for i in range (0, win_ysize):
    for j in range (0, win_xsize):
        NDVI_mat[i, j] = ndviVal(red_arr, nir_arr, i, j)
        # print(NDVI_mat[i,j])

NDVI_mat[NDVI_mat >= 0.7] = 1
NDVI_mat[NDVI_mat < 0.7] = 0

# plot NDVI
plt.imshow(NDVI_mat, cmap='gray')
plt.show()
print('Done')


if raster is not None:
    raster = None
    print("file closed.")



# assignment things
# newBand = newRaster.GetRasterBand(1)
# newBand.WriteArray(red_arr)
# newBand.FlushCache()
#
# newBand = newRaster.GetRasterBand(2)
# newBand.WriteArray(green_arr)
# newBand.FlushCache()
#
# newBand = newRaster.GetRasterBand(3)
# newBand.WriteArray(blue_arr)
#
# newBand = newRaster.GetRasterBand(4)
# newBand.WriteArray(nir_arr)
# newBand.FlushCache()
# newBand = None
# print('Finished')