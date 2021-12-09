#Created by Devon Embry and Blake Jones

import sqlite3

con = sqlite3.connect("celebrities.db")
cursor = con.cursor()

CelebsTables = "CREATE TABLE celebs(celebID INTEGER NOT NULL PRIMARY KEY,firstname TEXT,lastname	TEXT,age INTEGER,email TEXT,photo TEXT,bio	TEXT)"
MembersTables = "CREATE TABLE members(memberID INTEGER NOT NULL PRIMARY KEY,firstname TEXT,lastname TEXT,age INTEGER,email TEXT,bio TEXT)"
LoginTables = "CREATE TABLE member_login (memberID INTEGER NOT NULL PRIMARY KEY, username TEXT, password TEXT)"

CreateTables = {CelebsTables, MembersTables, LoginTables}

for i in CreateTables:
    cursor.execute(i)
    con.commit()

CelebsInsert = "INSERT INTO celebs values(?,?,?,?,?,?,?)"
CelebsData = (
    (1, "Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402021/aj.jpg", "stuff"),
    (2, "Brad", "Pitt", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402021/bp.jpg", "stuff"),
    (3, "Snow", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402021/sw.jpg", "stuff"),
    (4, "Darth", "Vader", 29, "dv@darkside.me", "https://s3.amazonaws.com/isat3402021/dv.jpg", "stuff"),
    (5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402021/ts.jpg", "stuff"),
    (6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402021/bk.jpg", "stuff"),
    (7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402021/sg.jpg", "stuff"),
    (8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402021/sc.jpg", "stuff")
)

cursor.executemany(CelebsInsert, CelebsData)
con.commit()

MembersInsert = "INSERT INTO members values(?,?,?,?,?,?)"
MembersData = {
    (1, "Devon", "Embry", 19, "embryda@dukes.jmu.edu", "I currently attend JMU working towards a degree in ISAT."),
    (2, "Blake", "Jones", 21, "jones2bg@dukes.jmu.edu", "I am currently pursuing a computer science degree at JMU.")}

cursor.executemany(MembersInsert, MembersData)
con.commit()

LoginInsert = "INSERT INTO member_login values(?,?,?)"
LoginData = {(1, "devon", "devon"),(2, "blake", "blake")}

cursor.executemany(LoginInsert, LoginData)
con.commit()

con.close()
