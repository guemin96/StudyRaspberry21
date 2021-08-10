from flask import Flask
import folium
import pandas as pd 

# pandas 라이브러리로 csv 파일 읽기 
df = pd.read_csv('./Map/gps.csv')

# 읽은 csv에서 Lat과, Lon을 [Lat, Lon] 리스트 형식으로 만들기
lines = df[['Lat', 'Lon']].values[:].tolist()

app = Flask(__name__)

# Flask 웹서버 
@app.route('/')
def index():
    # 지도 시작 위도 경도 지정 
    start_coords = (35.11744755557854, 129.09058121349395)

    # 지도의 시작 지점과 확대 비율을 정해서 지도를 띄우기 
    folium_map = folium.Map(location=start_coords, zoom_start=18)

    # location에 lines 리스트를 통해 위도 경도를 넣고, add_to로 계속 추가하는 형식
    folium.PolyLine(locations = lines).add_to(folium_map)
    return folium_map._repr_html_()

if __name__ == '__main__':
    app.run(
        host = "210.119.12.94",
        port = 8080,
        debug=True)