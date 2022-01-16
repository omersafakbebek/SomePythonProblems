def st(a,b):
    m=len(a)
    n=len(b)
    if m==0:
        return True
    if n==0:
        return False
    if a[m-1]==b[n-1]:
        return st(a[:m-1],b[:n-1])
    else:
        return st(a,b[:n-1])
print(st("bat","table"))