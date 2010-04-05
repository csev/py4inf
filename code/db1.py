import sqlite3

conn = sqlite3.connect('music.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS tracks ')
cur.execute('CREATE TABLE tracks (title TEXT, plays INTEGER)')

conn.close()

