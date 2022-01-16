n=int(input())
i=0
x=n
while(True):
    if x==0:
        break
    x=x//10
    i+=1
new=0
for m in range(i):
    if i%2==1:
        if m==i-1:
            new+=(n%10)*10**m
            break
    if m%2==0:
        new+=(n%10)*10**(m+1)
    else:
        new+=(n%10)*10**(m-1)
    n=n//10
print(new)




