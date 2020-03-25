import numpy as np
import cv2
import matplotlib.pyplot as mpt
from tkinter import *
from tkinter import filedialog

root = Tk()

root.fileName = filedialog.askopenfilename(filetypes = (("PNG", ".png"), ("All files", "*.*")))
originalImg = cv2.imread(root.fileName, cv2.IMREAD_GRAYSCALE)

mask = np.array(([0, 1, 0], [1, -4, 1], [0, 1, 0]), dtype=np.float32)
filteringImg = cv2.filter2D(originalImg, -1, mask)
#filteringImg = cv2.Laplacian(originalImg, -1)

mpt.subplot(121), mpt.imshow(originalImg, 'gray'), mpt.title('Original Image')
mpt.xticks([]), mpt.yticks([])
mpt.subplot(122), mpt.imshow(filteringImg, 'gray'), mpt.title('Laplacian Image')
mpt.xticks([]), mpt.yticks([])
mpt.show()

cv2.destroyAllWindows()