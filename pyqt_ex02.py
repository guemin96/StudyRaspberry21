## QT5 윈도우클래스 생성예제
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 

#윈도우 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QtWidgets.QApplication(sys.argv)

#button = QPushButton("Click me")
#button.show()
#label = QLabel("Hello QT5!")
#label.show()
win = MyWindow() #MyWindow말고 QMainWindow를 써도 됨
win.show()

app.exec_()
