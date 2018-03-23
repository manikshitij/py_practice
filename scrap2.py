import urllib.request
from bs4 import *

url = input('Enter - ')
count=int(input('Enter Count:'))
pos=int(input('Enter Position:'))

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
print ("Retrieving: ",url)
c=0
s=[]
tags = soup('a')
for tag in tags:
    s.append(str(tag.get('href', None)))
for link in s:
	print ("Retrieving: ",s[pos-1])
	new = urllib.request.urlopen(s[pos-1]).read()
	soup = BeautifulSoup(new,"html.parser")
	tags = soup('a')
	s=[] 
	for tag in tags:
		s.append(str(tag.get('href', None)))
	print (s)
	c=c+1
	if c==count:
		break