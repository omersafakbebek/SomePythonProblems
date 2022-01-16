x=input()
x=int(x)
l=[0,1]
for a in range(1,x+1):
    f=l[a]+l[a-1]
    l.append(f)
    if a==x-1:
        break
print(f)