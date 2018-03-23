a = int(input("enter a number"))
f=[]
pf=[]

for fact in range(1,a+1):
	if (a%fact==0):
		f.append(fact)
for fact in f:
	t=0
	for i in range(1,fact+1):
		if(fact%i==0):
			t=t+1
	if(t==2):
		pf.append(fact)
print(pf)