from skimage import io,draw
import matplotlib.pyplot as plt 
import numpy as np

def drawLine(image,color,linestep): 
    rows,cols,dims=image.shape 
    ret_img = np.uint8(image)
    
    for i in range(linestep, rows, linestep): 
        for j in range(0,cols):
            for k in range(0,3):
                ret_img[i,j,k] = np.uint8(color[k])

    for i in range(0,rows):
        for j in range(linestep,cols,linestep):
            for k in range(0,3):
                ret_img[i,j,k] = np.uint8(color[k])
    return ret_img 

img=io.imread('1.jpeg')

color = [255,255,0]
step = 20

plt.figure(num=2,figsize=(8,8))
plt.subplot(1,2,1)
plt.title('origin image')
plt.imshow(img)

img2 = drawLine(img,color,step)

plt.subplot(1,2,2)
plt.title('lined result')
plt.imshow(img2)
plt.show()