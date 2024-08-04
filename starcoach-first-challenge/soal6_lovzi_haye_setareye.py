n = int(input())
w = n//2
t = 1
e = 2
for i in range(0,n):
    if (i > w):
        print(t*" " + (n-(2*t))*"*" + e*" " + (n-(2*t))*"*")
        t = t + 1
        e = e + 2
    else:
        print(((n//2)-i)*" " + (2*i+1)*"*" + (n-(2*i+1))*" " + (2*i+1)*"*")
