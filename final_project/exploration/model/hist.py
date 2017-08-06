from numpy import *
import cv2
import os


def build(folder):
    if not os.path.isfile(folder + '/hists.txt'):
        files = os.listdir(folder)
        h = open(folder + '/hists.txt', 'wt')
        for _file in files:
            if _file.endswith(".tif"):
                img = cv2.imread(folder + '/' + _file)
                gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                hist = cv2.calcHist([gray], [0], None, [7], [1, 256])
                new_line = _file + ' '
                arr = hist.ravel()
                for value in arr:
                    new_line += str(value) + ' '
                h.write(new_line + "\n")
        h.close()
