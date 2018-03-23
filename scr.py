import requests
from bs4 import *
import re

url = 'https://www.google.com/search?q=abcd'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,'html.parser')

reg=re.compile(".*&sa=")

links = []
#Parsing web urls
for item in soup.find_all('h3', attrs={'class' : 'r'}):
    line = (reg.match(item.a['href'][7:]).group())
    links.append(line[:-4])

for i in links:
	print(i)

x=str(soup)
a=x.split(">")
b=[]
for terms in a:
	if terms == re.findall("^About?://",x):
		b.append(a.index(terms))
print(b)
