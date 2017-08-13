import os
import cv2
import numpy as np


# flatten data file
def mask2flat(name):
    img = cv2.imread(name)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img.flatten()


# build cov file in directory with images and created mask
def build(dir):
    if not os.path.isfile(dir + '/cov.txt'):
        files = os.listdir(dir)
        output = open(dir + '/cov.txt', 'wt')
        mask = mask2flat(dir + '/mask.tif')
        for file in files:
            if file.endswith(".tif") and file != 'mask.tif':
                img = cv2.imread(dir + '/' + file)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                edges = cv2.Canny(img, 100, 200)
                im_ed = edges.flatten()
                cor = np.corrcoef(im_ed, mask)[1][0]
                output.write(file + ' ' + str(cor) + "\n")
        output.close()









