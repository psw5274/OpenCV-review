import numpy as np
import cv2
import matplotlib.pyplot as mpt
from tkinter import *
from tkinter import filedialog

root = Tk()

root.fileName = filedialog.askopenfilename(filetypes = (("PNG", ".png"), ("All files", "*.*")))
originalImg = cv2.imread(root.fileName, cv2.IMREAD_GRAYSCALE)

fftImg = np.fft.fft2(originalImg)
fShift = np.fft.fftshift(fftImg)
originalMagnitudeSpectrum = 20 * np.log(np.abs(fftImg))
originalArrangedMagnitudeSpectrum = 20 * np.log(np.abs(fShift))

fIShift = np.fft.ifftshift(fShift)
inversedImg = np.abs(np.fft.ifft2(fIShift))

mpt.subplot(221), mpt.imshow(originalImg, cmap = 'gray'),
mpt.title('Original Image'), mpt.xticks([]), mpt.yticks([])
mpt.subplot(222), mpt.imshow(originalMagnitudeSpectrum , cmap = 'gray'),
mpt.title('Original Magnitude Spectrum'), mpt.xticks([]), mpt.yticks([])
mpt.subplot(223), mpt.imshow(originalArrangedMagnitudeSpectrum, cmap = 'gray'),
mpt.title('Original Arranged Magnitude Spectrum'), mpt.xticks([]), mpt.yticks([])
mpt.subplot(224), mpt.imshow(inversedImg, cmap = 'gray'),
mpt.title('Inversed Image'), mpt.xticks([]), mpt.yticks([])


mpt.show()
cv2.destroyAllWindows()