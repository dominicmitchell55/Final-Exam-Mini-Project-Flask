#import sqlite3
import sqlite3
#create or connect to an existing db
conn = sqlite3.connect('celebrities.db')
#get a cursor to work with database. database cursor is an object used to pinpoint records in db
cursor = conn.cursor()

#create a table
sql = "create table celebs(celebID int PRIMARY KEY, firstname text, lastname text, age int, email text, photo text, bio text)"
cursor.execute(sql)
#commit the changes to the db
conn.commit()

sql = "create table members(memberID int PRIMARY KEY, firstname text, lastname text, age int, email text, bio text)"
cursor.execute(sql)
#commit the changes to the db
conn.commit()

#close the connection to db
conn.close()