def Gaus(n):
    if n==1:
        return 1
    return n+Gaus(n-1)
print(Gaus(10))