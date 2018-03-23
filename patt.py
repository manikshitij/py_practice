n=int(input("enter a number"))
s=" "*n
count=1
for i in range(1,n):
	for j in range(n,1,-1):
		print (s)
		for x in range(count):
			print ("*",end='')
	count=count+1