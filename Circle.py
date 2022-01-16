def circle(r,n=0.0,x=0.1):
    if n>=2*r:
        return 0
    return (r*(x-n)/2)+ circle(r,n+0.1,x+0.1)
print(3*circle(25))