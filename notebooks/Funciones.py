#!/usr/bin/env python
# coding: utf-8

# In[1]:


def normalize_image(img):
    img = (img/img.max())*255
    return img.astype('uint8')

def denoise_image(img, h=30):
    # Filtro mediana para eliminar ruido impulsivo
    img = cv2.medianBlur(img, 5)
    # Non-local mean denoising http://www.ipol.im/pub/art/2011/bcm_nlm/
    img = cv2.fastNlMeansDenoising(img, None, h=h, templateWindowSize=7, searchWindowSize=21)
    return img
def get_binary_mask(img):
    # Adaptive thresholding    
    binary_mask = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv2.THRESH_BINARY, 21, 0)
    # Cerradura morfologica
    binary_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_CLOSE, 
                                   kernel=np.ones((3,3),np.uint8), iterations = 4)
    return binary_mask
def get_markers(dist, threshold=0.3):
    ret, sure_fg = cv2.threshold(dist, threshold*dist.max(), 255, 0)
    ret, markers = cv2.connectedComponents(sure_fg.astype('uint8'))
    return markers
def watershed_pipeline(img, th=0.1):
    #img = denoise_image(img)
    #binary_mask = ~get_binary_mask(img)
    dist_transform = cv2.distanceTransform(img, cv2.DIST_L2, 5)
    markers = get_markers(dist_transform, threshold=th)
    watershed =  cv2.watershed(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), markers.copy())
    return markers, watershed


# In[ ]:




