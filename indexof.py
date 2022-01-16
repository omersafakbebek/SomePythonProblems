x=0
def indexOf(a,b):
    global x
    if len(a)==0:
        return -1
    if a[:len(b)]==b:
        return x
    x+=1
    return indexOf(a[1:],b)
print(indexOf("Barack Obama", "BAR"))
