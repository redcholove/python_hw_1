from skimage import io,draw
import matplotlib.pyplot as plt 
import numpy as np
def drawPolygon(image,color,colX,lineY): 
    rows,cols,dims=image.shape
    ret_img = np.uint8(image)
    
    rr, cc=draw.polygon(lineY,colX)# 
    draw.set_color(ret_img,[rr,cc],color)#

    return ret_img 

img=io.imread('1.jpeg')

color=[255,255,0] 
lineY=[200,200,600,500] #順時針(y軸4點)
colX=[200,600,500,300] #順時針(x軸4點)

plt.figure(num=5,figsize=(8,8))
plt.subplot(1,2,1)
plt.title('origin image')
plt.imshow(img)

img2 = drawPolygon(img,color,colX,lineY)

plt.subplot(1,2,2)
plt.title('result')
plt.imshow(img2)
plt.show()