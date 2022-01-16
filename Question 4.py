l=input()
a=list(l)
y=0
for x in range(len(l)-1,-1,-1):
    if int(l[x])==1 :
        y=y+2**(len(l)-x-1)
    else:
        y=y+0

print(y)

