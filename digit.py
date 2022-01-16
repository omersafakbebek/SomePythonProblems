a=0

def digit(x,y):
    global a
    x=str(x)
    y=str(y)
    if len(x)==0 or len(y)==0:
        return a
    if x[-1]==y[-1]:
        a+=1
    return digit(x[:-1],y[:-1])
print(digit(1234567, 67))