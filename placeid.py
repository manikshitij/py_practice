# this cod is for python 3
import urllib.request
import urllib.parse
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"
address = input("Enter Location:")
url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print ('Retrieved',len(data),'characters')

js=json.loads(data)
print("Place id:",js["results"][0]["place_id"])