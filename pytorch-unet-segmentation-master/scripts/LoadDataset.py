import torchvision
import torchvision.transforms.functional as TF
import torch
import torch.nn as nn
from torch.autograd import Variable

def loadData(path):
    
    class ImproveImageTransform:

        def __init__(self, contrast_factor=1, brightness_factor=1, saturation_factor=1):
            self.saturation_factor= saturation_factor # 0 will give a black and white image,1 will give the original image while 2 will enhance the saturation by a factor of 2.
            self.contrast_factor = contrast_factor
            self.brightness_factor = brightness_factor

        def __call__(self, x):
            x = TF.adjust_gamma(x, gamma=1)
            x = TF.adjust_saturation(x, self.saturation_factor) 
            x = TF.adjust_brightness(x, self.brightness_factor)
            x = TF.adjust_contrast(x, self.contrast_factor)
            return x

    my_transforms = torchvision.transforms.Compose([torchvision.transforms.Grayscale(),
                                                    torchvision.transforms.Pad(padding=(572-388)//2,
                                                                               padding_mode='reflect'),
                                                    torchvision.transforms.ToTensor()])

    claudio_dataset = torchvision.datasets.ImageFolder(path, transform=my_transforms)

    claudio_loader = torch.utils.data.DataLoader(dataset=claudio_dataset, batch_size=1, 
                                                 num_workers=0, shuffle=False)
    return(claudio_loader)