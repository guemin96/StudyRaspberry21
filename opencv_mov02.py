import cv2
import numpy as np

# 카메라 기본 틀
cap = cv2.VideoCapture(0) #번호 0부터 +1 웹캠 열기
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200) # 넓이와 높이 수동변환
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)


# 무한 루프 (q버튼을 입력할 때까지)
while True:
    ret, frame = cap.read() #카메라 현재 영상 로드, frame에 저장, return은 true/false
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    if ret != True: break # return false면 루프 탈출

    # h, w, c 

    cv2.imshow('RealTime CAM',frame)  #로드한 영상을 창을 띄움
    cv2.imshow('Gray Result', gray)

    if cv2.waitKey(1) == ord('q'): # q를 누르면 루프 탈출
        break

cap.release()
cv2.destroyAllWindows()