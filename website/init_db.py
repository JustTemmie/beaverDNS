import sqlite3

connection = sqlite3.connect('website/database.db')


with open('website/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Titles', 'discord.com')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('I\'m so original', 'bjerkaker.tromsoskolen.no')
            )

cur.execute("INSERT INTO incoming (ip, requested, url) VALUES (?, ?, ?)",
            ('127.0.0.1', '1', 'loop back')
            )

connection.commit()
connection.close()