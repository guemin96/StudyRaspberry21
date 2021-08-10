import pyzbar.pyzbar as pyzbar
import cv2
import time
from PIL import ImageFont, ImageDraw, Image
import numpy as np

cap = cv2.VideoCapture(0)
# PKNU2020Fighting!!
hashVal = 'D67C69FFACCF947DBEAD024F8FF722D0'
font = ImageFont.truetype('./fonts/NANUMGOTHIC.ttf', 20) # 글꼴파일을 불러옴

i = 0
while (cap.isOpened()):
    ret, img = cap.read()

    if not ret:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    decoded = pyzbar.decode(gray)
    qrcode_data = ''

    for d in decoded:
        x, y, w, h = d.rect

        qrcode_data = d.data.decode("utf-8")
        qr_type = d.type

        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        text = '%s (%s)' % (str(qrcode_data).encode('utf-8').decode('utf-8'), qr_type)
        draw.text((0, 0),  text, font=font, fill=(255,255,255,0))

        img = np.array(img_pil)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # print("{}".format(qrcode_data))
        # cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
        #             1, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        i += 1
        # print("{}".format(qrcode_data))
        cv2.imwrite('D:\\c_%03d.jpg' % i, img)

cap.release()
cv2.destroyAllWindows()