def par(n,comb):
    if n==len(comb)/2:
        kont=comb.copy()
        for a in range(n):
            if "(" in kont and ")" in kont:
                if kont.index("(")<kont.index(")"):
                    kont.remove("(")
                    kont.remove(")")
        if kont==[]:
            print("".join(comb),end=" ")
        return
    for i in ["(",")"]:
        comb.append(i)
        par(n,comb)
        comb.pop()
par(3,[])




