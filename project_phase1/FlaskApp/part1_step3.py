import sqlite3
conn = sqlite3.connect('celebrities.db')
cursor = conn.cursor()

sql = 'insert into members values (?, ?, ?, ?, ?, ?)'
data = ((1, "Ethan", "Johnson", 21, "johns4eh@dukes.jmu.edu", "making money$"))

cursor.execute(sql, data)

#commit the changes to the db
conn.commit()
conn.close()