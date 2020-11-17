import glob
import cv2
import numpy as np
import sys
from skimage import img_as_float, img_as_ubyte


class FaceSet(object):
    def __init__(self, directory):
        self.directory = directory
        self.load_images()
        self.info()
        self.recenter()
        self.get_average()

    def load_images(self):
        self.jpegs = glob.glob(self.directory + '/*.jpeg')
        imgs = np.array([cv2.imread(i, 1) for i in self.jpegs])
        self.imgs = imgs

    def info(self):
        min_rows, min_cols = sys.maxsize, sys.maxsize
        max_rows, max_cols = 0, 0
        for (i, image) in enumerate(self.imgs):
            r, c = image.shape[0], image.shape[1]
            min_rows = min(min_rows, r)
            max_rows = max(max_rows, r)
            min_cols = min(min_cols, c)
            max_cols = max(max_cols, c)
        self.min_rows = min_rows
        self.min_cols = min_cols
        print("\n==> Least common image size:", min_rows, "x", min_cols, "pixels")
        
    def recenter(self):
        images = self.imgs
        for (i, image) in enumerate(images):
            r, c = image.shape[0], image.shape[1]
            images[i] = image.flatten()[int((r*c - self.min_rows*self.min_cols)/2):int((r*c + self.min_rows*self.min_cols)/2)]
        self.imgs = images
    
    def get_average(self):
        images = self.imgs
        for (i, image) in enumerate(self.imgs):
            images[i] = img_as_float(image)
        self.average = img_as_ubyte(np.average(images))
        return self.average
        
    
            


