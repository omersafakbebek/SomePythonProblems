lst=[]
def stairs(n):
    if n<=0:
        if n==0:
            if len(lst)!=0:
                print(lst)
        return
    lst.append(1)
    stairs(n-1)
    lst.pop()
    lst.append(2)
    stairs(n-2)
    lst.pop()

stairs(3)