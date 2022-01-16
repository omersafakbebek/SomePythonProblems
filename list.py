def lsts(n,lst):
    if n==0:
        return
    print(lst[n-1],end=" ")
    return lsts(n-1,lst[:n-1])
lsts(3,[1,2,3])
