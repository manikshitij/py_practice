import cmath

x=input()

l=[]
for n in range(len(x)):
	if(x[n]=="+" or x[n]=="-"):
		l.append(n)

if x.startswith("-"):
	num1=x[0:l[1]]
else:
	num1=x[0:(l[0])]
if x.startswith("-"):
	num2=x[l[1]:len(x)-1]
else:
	num2=x[(l[0]):(len(x)-1)]

a=float(num1)
b=float(num2)

p1=abs(complex(a,b))
p2=cmath.phase(complex(a,b))
print(p1)
print(p2)