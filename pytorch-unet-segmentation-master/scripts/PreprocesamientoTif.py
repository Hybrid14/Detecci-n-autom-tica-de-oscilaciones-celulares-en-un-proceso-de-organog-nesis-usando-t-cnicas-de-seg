import cv2
from os.path import join
import matplotlib.pyplot as plt
def preprocesing(read,load,largo):
    r = c = 289
    w = h = 304
    original=[]
    preprocesada=[]
    for x in range (0,largo):
        if(x<10):
            i = cv2.imread(read+'00'+str(x)+'.png', cv2.IMREAD_GRAYSCALE)[0:289, 0:289]
        elif(x>=10 and x<100):
            i = cv2.imread(read+'0'+str(x)+'.png', cv2.IMREAD_GRAYSCALE)[0:289, 0:289]
        else:
            i = cv2.imread(read+str(x)+'.png', cv2.IMREAD_GRAYSCALE)[0:289, 0:289]
        original.append(i)
        i_p= cv2.bilateralFilter(i, 5, 75, 75)
        i_p= cv2.equalizeHist(i_p)
        preprocesada.append(i_p)
        if(x<10):
            plt.imsave(join(load, '00'+str(x)+".png"), i_p, cmap='gray_r')
        elif(x>=10 and x<100):
            plt.imsave(join(load, '0'+str(x)+'.png'), i_p, cmap='gray_r')
        else:
            plt.imsave(join(load, str(x)+".png"), i_p, cmap='gray_r')
    return(original,preprocesada)