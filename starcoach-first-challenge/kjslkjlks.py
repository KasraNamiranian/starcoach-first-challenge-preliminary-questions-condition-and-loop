n = int(input())

for i in range(n,0,-2):
    for j in range(i):
        print(chr(65+i),chr(65+n+i-1),chr(65+n+i))