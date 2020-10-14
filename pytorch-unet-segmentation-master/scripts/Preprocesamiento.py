import cv2
from os.path import join
import matplotlib.pyplot as plt
def preprocesing(read,load):
    r = c = 190
    w = h = 388
    original=[]
    preprocesada=[]
    for x in range (0, 60):
        i = cv2.imread(read+str(x)+'.png', cv2.IMREAD_GRAYSCALE)[r:r+h, c:c+w]
        original.append(i)
        i_p= cv2.bilateralFilter(i, 5, 75, 75)
        i_p= cv2.equalizeHist(i_p)
        preprocesada.append(i_p)
        plt.imsave(join(load, str(x)+".png"), i_p, cmap='gray')
    return(original,preprocesada)