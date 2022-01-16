def isReverse(s,r):
    if len(s)==0 and len(r)==0:
        return True
    s=s.lower()
    r=r.lower()
    if s[0]!=r[-1]:
        return False
    return isReverse(s[1:],r[:-1])
print(isReverse("Obama", "McCain"))
