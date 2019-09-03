import os
from osgeo import gdal, ogr, gdal_array as gdarr
import matplotlib.pyplot as plt
import numpy as np

# import matplotlib.mpimg as img

dataDirecctory = r'C:\GeoComProjects\Georeferencing_LeastSquare'

# initialize dataset variable
raster = None

os.chdir(dataDirecctory)

#open the raster
raster = gdal.Open('28H.tif')

# get one band
band1 = raster.GetRasterBand(1)
band2 = raster.GetRasterBand(2)
band3 = raster.GetRasterBand(3)

xoff = 0
yoff = 0
win_xsize = raster.RasterXSize
win_ysize = raster.RasterYSize

# showing the image in 2D array
im_arr1 = gdarr.BandReadAsArray(band1, xoff, yoff, win_xsize, win_ysize)
im_arr2 = gdarr.BandReadAsArray(band2, xoff, yoff, win_xsize, win_ysize)
im_arr3 = gdarr.BandReadAsArray(band3, xoff, yoff, win_xsize, win_ysize)

# create a depth stack
d = np.dstack((im_arr1, im_arr2, im_arr3))

plt.imshow(d.astype(np.uint8))
plt.show()
print()


#coordinate transformation
# create RD New coordinates array
b = [251000, 487000, 259000, 487000, 259000, 476000]

rdCoord = np.array(b).reshape(6,1)
print(rdCoord)

# create image coordinates array
A = np.zeros((6, 6), dtype=np.float32)

A[0,0] = 360.125
A[0,1] = 329.981
A[0,2] = 1
A[1,3] = 360.125
A[1,4] = 329.125
A[1,5] = 1
A[2,0] = 2248.984
A[2,1] = 335.989
A[2,2] = 1
A[3,3] = 2248.984
A[3,4] = 335.989
A[3,5] = 1
A[4,0] = 2238.994
A[4,1] = 2939.996
A[4,2] = 1
A[5,3] = 2238.994
A[5,4] = 2939.996
A[5,5] = 1

# A = np.matrix([[359.448,329.844,1,0,0,0], [0,0,0,359.448,329.844,1], [2247.5,335.899,1,0,0,0], [0,0,0,2247.5,335.899,1], [2238.96,2939.02,1,0,0,0], [0,0,0,2238.96,2939.02,1]])
#
print(A)
# print(type(A))
#
#
# # getting transformation parameters
#
# x = np.linalg.inv(A) * rdCoord

xP = np.dot(np.linalg.inv(A),rdCoord)

print(xP)
print(xP.shape)


# Parameters array
B = xP.reshape(2,3)
B_mat = np.zeros((3, 3), dtype=np.float32)
B_mat[:2, :] = B
B_mat[2,2] = 1
# B1 = xP.reshape(3,2)
print(B_mat)


# new GCpoint
p = [348.985, 2931.936, 1]
vP = np.array(p).reshape(3,1)
print(vP)


# estimated points
# q1 = np.dot(B1, vP)
# print(q1)
# print(q1.shape)

q = np.dot(B_mat, vP)
print(q)
print(q.shape)


# Error
d = np.sqrt((q[0] - 251000)**2+(q[1] - 476000)**2)
print(d)


# coordinate transformation using least squares
# 1
# creating the b-matrix (real coordinates)
bls = [251000, 487000, 259000, 487000, 259000, 476000, 251000, 476000]
rdCoordls = np.array(bls).reshape(8,1)
print(rdCoordls)

# 2
# creating the A-matrix (image coordinates)
Als = np.zeros((8, 6), dtype=np.float32)

Als[0,0] = 360.125
Als[0,1] = 329.981
Als[0,2] = 1
Als[1,3] = 360.125
Als[1,4] = 329.125
Als[1,5] = 1
Als[2,0] = 2248.984
Als[2,1] = 335.989
Als[2,2] = 1
Als[3,3] = 2248.984
Als[3,4] = 335.989
Als[3,5] = 1
Als[4,0] = 2238.994
Als[4,1] = 2939.996
Als[4,2] = 1
Als[5,3] = 2238.994
Als[5,4] = 2939.996
Als[5,5] = 1
Als[6,0] = 348.985
Als[6,1] = 2931.936
Als[6,2] = 1
Als[7,3] = 348.985
Als[7,4] = 2931.936
Als[7,5] = 1

# print(Als)

# 3
Als_T = Als.transpose()     # transpose of A matrix
invAls = np.linalg.inv(np.dot(Als_T, Als))  # inverse of A-matrix and A transpose
Als_B = np.dot(Als_T, rdCoordls)        # product of A-matrix transpose and B-matrix

xls = np.dot(invAls, Als_B)
print(xls)

# 4
I_mat = np.identity(8)          # creating an identity matrix for I
# print(I_mat)
A1 = np.dot(Als, invAls)
A1_T = np.dot(A1, Als_T)
AID = I_mat - A1_T

# 5
# residuals
residuals =  np.dot(AID, rdCoordls)         # calculating the residuals
print(residuals)

# from functools import reduce
# even = lambda n : n%2 == 0
# myCoords = [(x,y) for x in range(1,11) for y in range(1,11) if even(x+y)]
# print(myCoords)
# print(myCoords.count(myCoords))
# print(type(myCoords))
#
# myMoves = [ (p,q) for p in myCoords for q in myCoords if p[0]+1==q[0] and abs(p[1]-q[1])==1 ]
# print(myMoves)