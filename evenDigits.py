def evendig(n,x):
    if x==0:
        if len(n)==0:
            return "0"
        return n
    n=str(n)
    if n[0]=="-":
        return int("-"+evendig(n[1:],x-1))
    if int(n[x-1])%2==0:
        return evendig(n,x-1)
    return evendig(n[:x-1]+n[x:],x-1)
print(evendig(353,3))

