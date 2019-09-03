import matplotlib.pyplot as plt
import numpy as np
band1= np.random.random_integers(0,255,(10,20,1))
band2= np.random.random_integers(0,255,(10,20,1))
band3= np.random.random_integers(0,255,(10,20,1))
print(band1.shape)
plt.gray()
plt.subplot(4,1,1)
plt.imshow(band1[:,:,0])
plt.subplot(4,1,2)
plt.imshow(band2[:,:,0])
plt.subplot(4,1,3)
plt.imshow(band3[:,:,0])
# create an image with three bands
d=np.dstack((band1,band2,band3))
plt.subplot(4,1,4)
plt.imshow(d.astype(np.uint8))
plt.show()






