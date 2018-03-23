import re
handle = open("file.txt")
y=[]
z=[]
for line in handle:
	if re.search('[0-9]+',line):
		y.append(re.findall('[0-9]+',line))
for element in y:
	for i in element:
		z.append(int(i))
print (sum(z))	