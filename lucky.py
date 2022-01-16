n=1
def summ(x):
    global n
    if n==x:
        return n
    if x%n==0:
        a=n
        n=n+1
        return a+summ(x)
    n=n+1
    return summ(x)
depth=0
def lucky(x):
    global depth
    if depth==0:
        depth+=1
        return lucky(summ(x))
    k=str(x)
    if len(k)==1:
        if k[-1]!="4" and k[-1]!="7":
            return 0
        else:
            return 1
    else:
        if k[-1]!="4" and k[-1]!="7":
            return 0
        return lucky(int(k[:-1]))
print(lucky(7))
