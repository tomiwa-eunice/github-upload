import os
from osgeo import gdal, ogr, gdal_array as gdarr
import matplotlib.pyplot as plt


# 1
# change to data directory
os.chdir(r"C:\GeoComProjects\Personal_Portfolio\Personal_Assignment_3")
nlWindClass2Ds = gdal.Open('nl_cf_250_class2.tif')      # opens raster dataset


# 2
# Getting the raster size in 2 dimensions
nlWindClass2X = nlWindClass2Ds.RasterXSize
nlWindClass2Y = nlWindClass2Ds.RasterYSize
print("x size: ", nlWindClass2X, " y size: ", nlWindClass2Y)

# getting projection and geotransform information
rasterP = nlWindClass2Ds.GetProjection()
print("projection:", rasterP)
rasterG = nlWindClass2Ds.GetGeoTransform()
if rasterG is not None:
    print()
    print("top-left x:", rasterG[0], "top left y:", rasterG[3])         # top-left coordinates
    print("pixel-size w-e:", rasterG[1], "pixel-size n-s:", rasterG[5]) # pixel size
    print("rotation x:", rasterG[2], "rotation y:", rasterG[4])         # rotation of the pixel
    print()

# number of bands
count = nlWindClass2Ds.RasterCount
print("There are " + str(count) + " bands")


# 3
# Access to band Information
band = nlWindClass2Ds.GetRasterBand(1)
stats = band.GetStatistics(False, True)         # determining band statistics
print("min = %.2f max = %.2f mean = %.2f std = %.2f" % (stats[0], stats[1], stats[2], stats[3]))
print("no data value:", band.GetNoDataValue())

# visualizing the raster image
# define the topleft pixels and window size
xoff = 0
yoff = 0
win_xsize = nlWindClass2X
win_ysize = nlWindClass2Y

cf_arr = gdarr.BandReadAsArray(band, xoff, yoff, win_xsize, win_ysize)      # read a single band as a two-dim array
cf_arr[cf_arr == -999.0] = None                                             # removes no data from the image plot

plt.imshow(cf_arr)
plt.colorbar()
plt.title('Raster Image showing \n Capacity Factor for The Netherlands')
plt.show()
print()


# 4
# defining a function for rasterizing
def rasterizeLayer(referenceRaster,layer):
    '''
    Returns the vector layer as a raster

    :param referenceRaster: An existing gdal raster to use as a reference
    :param layer: OGR vector layer to rasterize
    :type referenceRaster: osgeo.gdal.Dataset
    :type layer: osgeo.ogr.Layer
    :return: A new numpy array with same size as the reference raster
    and same values as reference raster where there is a vector intersection.
    Outside the vector intersection this numpy array has value 0, in other words, the no data value is 0.
    :rtype: numpy array
    '''
    # 5
    # creating a new raster
    driver = gdal.GetDriverByName('Mem')        # creates a new driver in memory
    # creates a new raster in the driver using the reference parameters
    newRaster = driver.Create('', referenceRaster.RasterXSize, referenceRaster.RasterYSize, 1, gdal.GDT_Float32)
    # set new raster projection and geotransform information as the reference raster
    newRaster.SetProjection(referenceRaster.GetProjection())
    newRaster.SetGeoTransform(referenceRaster.GetGeoTransform())
    newBand1 = newRaster.GetRasterBand(1)           # creates a band
    newBand1.SetNoDataValue(0)                      # set a pixel no data value to 0


    # 6
    # rasterizing the vector layer
    gdal.RasterizeLayer(newRaster, [1], layer, burn_values=[1], options=['ALL_TOUCHED=TRUE'])
    # with the "burn_values=[1]" all the pixel values where there is a vector intersection are assigned the value 1,
    # with the options "all_touched=true" all the pixels where the vector layer touches becomes rasterized.


    # 7
    # reads dataset as a two-dim array
    newPx = gdarr.DatasetReadAsArray(newRaster, 0, 0, newRaster.RasterXSize, newRaster.RasterYSize)
    nlWindPx = gdarr.DatasetReadAsArray(referenceRaster, 0, 0, referenceRaster.RasterXSize, referenceRaster.RasterYSize)


    # 8
    # creates a multiplication of the old and new raster array
    windValues = newPx * nlWindPx
    return windValues                                   # returns a numpy array when the function is called


# 9
# opens vector dataset
parksDs = ogr.Open("windfarms.shp")
parksLayer = parksDs.GetLayer()                         # obtaining the vector layer


# 10
for i in ['farm1', 'farm2', 'farm3', 'farm4']:          # access each feature in the farm list
    # 11
    parksLayer.SetAttributeFilter("farms = '"+i+"'")    # Filters each farm type attribute
    # 12
    # calls the function 'rasterizelayer' and rasterize the vector layer 'parkslayer'
    windValues = rasterizeLayer(nlWindClass2Ds, parksLayer)
    # 13
    # uses the boolean operator to check for windvalues greater than 0
    windValues = windValues[windValues > 0]
    # 14
    # prints the statistical values of the wind values for each farm type
    print("Stat values for", i, '--> Min:', windValues.min(), 'Max:', windValues.max(), 'Mean:', windValues.mean())


# 15
# create bar chart for wind values per farm
min_windValues = []
max_windValues = []
farms = ['farm1', 'farm2', 'farm3', 'farm4']
for i in farms:
    parksLayer.SetAttributeFilter("farms = '" + i + "'")
    windValues = rasterizeLayer(nlWindClass2Ds, parksLayer)
    windValues = windValues[windValues > 0]
    min_windValues.append(windValues.min())
    max_windValues.append(windValues.max())
print(max_windValues, min_windValues)

# create a stacked bar chart
plt.bar(farms,min_windValues, color='r', label='Min')           # creates a bar chart
plt.bar(farms, max_windValues, bottom=min_windValues, color='b', label='Max')   # creates a stacked bar chart
plt.xlabel('Farms')                                             # adds x label.
plt.xticks(farms, rotation=30)                                  # representation of the x-axis, rotate the labels
plt.ylabel('Wind values')                                       # adds y label.
plt.title('Statistical Values showing \n Minimum and Maximum Wind Values per Farm')     # adds title
plt.legend(loc='upper right')                                   # adds legend at upper right side
plt.grid(linestyle=':')
plt.show()


# 16
# flush cache and clean memory
nlWindClass2Ds = None
parksDs = None