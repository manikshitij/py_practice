import urllib.request
from bs4 import *

st = input('Enter exact search term - ')
url = "http://www.bing.com/search?q="+st+"&go=Submit&qs=bs&form=QBLH"
print(url)
html = urllib.request.urlopen(url).read()

print(html)

soup = BeautifulSoup(html,'html.parser')

