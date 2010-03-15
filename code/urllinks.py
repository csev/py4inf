import urllib

url = raw_input('Enter - ')
fhand = urllib.urlopen(url)
for line in fhand:
   pos = line.find('href="')
   if pos < 1 : continue
   rest = line[pos+6:]
   end = rest.find('"')
   if end < 1 : continue
   link = rest[:end]
   print link
