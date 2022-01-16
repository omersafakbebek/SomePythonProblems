def x_ish(a,b):
    if len(a)==0:
        return True
    if a[0] in b:
        return x_ish(a[1:],b)
    if a[0] not in b:
        return False
print(x_ish("ali","kabali"))