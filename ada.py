count={}
def countstr(n):
    global count
    if len(n)==0:
        return mult(list(count.values()))
    count[n[-1]]=count.get(n[0],0)+1
    return countstr(n[:-1])
def mult(lst):
    if len(lst)==0:
        return 1
    return lst[-1]*mult(lst[:-1])
print(countstr("ali"))

