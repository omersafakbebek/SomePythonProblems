def inttobin(a):
    if a<2:
        return a
    else:
        return str(inttobin(a//2))+str(a%2)
print(inttobin(15))