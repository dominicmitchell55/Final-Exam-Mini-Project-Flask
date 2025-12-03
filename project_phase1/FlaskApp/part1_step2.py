import sqlite3
conn = sqlite3.connect('celebrities.db')
cursor = conn.cursor()

sql = 'insert into celebs values (?, ?, ?, ?, ?, ?, ?)'
data = (
    (1, "Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402021/aj.jpg",
     "American actress, filmmaker, and humanitarian"),
    (2, "Brad", "Pitt", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402021/bp.jpg",
     "American actor and producer known for his portrayal of unconventional characters"),
    (3, "Snow", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402021/sw.jpg",
     "Fictional Disney character known for her kindness and connection with the Seven Dwarfs"),
    (4, "Darth", "Vader", 29, "dv@darkside.me", "https://s3.amazonaws.com/isat3402021/dv.jpg",
     "Iconic Star Wars villain and Sith Lord, formerly Anakin Skywalker"),
    (5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402021/ts.jpg",
     "American singer-songwriter known for narrative songwriting across multiple genres"),
    (6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402021/bk.jpg",
     "American singer, songwriter, and performer, widely regarded as a cultural icon"),
    (7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402021/sg.jpg",
     "American singer, actress, and producer, known for her work in music and television"),
    (8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402021/sc.jpg",
     "Professional basketball player for the Golden State Warriors, known for revolutionizing the game with his shooting"),
)

cursor.executemany(sql, data)

#commit the changes to the db
conn.commit()
conn.close()