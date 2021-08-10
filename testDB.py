import pymssql
import time

# DB 서버 주소
server = 'PC01'
# 데이터 베이스 이름
database = 'DogWorker'
# 접속 유저명
username = 'sa'
# 접속 유저 패스워드
password = 'mssql_p@ssw0rd!'
# MSSQL 접속
cnxn =  pymssql.connect(server , username, password, database)
cursor = cnxn.cursor()

# SQL문 실행
while True:

    cursor.execute('SELECT Lat,Lon FROM GPSTBL;')
# 데이타를 하나씩 Fetch하여 출력
    row = cursor.fetchone()

    while row:
        coordinate=[(row[0],row[1])]
        print(coordinate[0])
        row = cursor.fetchone()
    time.sleep(3)
# 연결 끊기
cnxn.close()