from osgeo import ogr
from osgeo import osr
import os

# ex.13.8
# distances between vector features
dataDirectory = r'C:\GeoComProjects\Exercise_13\data_OGR'

os.chdir(dataDirectory)

open_polygons = ogr.Open('Texel_Polygons.shp')      # open polygon data source
target_polygons = open_polygons.GetLayer(0)         # load the polygon layer

open_points = ogr.Open('Texel_Points.shp')          # open the points data source
target_points = open_points.GetLayer(0)             # load points layer

# if open_polygons is not None:
#     open_polygons = None
#     print('file closed!')
#
# if open_points is not None:
#     open_points = None
#     print('file closed!')

T_PolygonF = target_polygons.GetFeatureCount()
print(T_PolygonF)

T_PolygonSRS = target_polygons.GetSpatialRef()
print(T_PolygonSRS)

T_PointsF = target_points.GetFeatureCount()
print(T_PointsF)

T_PointsSRS = target_points.GetSpatialRef()
print(T_PointsSRS)


# ex.13.9
# 25th point
points = target_points.GetFeature(24)
pointGeometry = points.GetGeometryRef()
print(pointGeometry)

# 2nd polygon feature
poly = target_polygons.GetFeature(1)
polyGeometry = poly.GetGeometryRef()
print(polyGeometry)

Dis = pointGeometry.Distance(polyGeometry)
print(Dis)


# ex.13.10 & ex.13.11
# iterate over the polygon layer to print the 1st field
layer = open_polygons.GetLayer(0)
layerDefinition = layer.GetLayerDefn()
for feature in layer:
    print(feature.GetField(0))
    print(pointGeometry.Distance(feature.GetGeometryRef()))


