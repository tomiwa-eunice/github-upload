import os
from osgeo import gdal, ogr, gdal_array as gdarr
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

dataDirectory = r'C:\GeoComProjects\Image_Classification'

raster = None

# change to the data directory
os.chdir(dataDirectory)

# open the raster dataset
raster = gdal.Open('s2_25_sept_2016.img')

# getting raster information
xoff = 0
yoff = 0
win_xsize = raster.RasterXSize      # no of rows
win_ysize = raster.RasterYSize      # no of columns
count = raster.RasterCount          # no of bands


print('Number of rows: ', win_xsize)
print('Number of columns: ',win_ysize)
print('Number of bands: ',count)

# getting the red, green, blue and near infrared bands
redB = raster.GetRasterBand(3)
greenB = raster.GetRasterBand(2)
blueB = raster.GetRasterBand(1)
nirB = raster.GetRasterBand(7)

# read the selected bands as a numpy array
red_arr = gdarr.BandReadAsArray(redB, xoff, yoff, win_xsize, win_ysize)
green_arr = gdarr.BandReadAsArray(greenB, xoff, yoff, win_xsize, win_ysize)
blue_arr = gdarr.BandReadAsArray(blueB, xoff, yoff, win_xsize, win_ysize)
nir_arr = gdarr.BandReadAsArray(nirB, xoff, yoff, win_xsize, win_ysize)

# read the dataset in a two-dim array
dataset = gdarr.DatasetReadAsArray(raster, xoff, yoff, win_xsize, win_ysize)

# create a new driver
driver = gdal.GetDriverByName('GTiff')

# create a new raster dataset
newRaster = driver.Create('sentinel_2_2016.tif', dataset.shape[2], dataset.shape[1], 4, gdal.GDT_Float32)

# set projection and geotransform information for the new raster
prj = raster.GetProjection()
newRaster.SetProjection(prj)
newRaster.SetGeoTransform(raster.GetGeoTransform())


# create and save the selected bands as a 3-dim matrix
# newBands = np.zeros((win_ysize, win_xsize, 4), dtype=np.float32)
# newBands[:, :, 0] =  red_arr
# newBands[:, :, 1] = green_arr
# newBands[:, :, 2] =  blue_arr
# newBands[:, :, 3] =  nir_arr
#
# # creating a tiff file for the
# for i in range(1, 5):
#     newBand = newRaster.GetRasterBand(i)
#     newBand.WriteArray(newBands[:, :, i-1])
#     print(i)
#     newBand.FlushCache()
#     newBand = None
# print('Finished')

newBand = newRaster.GetRasterBand(1)
newBand.WriteArray(red_arr)
newBand.FlushCache()

newBand = newRaster.GetRasterBand(2)
newBand.WriteArray(green_arr)
newBand.FlushCache()

newBand = newRaster.GetRasterBand(3)
newBand.WriteArray(blue_arr)
newBand.FlushCache()

newBand = newRaster.GetRasterBand(4)
newBand.WriteArray(nir_arr)
newBand.FlushCache()
newBand = None
print('Finished')


# create matrix for water, urban and vegetation areas
# open new raster dataset
newRaster = gdal.Open('sentinel_2_2016.tif')
print(newRaster)

# getting new raster information
new_xoff = 0
new_yoff = 0
new_win_xsize = newRaster.RasterXSize
new_win_ysize = newRaster.RasterYSize

# read new dataset as a numpy array
newDataset = gdarr.DatasetReadAsArray(newRaster, new_xoff, new_yoff, new_win_xsize, new_win_ysize)
print(newDataset)
print(newDataset.shape)


water = newDataset[:, 1179:1195, 23:57]
print(water)

vegetation = newDataset[:, 1250:1253, 220:227]
print(vegetation)

urban = newDataset[:, 706:711, 394:403]
print(urban)

# create water, urban and vegetation matrix in selected bands
# water matrix in red, green, blue and NIR bands
waterRband = dataset[3:4, 1179:1195, 23:57]      # water feature in red band
waterGband = dataset[2:3, 1179:1195, 23:57]      # water feature in green band
waterBband = dataset[1:2, 1179:1195, 23:57]      # water feature in blue band
waterNIRband = dataset[7:8, 1179:1195, 23:57]    # water feature in Near Infrared band

# vegetation matrix in red, green, blue and NIR bands
vegRband = dataset[3:4, 1250:1253, 220:227]      # vegetation feature in red band
vegGband = dataset[2:3, 1250:1253, 220:227]      # vegetation feature in green band
vegBband = dataset[1:2, 1250:1253, 220:227]      # vegetation feature in blue band
vegNIRband = dataset[7:8, 1250:1253, 220:227]    # vegetation feature in Near Infrared band

# urban matrix in red, green, blue and NIR bands
urbanRband = dataset[3:4, 706:711, 394:403]      # urban feature in red band
urbanGband = dataset[2:3, 706:711, 394:403]      # urban feature in green band
urbanBband = dataset[1:2, 706:711, 394:403]      # urban feature in blue band
urbanNIRband = dataset[7:8, 706:711, 394:403]    # urban feature in Near Infrared band



















if raster is not None:
    raster = None
    print("file closed.")



