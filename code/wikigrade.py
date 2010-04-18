import sqlite3
import datetime
import urllib
from BeautifulSoup import *

conn = sqlite3.connect('wikidata.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS TinyTable (id INTEGER PRIMARY KEY, 
                   url TEXT, page BLOB, retrieved_at timestamp)''')

def tinyTable(url):
    global cur,conn
    cur.execute('SELECT id,page,retrieved_at FROM TinyTable WHERE URL = ?', (url, ))
    try:
        row = cur.fetchone()
        print 'DATE',row[2]
        return row[1]
    except:
        row = None
    print 'Retrieving', url

    data = urllib.urlopen (url).read()
    if row != None:
        cur.execute("UPDATE TinyTable SET page=?,retrieved_at=datetime('now') WHERE id=?", (unicode(data, 'utf-8'), row[0]))
    else:
        cur.execute("INSERT INTO TinyTable (url, page, retrieved_at) VALUES (?, ?, datetime('now'))",(url, unicode(data, 'utf-8')))
    conn.commit()
    return data

cururl = 'https://ctools.umich.edu/access/wiki/site/f57681b8-6db9-46cf-aad1-3a0bdd621138/home.html'
urls = list()
urls.append(cururl)
visited = list()

while len(urls) > 0 : 
    print '========= ',len(urls),' =========='
    cururl = urls.pop()
    print 'RETRIEVING',cururl
    d1 = tinyTable(cururl)
    if cururl in visited : visited.append(cururl)
    soup = BeautifulSoup(d1)

    tags = soup('a')
    print 'Tags'
    for tag in tags:
        print tag
        url = tag.get('href',None)
        if url == None : continue
        if url.startswith('http') : continue
        newurl = urllib.basejoin(cururl,url)
        if newurl in visited : continue
        print 'APPENDING',newurl
        urls.append(newurl)

    tags = soup('link')
    print 'RSS:'
    for tag in tags:
        if tag['type'] != 'application/rss+xml' : continue
        url = tag['href']
        newurl = urllib.basejoin(cururl,url)
        # Ask for RSS 2.0
        newurl = newurl.replace('.10.rss', '.20.rss')
        print newurl
        data = tinyTable(newurl)

conn.close()
