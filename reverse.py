def rev(s):
    l=s.split()
    if len(l)==1:
        return s

    return l[-1]+" "+rev(" ".join(l[0:-1]))
print(rev("one or two or three more cat are running"))

