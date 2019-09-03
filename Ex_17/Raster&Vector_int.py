# Integrating gdal raster and vector data with numpy
# ex.17.1
from osgeo import ogr, gdal, gdal_array as gdarr
from matplotlib import pyplot as plt
import numpy as np
import os


dataDirectory = r'C:\GeoComProjects\Ex_17\data_integration'
os.chdir(dataDirectory)

# subsetting a raster based on a polygon
ds = gdal.Open('2014.tif')          # opens the raster file
nlprovPath = r'NL_provinces.shp'    # reads the shapefile

# cutlines for overijssel province
overTemperatureDs = gdal.Warp('temOverijssel.tif', ds, format="GTiff", dstSRS='EPSG:28992',
                              cutlineDSName=nlprovPath, cutlineWhere="Name_1 = 'Overijssel'",
                              cropToCutline = True)

# getting the temperature for the 1st day
overTempArray = gdarr.DatasetReadAsArray(overTemperatureDs, 0, 0, overTemperatureDs.RasterXSize,
                        overTemperatureDs.RasterYSize)
print(overTempArray.shape)
overTempArray[overTempArray == -9999] = None
plt.imshow(overTempArray[0,:,:])
plt.show()
print('Finished.')


# ex.17.2
# creates a susbset of overijssel in memory
overijssel_temp = gdal.Warp("", '2014.tif', format='Mem', dstSRS='EPSG:28992', cutlineDSName='NL_provinces.shp',
                            cutlineWhere="NAME_1 = 'Overijssel'", dstNodata=-9999, cropToCutline=True,
                            outputType=gdal.GDT_Float32)
overTempArray = gdarr.DatasetReadAsArray(overijssel_temp, 0, 0, overijssel_temp.RasterXSize, overijssel_temp.RasterYSize)

# rasterizing a vector layer
memDriver = gdal.GetDriverByName('Mem')
roadsRasterDs = memDriver.Create('', overijssel_temp.RasterXSize, overijssel_temp.RasterYSize,
                                 1, gdal.GDT_Float32)
roadsRasterDs.SetProjection(overijssel_temp.GetProjection())    # set projection
roadsRasterDs.SetGeoTransform(overijssel_temp.GetGeoTransform())    # set geotransform

# create 1 band and set the nodata value
outband1 = roadsRasterDs.GetRasterBand(1)
outband1.SetNoDataValue(0)

# open and get vector layer
roadsVectorDs = ogr.Open('ovRoads.geojson')
roadsLayer = roadsVectorDs.GetLayer()

# rasterize A1 road in Overijssel
gdal.RasterizeLayer(roadsRasterDs, [1], roadsLayer, options=['ATTRIBUTE=vehic_p_hour'])
roadsArray = gdarr.DatasetReadAsArray(roadsRasterDs, 0, 0, roadsRasterDs.RasterXSize, roadsRasterDs.RasterYSize)
roadsArray[roadsArray == 0] = None
plt.imshow(roadsArray)
plt.colorbar()
plt.show()


# ex.17.3
# creates a susbset of overijssel in memory
overijssel_temp = gdal.Warp("", '2014.tif', format='Mem', dstSRS='EPSG:28992', cutlineDSName='NL_provinces.shp',
                            cutlineWhere="NAME_1 = 'Overijssel'", dstNodata=-9999, cropToCutline=True,
                            outputType=gdal.GDT_Float32)
overTempArray = gdarr.DatasetReadAsArray(overijssel_temp, 0, 0, overijssel_temp.RasterXSize, overijssel_temp.RasterYSize)

# rasterizing a vector layer
memDriver = gdal.GetDriverByName('Mem')
roadsRasterDs = memDriver.Create('', overijssel_temp.RasterXSize, overijssel_temp.RasterYSize,
                                 1, gdal.GDT_Float32)
roadsRasterDs.SetProjection(overijssel_temp.GetProjection())    # set projection
roadsRasterDs.SetGeoTransform(overijssel_temp.GetGeoTransform())    # set geotransform

# create 1 band and set the nodata value
outband1 = roadsRasterDs.GetRasterBand(1)
outband1.SetNoDataValue(0)

# open and get vector layer
roadsVectorDs = ogr.Open('ovRoads.geojson')
roadsLayer = roadsVectorDs.GetLayer()
roadsLayer.SetAttributeFilter("id = 'A1'")

# rasterize A1 road in Overijssel
gdal.RasterizeLayer(roadsRasterDs, [1], roadsLayer, burn_values=[1], options=['ALL_TOUCHED=TRUE'])
roadsArray=gdarr.DatasetReadAsArray(roadsRasterDs, 0, 0, roadsRasterDs.RasterXSize,
                                    roadsRasterDs.RasterYSize)

print('A1 road shape:',roadsArray.shape)
print('Overijssel temperature shape:',overTempArray.shape)

# getting road temperature
roadsTemperature = roadsArray*overTempArray
print('A1 road temperatures shape:',roadsTemperature.shape)

# compute higher temperatures
roadsMaxTemperature = np.max(roadsTemperature, axis = 0)
print('A1 highest temperatures shape:',roadsMaxTemperature.shape)

# removing below 0 and 0 values
roadsMaxTemperature[roadsMaxTemperature <= 0] = None

minHigherTemp = np.nanmin(roadsMaxTemperature)
maxHigherTemp = np.nanmax(roadsMaxTemperature)

print('Highest temperatures recorded in 2014 in A1 in Overijssel; are between:', minHigherTemp,
      'and', maxHigherTemp)




# ex.17.4
# creating the new dataset
gtiffDriver = gdal.GetDriverByName('GTiff')
highestTempRoadsDs = gtiffDriver.Create('roadHighestTemp.tif', overTemperatureDs.RasterXSize,
                                        overTemperatureDs.RasterYSize, 1, gdal.GDT_Float32)
# set projection
highestTempRoadsDs.SetProjection(overTemperatureDs.GetProjection())

# set geotransform
highestTempRoadsDs.SetGeoTransform(overTemperatureDs.GetGeoTransform())

# create 1 band and set the no data value
highestTempRoadsband1 = highestTempRoadsDs.GetRasterBand(1)
highestTempRoadsband1.SetNoDataValue(-9999)

# add numpy into the band
highestTempRoadsband1.WriteArray(roadsMaxTemperature)

# clean and close the dataset
overTemperatureDs=None
roadsVectorDs=None
roadsRasterDs=None
highestTempRoadsband1.FlushCache()
highestTempRoadsDs = None
