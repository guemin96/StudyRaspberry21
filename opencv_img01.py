import cv2
import numpy as np

org = cv2.imread('./image/cat.jpeg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h, w, c = org.shape
print('Width : {0}, Height : {1}, Channel : {2}'.format(w,h,c))
size_small = cv2.resize(org, dsize=(int(w/2), int(h/2)))

cv2.imshow('Original',org)
cv2.imshow('Gray',gray)
cv2.imshow('Resize',size_small)

cv2.waitKey(0)
cv2.destroyAllWindows()
