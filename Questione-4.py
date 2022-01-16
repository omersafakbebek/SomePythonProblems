l=[1,2,3,4,5,6,7,8,9,10]
for x in l:
    for y in l:
        print(x*y,end=" ")
        if y==10:
            print()