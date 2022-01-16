def g(n):
    if n<=1:
        return 0
    if n%2==0:
        return int(g(n/2)+n/2)
    else:
        return int(g((n-1)/2)+(n-1)/2)
print(g(5))