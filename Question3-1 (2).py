n=input()
n=int(n)
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=(""))
    if i==n:
        break
    print()