x=input()
m=""
for i in range(int(x)):
    if 2 ** i > int(x):
        break
    m=str((int(x)//2**i)%2)+m


print(m)