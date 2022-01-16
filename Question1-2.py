x=input("Please write some integers with comma")
x=x.split(",")
t=0
for a in range(len(x)-1,-1,-1):
    m=1
    for n in range(len(x)-2-a,-1,-1):
        m=m*10
    t=t+int(x[a])*m
print(t)