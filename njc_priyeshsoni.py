import sqlite3
connection=sqlite3.connect('Movies.db')
cursor=connection.cursor()


query_command=""" CREATE TABLE IF NOT EXISTS Movies(name TEXT PRIMARY KEY,actor TEXT,actress TEXT, director TEXT,year INTEGER) """

cursor.execute(query_command)


cursor.execute(" INSERT INTO Movies VALUES ('Angrezi Medium','Irrfan Khan','Radhika Madan','Homi Adajania',2020)")
cursor.execute(" INSERT INTO Movies VALUES ('Love aaj kal','Saif Ali Khan','Deepika Padukone','Imtiaz Ali',2009)")
cursor.execute(" INSERT INTO Movies VALUES ('Race','Saif Ali Khan','Katrina Kaif','Abbas & Mastan',2008)")
cursor.execute(" INSERT INTO Movies VALUES ('PK','Aamir khan','Anushka Sharma','Rajkumar Hirani',2014)")



cursor.execute("SELECT * FROM Movies")
answer=cursor.fetchall()


cursor.execute("SELECT * FROM Movies WHERE actor='Aamir Khan' ")
answer1=cursor.fetchall()

#print the answer
print(answer)

print(answer1)