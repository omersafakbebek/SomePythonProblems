for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if 1000*a+100*b+10*c+d==a**5+b**5+c**5+d**5:
                    print(1000*a+100*b+10*c+d,end=" ")