import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'devmyself',
    charset = 'utf8'
)

curs = conn.cursor()

sql = 'CREATE TABLE IF NOT EXISTS user ( id INTEGER PRIMARY KEY AUTO_INCREMENT, user_id VARCHAR(20) NOT NULL UNIQUE, \
    user_password VARCHAR(64) NOT NULL, user_name VARCHAR(20) NOT NULL, user_email VARCHAR(20) NOT NULL, \
    user_phone VARCHAR(13) NOT NULL, user_birth VARCHAR(10) NOT NULL, enroll_date DATETIME DEFAULT CURRENT_TIMESTAMP)'


curs.execute(sql)
conn.commit()

sql = 'CREATE TABLE IF NOT EXISTS todo ( id INTEGER PRIMARY KEY AUTO_INCREMENT, user_id VARCHAR(20) NOT NULL, \
        priority INTEGER NOT NULL, task VARCHAR(20) NOT NULL, create_date DATETIME DEFAULT CURRENT_TIMESTAMP, \
        deadline DATETIME NOT NULL, is_deleted TINYINT DEFAULT 0)'
        
curs.execute(sql)
conn.commit()