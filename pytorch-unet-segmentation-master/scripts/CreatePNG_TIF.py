
from os.path import join
import matplotlib.pyplot as plt
def png(path,image_arrays):
    for x in range (len(image_arrays)):
        img = image_arrays[x]
        if(x<10):
            plt.imsave(join(path, "00"+str(x)+".png"), img, cmap='gray_r') #guarda en escala de grises invertido
        elif(x>=10 and x<100):
            plt.imsave(join(path, '0'+str(x)+'.png'), img, cmap='gray_r')
        else:
            plt.imsave(join(path, str(x)+".png"), img, cmap='gray_r')

