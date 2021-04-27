import mysql.connector
import random
import time
import hashlib

from datetime import datetime, timedelta

conn = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'mir',
    password = 'wjdalfm1!',
    database = 'db_test',
    charset = 'utf8'
)


MAX_QUERY_LENGTH = 1000
idSet = [chr(i+97) for i in range(26)] + [str(i) for i in range(10)]
passwordSet = idSet + list('!@#$%^*&()-_=+')
nameSet = [chr(i+97) for i in range(26)]
emailSurfix = '@gmail.com'
userBirth = datetime(1990, 1, 1)
taskSet = ['토익 공부하기', '세계여행 가기', '다이어트하기', '공부하기', '애인 만들기',
           '취업하기', '돈 모으기', '책 읽기', '스키장 가기', '대회 나가기', '상타기'
           '물 많이 마시기', '제2 외국어 공부하기', '만점 받기', '집 사기', '자동차 사기'
           '효도 여행 보내드리기', '친구랑 화해하기', '일기 쓰기', '연예인 만나기',
           '산책하기', '자세 교정하기', '청소하기', '책상 정리하기', '영화 보기',
           '병원 가기', '건강 검진하기', '약 먹기', '비타민 챙겨 먹기', '강아지랑 놀아주기']

def insertUser():
    global userBirth,  conn
    with conn.cursor() as curs:
        user_id = "".join(sorted(random.sample(idSet, random.randint(6,10)), reverse=True))
        user_password = "".join(random.sample(passwordSet, random.randint(8, 15)))
        user_password = hashlib.sha256(user_password.encode()).hexdigest()
        user_name = "".join(random.sample(nameSet, random.randint(5, 10)))
        user_email = f'{"".join(user_id)}{emailSurfix}'
        user_phone = f'010-{random.randint(0, 9999):04d}-{random.randint(0, 9999):04d}'
        userBirth = userBirth + timedelta(random.randint(-10_000, 10_000))
        user_birth = f'{userBirth.year}-{userBirth.month}-{userBirth.day}'
        sql = f"insert into user(user_id, user_password, user_name, user_email, user_phone, user_birth) values('{user_id}', '{user_password}', '{user_name}', '{user_email}', '{user_phone}', '{user_birth}');"
        curs.execute(sql)
        print(f'{user_id} - {sql}')
        conn.commit()
        insertUserToDoList(user_id)

    
    
def insertUserToDoList(user_id):
    global userBirth, conn
    
    with conn.cursor() as curs:
        curs.execute(f"SELECT * FROM user where user_id = '{user_id}';")
        row = curs.fetchone()
        deadline = datetime.now() + timedelta(random.randint(4, 365))
        user_priority = user_task = ""
        for j in range(random.randint(1, 4)):
            user_priority = j + 1
            user_task = "".join(random.sample(taskSet, 1))
            is_done = random.randint(0,2);
            sql = f'insert into todo(user_id, priority, task, deadline, is_done) values("{row[0]}", "{user_priority}", "{user_task}", "{deadline}", "{is_done}")'
            print(f'\ttodo : {sql}')
            curs.execute(sql)
            conn.commit()
def main():
    startTime = time.time()
    
    for _ in range(MAX_QUERY_LENGTH):
        insertUser()
        
    print(f'Total Time : {time.time() - startTime}')

if __name__ == '__main__':
    main()