import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

# 카메라 기본 틀
# 영상 자르기q
cap = cv2.VideoCapture(0) #번호 0부터 +1 웹캠 열기
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 520) # 넓이와 높이 수동변환
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)

#나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf',20)

# 무한 루프 (q버튼을 입력할 때까지)
while True:
    ret, frame = cap.read() #카메라 현재 영상 로드, frame에 저장, return은 true/false
    h, _, _= frame.shape
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')

    if ret != True: break # return false면 루프 탈출

    frame = Image.fromarray(frame) #글자출력을 위해 변환
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10,(h-40)),text='실시간 웹캠 - {0}'.format(currDateTime),font=font, fill=(255,255,0))
    frame = np.array(frame)

    cv2.imshow('RealTime CAM',frame)  #로드한 영상을 창을 띄움

    if cv2.waitKey(1) == ord('q'): # q를 누르면 루프 탈출
        break

cap.release()
cv2.destroyAllWindows()