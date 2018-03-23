import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter location:")
print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print ('Retrieved',len(data),'characters')
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print ("count:",len(lst))
sum = 0
for item in lst:
    sum=sum+int(item.find("count").text)
print ("Sum:",sum)