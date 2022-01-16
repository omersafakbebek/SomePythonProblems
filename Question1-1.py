x=input("Please write some integers with come")
x=x.split(",")
n=0
for a in range(len(x)-1,-1,-1):
    n=n+int(x[a])*10**(len(x)-a-1)
print(n)
