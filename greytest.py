import cv2
import numpy as np


img = cv2.imread("images/train4.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(img, 115, 255, cv2.THRESH_BINARY)

cv2.imshow('gray', gray)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
