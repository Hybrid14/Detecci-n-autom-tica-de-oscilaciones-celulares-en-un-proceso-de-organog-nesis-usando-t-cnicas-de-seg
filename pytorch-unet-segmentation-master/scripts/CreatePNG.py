from os.path import join
import matplotlib.pyplot as plt
def png(path,image_arrays):
    for x in range (0, 60):
        img = image_arrays[0, 0, 0, x, 0, :, :, 0]
        if(x<10):
            plt.imsave(join(path, "0"+str(x)+".png"), img, cmap='gray_r') #guarda en escala de grises invertido
        else:
            plt.imsave(join(path, str(x)+".png"), img, cmap='gray_r')
