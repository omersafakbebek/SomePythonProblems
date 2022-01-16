n=int(input())
x=False
for i in range(1,n):
    for j in range(1,n):
        if i**2+j**2==n:
            x=True
            print(i,j)
if x==False:
    print(0)

