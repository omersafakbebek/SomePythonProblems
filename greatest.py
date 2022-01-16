d=2
def gre(a,b):
    global d
    if a==1 or b==1:
        return 1
    if a%d==0 and b%d==0:
        return (d)*gre(a/d,b/d)
    if a%d==0 and b%d!=0:
        return gre(a/d,b)
    if a%d!=0 and b%d==0:
        return gre(a,b/d)
    if a%d!=0 and b%d!=0:
        d=d+1
        return gre(a,b)
print(gre(48,36))
