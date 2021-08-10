import io
import sys
import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets # PyQtWebEngine 추가 설치 -->QtWebEngineWidgets

app = QtWidgets.QApplication(sys.argv)

m = folium.Map(location=[35.1175, 129.0903], zoom_start=12)

data = io.BytesIO()
m.save(data, close_file=False)

win = QtWebEngineWidgets.QWebEngineView()
win.setHtml(data.getvalue().decode())
win.resize(800,600)
win.show()

sys.exit(app.exec_())