from skimage import io,draw
import matplotlib.pyplot as plt 
import numpy as np
def drawPyramid(canvasSize):
    ret_img = np.uint8(255*np.ones((canvasSize[0],canvasSize[1],3)))
    
    for index in range(25,0,-1):
        color = [index*10, index*5, index] 
        lineY=[0,0,index*10,index*10] 
        colX=[0,index*10,index*10,0]
        rr, cc=draw.polygon(lineY,colX) 
        draw.set_color(ret_img,[rr,cc],color)
    return ret_img 

plt.figure(num=6,figsize=(8,8)) 
canvasSize=[500,500]

img = drawPyramid(canvasSize)

plt.imshow(img)
plt.show()