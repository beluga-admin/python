# Section12-1
# python database SQLite
# Table creation and data insertion

import sqlite3
import datetime

# insert date
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")
print('nowDatetime : ' , nowDatetime)

# sqlite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version : ', sqlite3.sqlite_version)

# DB creation & Auto commit
conn = sqlite3.connect('D:/dev/python/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type: ', type(c))

# Table creation(Data Type: TEXT, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# Data insertion
c.execute("INSERT INTO users VALUES(1, 'Kim', 'Kim@naver.com', '010-1234-5678', 'Kim.com', ?)", (nowDatetime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2, 'Park', 'Park@naver.com', '010-1234-5678', 'Park.com', nowDatetime))

# Many data insertion(Tuples, Lists)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-1234-5678', 'Lee.com', nowDatetime),
    (4, 'Choi', 'Cho@naver.com', '010-1234-5678', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-1234-5678', 'Yoo.com', nowDatetime),
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

# Table data select
# c.execute("SELECT * FROM users")
# print("users db delted : ", conn.execute("DELETE FROM users").rowcount)
