import numpy as np
import cv2
import matplotlib.pyplot as mpt
from tkinter import *
from tkinter import filedialog

root = Tk()

root.fileName = filedialog.askopenfilename(filetypes = (("PNG", ".png"), ("All files", "*.*")))
originalImg = cv2.imread(root.fileName, cv2.IMREAD_GRAYSCALE)

# 소벨 마스크의 x, y 방향 미분값을 구하여 기울기와 방향각 구함
# 기울기 크기가 방향각의 주변값 보다 작을 경우 에지 대상에서 제거
# 상한과 하한의 threshold를 두어 초과시 에지, 미만시 에지 제외, 중간은 주변에 자신 이상인 것이 있을 때 에지로 삼음

filteringImg = cv2.Canny(originalImg, 30, 200)

mpt.subplot(121), mpt.imshow(originalImg, 'gray'), mpt.title('Original Image')
mpt.xticks([]), mpt.yticks([])
mpt.subplot(122), mpt.imshow(filteringImg, 'gray'), mpt.title('Canny Image')
mpt.xticks([]), mpt.yticks([])
mpt.show()

cv2.destroyAllWindows()