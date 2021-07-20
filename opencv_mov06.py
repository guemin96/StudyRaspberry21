import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

# 카메라 기본 틀
# 영상 캡쳐, 녹화
cap = cv2.VideoCapture(0) #번호 0부터 +1 웹캠 열기
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 520) # 넓이와 높이 수동변환
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)

# 나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf',20)
# 영상 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID') # H263
is_record = False   # 녹화상태


# 무한 루프 (q버튼을 입력할 때까지)
while True:
    ret, frame = cap.read() #카메라 현재 영상 로드, frame에 저장, return은 true/false
    h, w, _= frame.shape
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDateTime = now.strftime('%Y%m%d_%H%M%S') #20210720_164725

    if ret != True: break # return false면 루프 탈출

    frame = Image.fromarray(frame) #글자출력을 위해 변환
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10,(h-40)),text='실시간 웹캠 - {0}'.format(currDateTime),font=font, fill=(255,255,0))
    frame = np.array(frame)

    key = cv2.waitKey(1)
    if key == ord('q'): break #q는 종료
    elif key == ord('c'): #c는 화면캡쳐
        cv2.imwrite('./capture/img_{}.png'.format())
        print('이미지 저장 완료')
    elif key == ord('r'):
        if(is_record==False):
            is_record = True
            video = cv2.VideoWriter('record_{0}.avi'.format(fileDateTime),fourcc, 20, (w,h))
            print('녹화 시작')
        elif(is_record==True):
            is_record = False
            video.release() # 객체 해제
            print('녹화 완료')

    if is_record:
        video.write((frame))
        cv2.circle(img=frame, center=((w-20),15), radius=5, color=(0,0,255), thickness=3)
    cv2.imshow('RealTime CAM',frame)  #로드한 영상을 창을 띄움

cap.release()
cv2.destroyAllWindows()