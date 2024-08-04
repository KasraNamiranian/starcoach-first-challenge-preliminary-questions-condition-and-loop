a = int(input())
b = int(input())
l=[]
t=0

for i in range(a+1 , b):
    t=0
    for k in range(2,(i//2)+1):
        if i % k == 0:
            t=t+1
            break
    if(t == 0):
        l.append(i)
p=len(l)
for d in range(p):
    print(l[d],end="")
    if(d!=p-1):
        print(",",end="")
