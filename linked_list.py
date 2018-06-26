from skimage import io,draw
import matplotlib.pyplot as plt 
import numpy as np

def blurImage(image):
    rows,cols,dims=image.shape
    image2 = np.double(image)
    ret_img = np.uint8(255*np.ones((rows,cols,dims))) 
    for i in range(1, rows-1):
        for j in range(1,cols-1): 
            for k in range(0,3):
                sum = image2[i,j,k]+image2[i-1,j,k]+image2[i,j-1,k]+image2[i+1,j,k]+image2[i,j+1,k]
                average = sum/5
                ret_img[i,j,k] = np.uint8(average) 
    return ret_img

img=io.imread('1.jpeg')

plt.figure(num=0, figsize=(8,8))
plt.subplot(1,2,1)
plt.title('origin image')
plt.imshow(img)

img2 = blurImage(img)

plt.subplot(1,2,2)
plt.title('canvas result')
plt.imshow(img2)
plt.show()

