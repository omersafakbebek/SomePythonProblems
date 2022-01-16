n=int(input())
binary=0
for x in range(n):
    binary=binary+((n//2**x)%2)*10**x

print(binary)