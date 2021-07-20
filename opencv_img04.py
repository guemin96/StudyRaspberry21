import cv2
import numpy as np # C#의 리스트, 행렬이 포함되어 있지 않아,numpy

#이미지 로드 기본틀
## 이미지 흐리게 하기(Blur 블러)
# 선명하게
org = cv2.imread('./image/cat.jpeg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(org, (10, 10))
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharp =cv2.filter2D(org, -1, kernel)

cv2.imshow('Original',org) #이미지를 새창에 띄우기
cv2.imshow('Blur',blur) #흐리게 변경한 이미지
cv2.imshow('Sharp',sharp)#선명하게


cv2.waitKey(0)
cv2.destroyAllWindows()

