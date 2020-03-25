import numpy as np
import cv2
import matplotlib.pyplot as mpt
from tkinter import filedialog
from tkinter import *

root = Tk()

root.fileName = filedialog.askopenfilename(filetypes=(("JPG files", ".jpg"), ("All files", "*.*")))
cvGrayImg = cv2.imread(root.fileName, cv2.IMREAD_GRAYSCALE)

eqImg = cv2.equalizeHist(cvGrayImg)

cvHist1 = cv2.calcHist([cvGrayImg], [0], None, [256], [0, 256])
cvHist2 = cv2.calcHist([eqImg], [0], None, [256], [0, 256])

mpt.subplot(221), mpt.imshow(cvGrayImg, 'gray'), mpt.title('Source Image')
mpt.subplot(222), mpt.plot(cvHist1), mpt.title('OpenCV1 Histogram')
mpt.subplot(223), mpt.imshow(eqImg, 'gray'), mpt.title('equalized Image')
mpt.subplot(224), mpt.plot(cvHist2), mpt.title('OpenCV2 Histogram')
mpt.show()



cv.destroyAllWindows()