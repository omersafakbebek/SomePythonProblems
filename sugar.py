n=int(input())
def ways(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n==3:
        return 2
    return ways(n-1)+ways(n-3)
print(ways(n))