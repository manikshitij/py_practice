n=input()
a=n
p=[]
sum=0
while (len(p)!=1):
	p=[]
	sum=0
	for i in range(len(a)):
		p.append(a[i])
	if len(p)==1:
		break
	for i in p:
		sum=sum+int(i)
	a=str(sum)
print(a)