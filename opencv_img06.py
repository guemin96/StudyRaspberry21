import cv2
import numpy as np # C#의 리스트, 행렬이 포함되어 있지 않아,numpy

#이미지 로드 기본틀
## 이미지 대비
org = cv2.imread('./image/cat.jpeg')
gray = cv2.cvtColor(org,cv2.COLOR_BGR2GRAY)
enhanced = cv2.equalizeHist(gray)

cv2.imshow('gray',gray) #이미지를 새창에 띄우기
cv2.imshow('Enhance', enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()

