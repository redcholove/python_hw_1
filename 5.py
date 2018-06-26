from skimage import io,draw
import matplotlib.pyplot as plt 
import numpy as np
def drawCircle(image,color,center,raduis): 
    rows,cols,dims=image.shape
    ret_img = np.uint8(image)
    
    rr, cc = draw.circle(center[0], center[1],radius)# 
    draw.set_color(ret_img,[rr,cc],color)#

    return ret_img 

img=io.imread('1.jpeg')
plt.figure(num=4,figsize=(8,86))

color = [255,255,0]
center = [200,400]
radius = 100

plt.subplot(1,2,1)
plt.title('origin image')
plt.imshow(img)

img2 = drawCircle(img,color,center,radius)

plt.subplot(1,2,2)
plt.title('circle result')
plt.imshow(img2)
plt.show()