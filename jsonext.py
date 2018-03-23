# this code is for python3
import urllib.request
import json

sum = 0
url = input("Enter location:")
print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()

print ('Retrieved',len(data),'characters')

dat = json.loads(data)
ndat = dat["comments"]
print ('Count:', len(ndat))

for item in ndat:
	sum = sum + item["count"]
print("Sum:",sum)