l=input()
l=l.split()
bin_list=[]
for i in range(2**len(l)):
    bin = []
    for m in range(len(l)):
        bin.insert(0,i%2)
        i=i//2
    bin_list.append(bin)
print(bin_list)
for x in bin_list:
    subset=[]
    for y in range(len(x)):
        if x[y]==1:
            subset.append(l[y])
    k=0
    for e in range(len(subset)):
        k=k+(int(subset[len(subset)-e-1])*10**e)
    print(k)









