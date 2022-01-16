def ways(n,lst):
    if n<=0:
        if n==0:
            print(lst)
        return
    lst.append(1)
    ways(n-1,lst)
    lst.pop()
    lst.append(2)
    ways(n-2,lst)
    lst.pop()
ways(4,[])
