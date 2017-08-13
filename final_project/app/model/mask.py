import cv2
import numpy as np
from numpy import *
import os


# create mask.tif file, which used for cov parameter calculation
def build(dir):
    if not os.path.isfile(dir + '/mask.tif'):
        files = os.listdir(dir)
        sum = np.array([])
        i_h = 0
        i_w = 0
        for file in files:
            if file.endswith(".tif"):
                img = cv2.imread(dir + '/' + file)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                img = cv2.Canny(img, 100, 200)
                i_h, i_w = img.shape
                data = img.flatten().astype(float)
                c = np.array([]).astype(float)
                if len(data) < len(sum):
                     c = sum.copy()
                     c[:len(data)] += data
                else:
                    c = data.copy()
                    c[:len(sum)] += sum
                sum = c

        max = np.amax(sum)
        min = np.amin(sum)

        for i in range(0, len(sum)):
            norm = (sum[i] - min) / (max - min)
            if norm > 0.1 and norm < 0.3:
                sum[i] = 255
            else:
                sum[i] = 0

        sum = sum.reshape((i_h, i_w))
        cv2.imwrite(dir + '/mask.tif', sum)




