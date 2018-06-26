from skimage import io,draw
import matplotlib.pyplot as plt 
import numpy as np

def drawLine2(image,color,startX,startY,endX,endY): 
    rows,cols,dims=image.shape
    ret_img = np.uint8(image)
    
    rr, cc = draw.line(startX,startY,endX,endY)
    ret_img[rr,cc]=color

    return ret_img 

img=io.imread('1.jpeg')

color = [255,255,0]
startX = 0
startY = 200
endX = 600
endY = 800

plt.figure(num=3,figsize=(8,8))
plt.subplot(1,2,1)
plt.title('origin image')
plt.imshow(img)

img2 = drawLine2(img,color,startX,startY,endX,endY)

plt.subplot(1,2,2)
plt.title('lined result')
plt.imshow(img2)
plt.show()