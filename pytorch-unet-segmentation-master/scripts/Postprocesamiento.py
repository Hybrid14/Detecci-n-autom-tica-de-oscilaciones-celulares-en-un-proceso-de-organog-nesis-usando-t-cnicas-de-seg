import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
from PIL import Image
import cv2

from tqdm.notebook import tqdm
def postprocesing(claudio_loader, modelo, paramThresh):
    model = torch.load(modelo, map_location=torch.device('cpu')).module.cpu()
    model.eval()
    img_list = []
    water_list = []
    kernel = np.ones((1, 1), np.uint8)
    kernel1 = np.ones((3, 3), np.uint8)
    for image, label in tqdm(claudio_loader):
        with torch.no_grad():
            output = model.forward(image)
            output = torch.argmax(output, dim=1).float()
            img = output[0].detach().numpy().astype('uint8')*255
            img_list.append(img)
            ret, bin_image = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            #closing = cv2.morphologyEx(bin_image, cv2.MORPH_CLOSE, kernel, iterations=1)
            sure_bg = cv2.dilate(bin_image, kernel1, iterations=1)#closing
            dist_transform = cv2.distanceTransform(bin_image, cv2.DIST_L2, 5)
            ret, sure_fg = cv2.threshold(dist_transform, paramThresh*dist_transform.max(), 255, 0)
            sure_fg = np.uint8(sure_fg)
            unknown = cv2.subtract(sure_bg, sure_fg)
            ret, markers = cv2.connectedComponents(sure_fg)
            markers_plus1 = markers + 1
            markers_plus1[unknown == 255] = 0
            watershed =  cv2.watershed(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), markers_plus1.copy())
            water_list.append(watershed)
        
    return(image,output,img_list,water_list,watershed)