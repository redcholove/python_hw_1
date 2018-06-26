from skimage import io,draw
import matplotlib.pyplot as plt 
import numpy as np

def blendingImages(image1,image2,startX,startY):
    rows1,cols1,dims1=image1.shape
    rows2,cols2,dims2=image2.shape
    
    image11 = np.double(image1)
    image21 = np.double(image2)
    
    ret_img = np.uint8(255*np.ones((1000,1000,3)))
    for i in range(0, rows1): 
        for j in range(0,cols1): 
            for k in range(0,3):
                ret_img[i,j,k] = np.uint8(image11[i,j,k])

    for i in range(startY+0, startY+rows2): 
        for j in range(startX+0,startX+cols2):
            if (ret_img[i,j,0] == 255) and (ret_img[i,j,1] == 255) and ( ret_img[i,j,2] == 255):
                for k in range(0,3):
                    ret_img[i,j,k] = np.uint8(image21[i-startY,j-startX,k])
            else:
                for k in range(0,3):
                    ret_img[i,j,k] = np.uint8((ret_img[i,j,k]+image21[i-startY,j-startX,k])/2) 
    return ret_img

img=io.imread('1.jpeg')
img2=io.imread('2.jpeg')

startX = 100
startY = 200
img3 = blendingImages(img,img2,startX,startY)

plt.figure(num=1, figsize=(15,15))
plt.subplot(1,3,1)
plt.title('BoA')
plt.imshow(img)

plt.subplot(1,3,2)
plt.title('BoA2')
plt.imshow(img2)

plt.subplot(1,3,3)
plt.title('blend')
plt.imshow(img3)
plt.show()