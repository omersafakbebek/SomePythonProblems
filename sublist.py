def sub(lst,x,subl):
    if x==0:
        print(subl)
        return
    subl.append(lst[0])
    sub(lst[1:],x-1,subl)
    subl.pop()
    sub(lst[1:],x-1,subl)
sub(["Janet", "Robert", "Morgan", "Char"],4,[])