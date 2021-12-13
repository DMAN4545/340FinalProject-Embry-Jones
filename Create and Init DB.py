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
    (1, "Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402021/aj.jpg", "Angelina Jolie is a professional actor and film producer with decades of experience. A recipient of many accolades and awards, Angelina Jolie is one of Hollywood's leading actresses."),
    (2, "Brad", "Pitt", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402021/bp.jpg", "Brad Pitt is a professional actor and filmmaker with decades of acting experience. A father of six children, he spends his days writing, filmmaking, and parenting."),
    (3, "Snow", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402021/sw.jpg", "Snow White is a fictional character apart of the Disney Princess Universe and the main character of the film, Snow White and the Seven Dwarfs. She is often described as the fairest one of all."),
    (4, "Darth", "Vader", 29, "dv@darkside.me", "https://s3.amazonaws.com/isat3402021/dv.jpg", "Darth Vader is a fictional character apart of the Disney + Lucasfilm Star Wars Universe and a main character and protagonist throughout the story. Described as one of the most powerful Sith Lords ever, you do not want to find yourself on Vader's bad side."),
    (5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402021/ts.jpg", "Taylor Swift is a professional singer, songwriter, producer, and entrepreneur with many number one chart-toppers. A consistent major player in the music industry, Taylor is one of the biggest pop superstars ever."),
    (6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402021/bk.jpg", "Beyonce Knowles is a professional singer, songwriter, producer, entrepreneur, and political activist. Beyonce is known for her many achievements in the music industry, including being the first female artist to debut at No. 1 on the Billboard 200 with her first five studio albums."),
    (7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402021/sg.jpg", "Selena Gomez is a professional actor, singer, and songwriter. Selena Gomez is best known for her work at Disney for the show Wizards of Waverly Place, starring as the main character, Alex Russo."),
    (8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402021/sc.jpg", "Stephen Curry is a professional basketball player and entrepreneur. Stephen Curry is a 3-time NBA Champion, 2-time FIBA World Cup Champion, and has played for the Golden State Warriors since 2009. ")
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
