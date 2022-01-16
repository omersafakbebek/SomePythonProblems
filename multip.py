def multi(m,n):
    if n==0:
        return 0
    return m+multi(m,n-1)
print(multi(7,4))