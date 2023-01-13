import sqlite3

connection = sqlite3.connect('website/database.db')


with open('website/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'URL')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'URL')
            )

cur.execute("INSERT INTO incoming (ip, requested, url) VALUES (?, ?, ?)",
            ('127.0.0.1', '1', 'yourself')
            )

connection.commit()
connection.close()