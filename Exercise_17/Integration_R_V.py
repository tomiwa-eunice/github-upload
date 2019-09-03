# Integrating gdal raster and vector data with numpy
# ex.17.1
from osgeo import ogr, gdal, gdal_array as gdarr
from matplotlib import pyplot as plt
import numpy as np
import os


dataDirectory = r'C:\GeoComProjects\Exercise_17'
os.chdir(dataDirectory)

# subsetting a raster based on a polygon
ds = gdal.Open('2014.tif')      # opens the raster file
nlprovPath = r'NL_provinces.shp'    # reads the shapefile

# cutlines for overijssel province
overTemperatureDs = gdal.Wrap('temOverijssel.tif', ds, format="GTiff", dstSRS='EPSG:28992',
                              cutlineDSName=nlprovPath, cutlineWhere="Name_1 = 'Overijssel'",
                              cropToCutline = True)

# getting the temperature for the 1st day
overTempArray = gdarr.DatasetReadAsArray(overTemperatureDs, 0, 0, overTemperatureDs.RasterXSize,
                        overTemperatureDs.RasterYSize)
overTempArray[overTempArray == -9999] = None
plt.imshow(overTempArray[0,:,:])
plt.show()
print('Finished.')
