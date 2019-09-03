import os
from osgeo import gdal, ogr, gdal_array as gdarr


#1
os.chdir(r"C:\Users\piscobexigacalistlf\Documents\ScientificGeocomputing\Assigments\3")
nlWindClass2Ds = gdal.Open('nl_cf.tif')

#2
nlWindClass2X = nlWindClass2Ds.RasterXSize
nlWindClass2Y = nlWindClass2Ds.RasterYSize
print("x size: ", nlWindClass2X, " y size: ", nlWindClass2Y)
rasterP = nlWindClass2Ds.GetProjection()
print("projection:", rasterP)
rasterG = nlWindClass2Ds.GetGeoTransform()
if rasterG is not None:
    print()
    print("top-left x:", rasterG[0], "top left y:", rasterG[3])
    print("pixel-size w-e:", rasterG[1],"pixel-size n-s:", rasterG[5])
    print("rotation x:", rasterG[2], "rotation y:", rasterG[4])
    print()
count = nlWindClass2Ds.RasterCount
print("There are " + str(count) + " bands")

#3
band = nlWindClass2Ds.GetRasterBand(1)
stats = band.GetStatistics(False, True)
print("min = %.2f max = %.2f mean = %.2f std = %.2f" % (stats[0], stats[1], stats[2], stats[3]))
print("no data value:", band.GetNoDataValue())
print()

#4
def rasterizeLayer(referenceRaster,layer):
    '''
    :param referenceRaster: An existing gdal raster to use as a reference
    :param layer: OGR vector layer to rasterize
    :return: A new numpy array with same size as the reference raster
    and same values as reference raster where there is a vector intersection.
    Outside the vector intersection this numpy array has value 0, in other words, the no data value is 0.
    '''
    #5
    driver=gdal.GetDriverByName('Mem')
    newRaster = driver.Create('', referenceRaster.RasterXSize, referenceRaster.RasterYSize, 1, gdal.GDT_Float32)
    newRaster.SetProjection(referenceRaster.GetProjection())
    newRaster.SetGeoTransform(referenceRaster.GetGeoTransform())
    newBand1 = newRaster.GetRasterBand(1)
    newBand1.SetNoDataValue(0)
    #6
    gdal.RasterizeLayer(newRaster, [1], layer, burn_values=[1], options=['ALL_TOUCHED=TRUE'])
    #7
    newPx = gdarr.DatasetReadAsArray(newRaster, 0, 0, newRaster.RasterXSize, newRaster.RasterYSize)
    nlWindPx = gdarr.DatasetReadAsArray(referenceRaster, 0, 0, referenceRaster.RasterXSize, referenceRaster.RasterYSize)
    #8
    windValues = newPx * nlWindPx
    return windValues

#9
parksDs = ogr.Open("windfarms.shp")
parksLayer = parksDs.GetLayer()

#10
for i in ['farm1','farm2','farm3','farm4':
    #11
    parksLayer.SetAttributeFilter("farms = '"+i+"'")
    #12
    windValues=rasterizeLayer(nlWindClass2Ds,parksLayer)
    #13
    windValues = windValues[windValues > 0]
    #14
    print("Stat values for",i,'--> Min:',windValues.m,'Max:',windValues.ma, 'Mean:',windValues.m)

#15
nlWindClass2Ds=None
parksDs=None