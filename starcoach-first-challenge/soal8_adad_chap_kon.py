a = input()
c = int (a)
d = int(len(a))
d = d-1

for i in range(len(a)):
    b = c // 10**d
    c = c - (b * 10**d)
    d = d - 1
    print(f"{b}:", end=" ")
    for k in range(b):
        print(b , end="")
    print("\n")
    
