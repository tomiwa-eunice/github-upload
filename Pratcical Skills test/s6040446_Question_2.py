import numpy as np
from osgeo import ogr, gdal,osr, gdal_array as gdarr
import matplotlib.pyplot as plt

# # Question 2a
# # random integers in 3 dimensions
# list = np.random.randint(0, 255, 50000).reshape(50, 100, 10)
# image_arr = np.array(list)
# # display the 8th column and 4th band
# band_4 = image_arr[:, 7:8, 3]
# print("Values in the 8th column of the 4th band are: ", band_4)
# print(image_arr.shape)
#
#
# # Question 2b
# # maximum and minimum values per band
# image_max = image_arr[0:50, 0:100, :].max()
# image_min = image_arr[0:50, 0:100, :].min()
#
# print(image_min, image_max)
#
#
# # Question 2c
# # plotting Veluwe park
# veluwe_park = image_arr[30:81, 40:91, 1]
# # print(veluwe_park)
# plt.title('Veluwe Natural Park')
# plt.imshow(veluwe_park)
# plt.show()
#
#
#
# # Question 2d
# def add_value(arr):
#     """
#     adds 15 to every value below 55 in band 4
#     :param arr: numpy array of the image which will be iterated from
#     :return: a numpy array which as added the value 15 to values below 55
#     """
#     if arr[:,:,3].all() < 55:
#         return arr[:,:,3] + 15
#
# image_val = add_value(image_arr)
# print(image_val)
#
#

def generate_VI(image,band1,band2,band3,c0, c1, c2, c3):
    """
    Returns the VI value for the image using two bands.

    :param image: image to be accessed and read for image classification
    :param band1: first band read as a numpy array for VI analysis
    :param band2: second band read as a numpy array for VI analysis
    :return: the VI value for that particular image in a numpy array
    :assumptions: the function takes into assumption that band 1 and 2 are the best band for analysing VI at a
    particular threshold and the values in are of type float.
    :param c0:
    """

    imageBand1 = image.GetRasterBand(band1)
    imagePx1 = gdarr.BandReadAsArray(imageBand1, 0, 0, image.RasterXSize, image.RasterYSize)
    imagePx1 = imagePx1.astype(np.float32)
    imageBand1 = None

    imageBand2 = image.GetRasterBand(band2)
    imagePx2 = gdarr.BandReadAsArray(imageBand2, 0, 0, image.RasterXSize, image.RasterYSize)
    imagePx2 = imagePx2.astype(np.float32)
    imageBand2 = None

    imageBand3 = image.GetRasterBand(band3)
    imagePx3 = gdarr.BandReadAsArray(imageBand3, 0, 0, image.RasterXSize, image.RasterYSize)
    imagePx3 = imagePx3.astype(np.float32)
    imageBand3 = None

    # vi = (imagePx2 - imagePx1) / (imagePx2 + imagePx1)
    svi = (imagePx2 - imagePx1) / (imagePx2 + imagePx1 - imagePx3)
    evi = (c0 * (imagePx2 - imagePx1)) / (imagePx2 + c1 * imagePx1 - c2 *imagePx3 + c3)

    imagePx1 = None
    imagePx2 = None
    imagePx3 =None

    return evi


print((1*(4 - 2)) / (4 + 1*2 - 0 *3 + 0))
print(((4 - 2)) / (4 + 2))