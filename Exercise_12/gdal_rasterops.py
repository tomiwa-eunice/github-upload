# ex.12.1
# open a gdal raster dataset
from osgeo import gdal
from osgeo import gdal_array as gdarr
import os

d_directory = r'C:\GeoComProjects\Exercise_12'

# initialize dataset variable
raster_set = None
# change to the data directory
os.chdir(d_directory)
# open dataset
raster_set = gdal.Open('2014.tif')
print('file opened')
if raster_set is not None:
    raster_set = None
    print('file is closed')

raster_set = gdal.Open('2014.tif')
# driver name
driverType = raster_set.GetDriver().LongName
print('driver name:', driverType)

# raster size
x = raster_set.RasterXSize
y = raster_set.RasterYSize
print('x size:', x, 'y size:', y)

# spatial projection
p = raster_set.GetProjection()
print('projection:', p)

# Geo-transform Information - getting the 6 Geo-transform Coefficients/parameters
g = raster_set.GetGeoTransform()
if g is not None:
    print('top left x:', g[0], 'top left y:', g[3])             # Top left coordinates
    print('pixel size w-e:', g[1], 'pixel size n-s:', g[5])     # Pixel size
    print('rotation x:', g[2], 'rotation y:', g[4])             # Rotation

# Number of bands
c_bands = raster_set.RasterCount
print('There are ' + str(c_bands) + ' bands')


# ex.12.2
# accessing day 1(band 1) information and statistics
# information
band = raster_set.GetRasterBand(1)      # opens the first band
min = band.GetMinimum()
max = band.GetMaximum()
print('min value:', min, 'max value:', max)

# statistics
stats = band.GetStatistics(False, True)
# parameter 1: If TRUE statistics may be computed based on overviews.
# parameter 2: If FALSE statistics will only be returned without rescanning the image

print('min = %.2f max = %.2f mean = %.2f std = %.2f'    # gets statistics of the band
      % (stats[0], stats[1], stats[2], stats[3]))
print('no data value:', band.GetNoDataValue())         # determines the no data value
print('number of overviews:', band.GetOverviewCount())


# ex.12.3
# extracting the subset of one band
band = raster_set.GetRasterBand(1)
xoff = 0            # gets the position of the pixel
yoff = 0
win_xsize = 273     # gets the size of the pixel
win_ysize = 101

# read a single band as a 2d array
px = gdarr.BandReadAsArray(band, xoff, yoff, win_xsize, win_ysize)
print(type(px))
print('shape:', px.shape)
print('topleft:', px[0, 0])
print('bottomright:', px[-1, -1])


# ex.12.4
# extracting information for Amsterdam
band_A = raster_set.GetRasterBand(1)
xoff = 0            # gets the position of the pixel
yoff = 0
win_xsize = 200     # gets the size of the pixel
win_ysize = 200
# saving a gdal raster image
arr = gdarr.BandReadAsArray(band, 0, 0, 200, 200)
driver = raster_set.GetDriver()     # use the same format as the original image
raster_set1 = driver.Create('2014_Amsterdam.tif', arr.shape[1], arr.shape[0],
                            1, gdal.GDT_Float32)
prj = raster_set.GetProjection()        # define new raster dataset proj. & geotransform
raster_set1.SetProjection(prj)
raster_set1.SetGeoTransform(raster_set.GetGeoTransform())

newBand = raster_set1.GetRasterBand(1)  # get band 1 so we can fill it with data
newBand.WriteArray(arr)                 # write the array to the band
newBand.SetNoDataValue(-9999)           # set a pixel nodata value
newBand.FlushCache()                    # flush the cache and clean memory
newBand = None
print('Finished')


# ex.12.5
band_A_stack = gdarr.DatasetReadAsArray(raster_set, 0, 0, 200, 200)
# day 1, position 0,0
print('Temperature value is', band_A_stack[0, 0, 0])
# day 31, position 100,100
print('Temperature value is', band_A_stack[30, 100, 100])
# day 59, position 78,150
print('Temperature value is', band_A_stack[58, 150, 78])
# day 90, position 186, 180
print('Temperature value is', band_A_stack[89, 180, 186])
# day 120, position 20,160
print('Temperature value is', band_A_stack[119, 160, 20])
# day 151, position 100,100
print('Temperature value is', band_A_stack[150, 100, 100])
# day 365, position 78,150
print('Temperature value is', band_A_stack[364, 150, 78])


# ex.12.6
# extraction of subset using pixel offset calculations
band_E = raster_set.GetRasterBand(1)
E_xoff = 100
E_yoff = 40
E_win_xsize = 200
E_win_ysize = 200

arr_E = gdarr.BandReadAsArray(band_E, 100, 40, 200, 200)
driver = gdal.GetDriverByName('GTiff')
raster_set2 = driver.Create('2014_Enschede.tif', arr_E.shape[1], arr_E.shape[0],
                            1, gdal.GDT_Float32)
prj_1 = raster_set2.GetProjection()
raster_set2.SetProjection(prj_1)
gt = raster_set2.GetGeoTransform()
newTLCoord = gdal.ApplyGeoTransform(gt, 100, 40)
raster_set2.SetGeoTransform([newTLCoord[0], 1000, 0, newTLCoord[1], 0, -1000])
newBand2 = raster_set2.GetRasterBand(1)
newBand2.WriteArray(arr_E)
newBand2.SetNoDataValue(band_E.GetNoDataValue())
newBand2.FlushCache()
newBand2 = None
print('Finished')



# ex.12.7
# use of translate and wrap
#12.8
# translate
import matplotlib.pyplot as plt


# translate amsterdam region
raster = gdal.Open('2014.tif')
newDataset = gdal.Translate('amsterdam_2014.tif', raster, format="GTiff",
                            srcWin=[0, 0, 200, 200])
nBand = newDataset.GetRasterBand(1)
px = gdarr.BandReadAsArray(nBand, 0, 0, newDataset.RasterXSize, newDataset.RasterYSize)
px[px==-9999] = None
plt.imshow(px)
plt.show()
print('Finished')


#translate enschede region
raster1 = gdal.Open('2014.tif')
newDataset1 = gdal.Translate('enschede_2014.tif', raster1, format="GTiff",
                            srcWin=[100, 40, 200, 200])
nBand1 = newDataset1.GetRasterBand(1)
px1 = gdarr.BandReadAsArray(nBand1, 0, 0, newDataset1.RasterXSize, newDataset1.RasterYSize)
px1[px1==-9999] = None
plt.imshow(px1)
plt.show()
print('Finished')


# ex.12.9
# warp
w_raster = gdal.Open('2014.tif')
w_dataset = gdal.Warp('', w_raster, format='Mem', dstSRS='EPSG:4326')

w_band = w_dataset.GetRasterBand(1)
px2 = gdarr.BandReadAsArray(w_band, 0, 0, w_dataset.RasterXSize, w_dataset.RasterYSize)
px2[px2==-9999] = None
plt.imshow(px2)
plt.show()
print('Finished')