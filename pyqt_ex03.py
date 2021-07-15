## QT5 사용자 윈도우 구성 예제
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 

#윈도우 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self): #self => c#에서 this
        super().__init__()

        self.setWindowTitle("My QT5 Window") #제목표시줄
        self.setGeometry(300, 120, 400, 400) # x, y, width, height
        self.setWindowIcon(QIcon('./image/chart.png'))

        #label add
        self.label = QLabel('메시지: ',self)
        self.label.move(10,10)#좌표 위치
        #self.label.setGeometry(10,10,200,50)
        self.label.setFixedSize(200,50)


        #button add
        self.btn = QPushButton('Click',self)
        self.btn.move(10, 50)

        #signal(C# Event)
        self.btn.clicked.connect(self.btn_clicked)
    
    # 버튼 클릭 시그널(이벤트)
    def btn_clicked(self):
        self.label.clear()
        self.label.setText("메시지: 버튼 클릭")



app = QtWidgets.QApplication(sys.argv)

win = MyWindow() #MyWindow말고 QMainWindow를 써도 됨
win.show()
app.exec_()
