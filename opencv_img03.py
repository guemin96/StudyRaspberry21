import cv2
import numpy as np

org = cv2.imread('./image/cat.jpeg')

h, w, c = org.shape

cropped = org[:, :int(w/2)]

cv2.imshow('Original',org) #이미지를 새창에 띄우기
cv2.imshow('Cropped', cropped) # 반으로 자른 이미지

cv2.waitKey(0)
cv2.destroyAllWindows()
