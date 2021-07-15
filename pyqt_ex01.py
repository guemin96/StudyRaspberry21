## QT6 베이스 프레임 소스
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 


app = QtWidgets.QApplication(sys.argv)


win = QMainWindow() #MyWindow말고 QMainWindow를 써도 됨
win.show()

app.exec_()
