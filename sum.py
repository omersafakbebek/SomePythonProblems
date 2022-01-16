def sum(n):
    n=str(n)
    if len(n)==0:
        return 0
    return int(n[-1])+sum(n[:-1])
print(sum(247))