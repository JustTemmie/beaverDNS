from os.path import dirname
import sqlite3
import time

while True:
    connection = sqlite3.connect(f'{dirname(__file__)}/website/database.db')

    posts = connection.execute('SELECT * FROM posts').fetchall()

    connection.close()

    with open(f'{dirname(__file__)}/ipAllowances.sh', 'w+') as gamesFile:
        gamesFile.flush()
        for thing in posts:
            gamesFile.write(f"iptables -A OUTPUT -d {thing[3]} -j ACCEPT\n")
        gamesFile.close()

    time.sleep(60)