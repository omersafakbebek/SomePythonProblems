l=[0,1,2,3,4,5,6,7,8,9]
for i in range(1,len(l)):
    for k in l:
        if k==i:
            continue
        for d in range(1,len(l)):
            if d==i or d==k:
                continue
            for o in l:
                if o==d or o ==k or o==i:
                    continue
                for r in l:
                    if r==o or r==d or r==k or r==i:
                        continue
                    for t in l:
                        if t==r or t==o or t==d or t==k or t==i:
                            continue
                        elif 202*i+20*k==1000*d+100*o+10*r+t:
                            print(101*i+10*k,1000*d+100*o+10*r+t)