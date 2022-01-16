def printsquares(n,lst,x=1):
    if x==int(n**(1/2))+1:
        new=0
        for i in range(len(lst)):
            new+=lst[i]**2
        if new==n:
            s=""
            for i in range(len(lst)):
                if i==len(lst)-1:
                    s+=str(lst[i])+"^2"
                    break
                s+=str(lst[i])+"^2 + "
            print(s)
        return
    lst.append(x)
    printsquares(n,lst,x+1)
    lst.pop()
    printsquares(n,lst,x+1)
printsquares(200,[])

