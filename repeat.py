def repeat(s,x):
    if x==0:
        return ""
    return s+repeat(s,x-1)
print(repeat("hi ho! ",0))