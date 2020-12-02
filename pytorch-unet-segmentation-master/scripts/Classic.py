import numpy as np
import cv2

def normalize_image(img):
    img = (img.copy()/img.max())*255
    return img.astype('uint8')

def denoise_image(img, median_kernel=5, bandwidth=30):
    # Filtro mediana para eliminar ruido impulsivo
    img = cv2.medianBlur(img, median_kernel)
    # Non-local mean denoising http://www.ipol.im/pub/art/2011/bcm_nlm/
    img = cv2.fastNlMeansDenoising(img, None, h=bandwidth, 
                                   templateWindowSize=7, searchWindowSize=21)
    return img

def get_binary_mask(img, block_size=21, close_iter=2):
    # Adaptive thresholding    
    binary_mask = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv2.THRESH_BINARY, block_size, 0)
    # Cerradura morfologica
    binary_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_CLOSE, 
                                   kernel=np.ones((3,3),np.uint8), 
                                   iterations=close_iter)
    return binary_mask

def do_watershed(img, binary_mask, marker_threshold=0.3):
    dist_transform = cv2.distanceTransform(binary_mask, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 
                                 marker_threshold*dist_transform.max(), 
                                 255, 0)
    ret, markers = cv2.connectedComponents(sure_fg.astype('uint8'))
    watershed =  cv2.watershed(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), markers.copy())
    return markers, watershed, dist_transform


    