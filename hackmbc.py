import math

ab=int(input())
bc=int(input())
tantheta=ab/bc

ansrad=math.atan(tantheta)
ans=math.degrees(ansrad)
a=round(ans)
print(str(a)+"\xb0")