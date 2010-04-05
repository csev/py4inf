import sqlite3

conn = sqlite3.connect('twspider.db')
cur = conn.cursor()

cur.execute('SELECT * FROM twitter')
for row in cur :
   print row

cur.close()
