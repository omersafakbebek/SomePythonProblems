l=input("")
l.lower()
l=list(l)
k=True
v=["a","e","i","o","u"]
for j in l:
    if j in v:
         k=True
    else:
         k=False
         break
print(k)



