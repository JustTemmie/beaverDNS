import time  
import sqlite3
import socket
import random

def follow(thefile):
    thefile.seek(0,2) # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        yield line

logfile = open("/var/log/kern.log")
loglines = follow(logfile)
for line in loglines:
    IP = line.split("DST=")[1].split(" LEN")[0]
    print(IP)

    connection = sqlite3.connect('./website/database.db')

    cur = connection.cursor()
    
    foundIt = False
    counter = 1
    rowID = 0
    

    hostName = "?"
    try:
        host = socket.gethostbyaddr(IP)
        hostName = host[0]
    except:
        pass
    
    for row in cur.execute('SELECT * FROM incoming;'):
        if row[2] == IP:
            counter = int(row[3]) + 1
            foundIt = True
            break

    if not foundIt:
        cur.execute("INSERT INTO incoming (ip, requested, url) VALUES (?, ?, ?)",
                    (IP, counter, hostName)
                    )

    else:
        sql =   ''' UPDATE incoming
                    SET requested = ?,
                        url = ?
                    WHERE ip = ?'''
        task = [counter, hostName, IP]
        cur.execute(sql, task)
        
    connection.commit()
    connection.close()
    
    connection = sqlite3.connect('./website/database.db')
    
    
    cur = connection.cursor()
    
    cur.execute("SELECT * FROM incoming ORDER BY requested")
    
    connection.commit()
    connection.close()    