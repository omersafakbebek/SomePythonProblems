def mul(a,b):
    if a==1:
        return b
    return b+mul(a-1,b)
print(mul(6,5))