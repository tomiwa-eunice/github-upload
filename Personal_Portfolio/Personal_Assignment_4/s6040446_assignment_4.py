import os
from osgeo import gdal, gdal_array as gdarr
import matplotlib.pyplot as plt


dataDirectory = r'C:\GeoComProjects\Personal_Portfolio\Personal_Assignment_4'

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


# create matrix for water, urban and vegetation areas
# read new dataset as a numpy array
dataset = gdarr.DatasetReadAsArray(raster, xoff, yoff, win_xsize, win_ysize)
print(dataset)
print(dataset.shape)

# create water, urban and vegetation matrix in selected bands
# water matrix in red, green, blue and NIR bands
waterRband = dataset[3:4, 1232:1247, 342:362]      # water feature in red band
waterGband = dataset[2:3, 1232:1247, 342:362]      # water feature in green band
waterBband = dataset[1:2, 1232:1247, 342:362]      # water feature in blue band
waterNIRband = dataset[7:8, 1232:1247, 342:362]    # water feature in Near Infrared band

# vegetation matrix in red, green, blue and NIR bands
vegRband = dataset[3:4, 605:660, 1044:1087]      # vegetation feature in red band
vegGband = dataset[2:3, 605:660, 1044:1087]      # vegetation feature in green band
vegBband = dataset[1:2, 605:660, 1044:1087]      # vegetation feature in blue band
vegNIRband = dataset[7:8, 605:660, 1044:1087]    # vegetation feature in Near Infrared band

# urban matrix in red, green, blue and NIR bands
urbanRband = dataset[3:4, 942:953, 745:757]      # urban feature in red band
urbanGband = dataset[2:3, 942:953, 745:757]      # urban feature in green band
urbanBband = dataset[1:2, 942:953, 745:757]      # urban feature in blue band
urbanNIRband = dataset[7:8, 942:953, 745:757]    # urban feature in Near Infrared band


# reshaping the matrix to vectors
# water class for each selected bands
wr = waterRband.ravel()     # reshapes to a one dimension matrix
wg =  waterGband.ravel()
wb = waterBband.ravel()
wnir = waterNIRband.ravel()

# vegetation class for each selected bands
vr = vegRband.ravel()
vg = vegGband.ravel()
vb = vegBband.ravel()
vnir = vegNIRband.ravel()

# urban class for each selected bands
ur = urbanRband.ravel()
ug = urbanGband.ravel()
ub = urbanBband.ravel()
unir = urbanNIRband.ravel()


# showing the vectors in specific bands
# plotting feature classes in Red-Green band combination
plt.subplot(2,2,1)
plt.scatter(wr, wg, color='Blue', marker='o', label='Water')
plt.scatter(vr, vg, color='Green', marker='^', label='Vegetation')
plt.scatter(ur, ug, color='Gray', marker='*', label='Urban')
plt.xlabel('Red Band')
plt.ylabel('Green Band')
plt.legend(loc='lower right')
plt.colorbar()
plt.title('Feature Space Image \n for Red and Green Band Combination')


# plotting feature classes in Red-NIR band combination
plt.subplot(2,2,2)
plt.scatter(wr, wnir, color='Blue', marker='o', label='Water')
plt.scatter(vr, vnir, color='Green', marker='^', label='Vegetation')
plt.scatter(ur, unir, color='Gray', marker='*', label='Urban')
plt.xlabel('Red Band')
plt.ylabel('NIR Band')
plt.legend(loc='lower right')
plt.title('Feature Space Image \n for Red and NIR Band Combination')

# plotting feature classes in Green-NIR band combination
plt.subplot(2,2,3)
plt.scatter(wg, wnir, color='Blue', marker='o', label='Water')
plt.scatter(vg, vnir, color='Green', marker='^', label='Vegetation')
plt.scatter(ug, unir, color='Gray', marker='*', label='Urban')
plt.xlabel('Green Band')
plt.ylabel('NIR Band')
plt.legend(loc='lower right')
plt.title('Feature Space Image \n for Green and NIR Band Combination')


# plotting feature classes in Blue-NIR band combination
plt.subplot(2,2,4)
plt.scatter(wb, wnir, color='Blue', marker='o', label='Water')
plt.scatter(vb, vnir, color='Green', marker='^', label='Vegetation')
plt.scatter(ub, unir, color='Gray', marker='*', label='Urban')
plt.xlabel('Blue Band')
plt.ylabel('NIR Band')
plt.legend(loc='lower right')
plt.title('Feature Space Image \n for Blue and NIR Band Combination')

plt.show()



if raster is not None:
    raster = None
    print("file closed.")