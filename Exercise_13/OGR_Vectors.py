# Gdal vector operations
# ex.13.1
from osgeo import ogr
from osgeo import osr
import os

dataDirectory = r'C:\GeoComProjects\Exercise_13\data_OGR'

os.chdir(dataDirectory)
# open dataset
datasource = ogr.Open('NL_provinces.shp')
print('file opened!')


# to get the driver name
driverType = datasource.GetDriver().GetName()
print('Driver name:', driverType)

# Accessing data source metedata
meta = datasource.GetMetadata()
print('vector metadata:', meta)

# getting data source layer count
layerCount = datasource.GetLayerCount()     # getting the no of layers
print('dataset layers:', layerCount)


# ex.13.2
# accessing the layer properties
layer = datasource.GetLayer(0)
layerDefinition = layer.GetLayerDefn()
fieldCount = layerDefinition.GetFieldCount()   # get no of attribute table fields
print('Number of fields:'+str(fieldCount))
for i in range(fieldCount):                    # iterate over the attribute table fields
    print('Attribute field:'+layerDefinition.GetFieldDefn(i).GetName())     #get field defn and its name

# getting layer extents
layerExtents = layer.GetExtent()
print('x_min=%.2f x_max=%.2f y_min=%.2f y_max=%.2f' % (layerExtents[0], layerExtents[1], layerExtents[2], layerExtents[3]))

# obtaining no of features
layerFeatureNum = layer.GetFeatureCount()
print('Number of features: '+str(layerFeatureNum))

# obtaining the spatial reference system
layerSRS = layer.GetSpatialRef()
print('Spatial Reference System (srs):'+str(layerSRS))


# ex.13.3
# access to layer feature data
for feature in layer:               # iterate over the features
    nameFeature = feature.GetFieldAsString('NAME_1')
    print('feature NAME_1:'+nameFeature)
    #alternative
    print(feature.GetField(1))

# getting only one feature
    print(layer.GetFeature(0).GetFieldAsString('NAME_1'))


# ex.13.4
# access to the feature
layer.SetAttributeFilter('NAME_1 = "Overijssel"')
for feature in layer:
    OverijsselFeature = feature
name = OverijsselFeature.GetField('NAME_1')
print('NAME_1 for selected feature:'+name)

OverijsselGeometry = OverijsselFeature.GetGeometryRef()         # extract the geometry

print('Type of Geometry: '+OverijsselGeometry.GetGeometryName())    # type of geometry

print('Geometry WKT: '+OverijsselGeometry.ExportToWkt())            # geometry as a text

area = OverijsselGeometry.Area()                    # get the area in projection units
print('Area is: '+str(area))

env = OverijsselGeometry.GetEnvelope()              # get the extent/bounding box/envelope
print('Feature extent: x_min = %.2f x_max = %.2f y_min = %.2f y_max = %.2f'
      % (env[0], env[1], env[2], env[3]))


# ex.13.5
# spatial analysis methods with ogr
bufferDistance = 5000
buffer = OverijsselGeometry.Buffer(bufferDistance)
print('Buffer geometry WKT: ' + str(buffer.ExportToWkt()))
print('Buffer geometry Json: ' + str(buffer.ExportToJson()))       # geometry buffer as a json
buffer_area = buffer.Area()
print((buffer_area))


# ex.13.6
# save data as a new shapefile
from osgeo import ogr
from osgeo import osr
import os

driver = ogr.GetDriverByName("ESRI Shapefile")      # save as a different file format

# create the data source
data_source = driver.CreateDataSource("Overijssel_buffer.shp")

# create the spatial reference, EPSG 28992
srs = osr.SpatialReference()
srs.ImportFromEPSG(28992)

# create the layer
layer = data_source.CreateLayer("Overijssel_buffer", srs, ogr.wkbPolygon)

# create field name (attribute 1)
field_name = ogr.FieldDefn("Name", ogr.OFTString)       # define the field
field_name.SetWidth(24)
layer.CreateField(field_name)                           # create the field in the layer

# create field area (attribute 2)
field_area = ogr.FieldDefn("Area", ogr.OFTReal)
field_area.SetWidth(32)
field_area.SetPrecision(2)                              # sets precision of the field type
layer.CreateField(field_area)

# define the first feature
feature = ogr.Feature(layer.GetLayerDefn())
feature.SetField("Name", 'Overijssel')
feature.SetField("Area", buffer_area)
feature.SetGeometry(buffer)                             # add geometry into the feature

layer.CreateFeature(feature)                            # assigns feature into the layer
feature = None                                          # dereference the feature
data_source = None                                      # save and close the data source


# ex.13.7
# extract geometry of Drenthe Province
layer = datasource.GetLayer(0)
layerDefinition = layer.GetLayerDefn()

layer.SetAttributeFilter("Name_1 = 'Drenthe'")
for feature in layer:
    DrentheFeature = feature
DrentheGeometry = DrentheFeature.GetGeometryRef()

# intersection between overijssel and drenthe
if buffer.Intersects(DrentheGeometry):
    intersection = buffer.Intersection(DrentheGeometry)
    print('Intersection between buffer and Drenthe:' + intersection.ExportToWkt())

intersectsOD = buffer.Intersects(DrentheGeometry)
print('Buffer intersects Drenthe: '+str(intersectsOD))

driver = ogr.GetDriverByName("ESRI Shapefile")

data_source = driver.CreateDataSource("Intersection.shp")

srs = osr.SpatialReference()
srs.ImportFromEPSG(28992)

layer = data_source.CreateLayer("Intersection", srs, ogr.wkbPolygon)

field_name = ogr.FieldDefn("Name", ogr.OFTString)
field_name.SetWidth(24)
layer.CreateField(field_name)

field_area = ogr.FieldDefn("Area", ogr.OFTReal)
field_area.SetWidth(32)
field_area.SetPrecision(2)
layer.CreateField(field_area)

feature = ogr.Feature(layer.GetLayerDefn())
feature.SetField("Name", 'Intersection')
feature.SetField("Area", intersection.Area())
feature.SetGeometry(intersection)

layer.CreateFeature(feature)
feature = None
data_source = None


if datasource is not None:
    datasource = None
    print('file closed!')     #to close the file