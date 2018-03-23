l=[]
p=[]

a=int(input("enter a number")

for i in range(a):
	if(a%i==0):
		l.append(i)
for f in l:
	t=0
	for i in range(f):
		if(f%i==0):
			t=t+1
	if(t==2):
		p.append(f)
print(p)