from flask import Flask, render_template

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 최초 url
def index():
    #백엔드에서 데이터를 프론트엔드로 전달
    return render_template('index01.html',user='박규민',data={'userid':'guemin96','gender':'male','age':26})

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)