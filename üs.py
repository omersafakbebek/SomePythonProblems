def exp(m,n):
    if n==0:
        return 1
    return m*exp(m,n-1)
print(exp(-3,5))