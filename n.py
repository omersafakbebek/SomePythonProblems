x=1
def m(n,x=1):
    if x==n:
        return n+1/(n+1)
    return x+1/m(n,x+2)
print(m(101))

