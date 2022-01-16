def rever(n):
    if n==1:
        print(n,end="")
        return
    print(n,end=" ")
    return rever(n-1)
rever(5)