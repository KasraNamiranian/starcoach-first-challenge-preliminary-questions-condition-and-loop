n = int(input())

a=n

c=0

t=3

d = (n//2) + 1
for i in range(1,d+1):
        amount=i-1
        s=n-1
        p=s
        print(chr(65+i-1),end=" ")
        while(amount>0):
              print(chr(65+i-1+p),end=" ")
              s-=2
              p=p+s
              amount-=1
        print("")

for i in range((d+1),n+1):
    amount=i-t
    t+=2
    s=n-1
    p=s
    print(chr(65+i-1),end=" ")
    while(amount>0):
          print(chr(65+i-1+p),end=" ")
          s-=2
          p=p+s
          amount-=1
    print("")