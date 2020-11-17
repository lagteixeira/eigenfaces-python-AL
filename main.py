import glob
import cv2
import numpy as np
import sys


class FaceSet(object):
    def __init__(self, directory):
        self.directory = directory
        self.load_images()
        self.info()
        self.flatten()

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
        
    def flatten(self):
        imgs = np.array([cv2.imread(i, 1).flatten() for i in self.jpegs])
        self.imgs = imgs
        
    
            


