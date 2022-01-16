n=input()
n=int(n)
for i in range(1,n+1):
    print(int((2*n-2*(i))/2)*" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print(int((2 * n - 2 * (n - i)) / 2) * " ", end="")
    if i==7:
        break
    print()