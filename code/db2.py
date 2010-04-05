import sqlite3

conn = sqlite3.connect('music.db')
cur = conn.cursor()

cur.execute('INSERT INTO tracks (title, plays) VALUES ( ?, ? )', 
    ( 'Thunderstruck', 20 ) )
cur.execute('INSERT INTO tracks (title, plays) VALUES ( ?, ? )', 
    ( 'My Way', 15 ) )

print "Tracks:"
cur.execute('SELECT title, plays FROM tracks')
for row in cur :
   print row

cur.execute("DELETE FROM tracks WHERE plays < 100")

conn.close()

