import cv2
import numpy as np # C#의 리스트, 행렬이 포함되어 있지 않아,numpy

#이미지 로드 기본틀
## 
org = cv2.imread('./image/피카츄.png')
gray = cv2.cvtColor(org,cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray,127,255,0)
cont, hirc = cv2.findContours(bny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(org, cont, -1,(0,255,0),1)
cv2.imshow('Thr',bny)
cv2.imshow('Result',org)


cv2.waitKey(0)
cv2.destroyAllWindows()

