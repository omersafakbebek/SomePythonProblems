w1=input("w1=")
w2=input("w2=")
h1=input("h1=")
h2=input("h2=")
w1=int(w1)
w2=int(w2)
h1=int(h1)
h2=int(h2)
if h1>=h2 and w1>=w2:
    for i in range(int((h1-h2)/2)):
        print(w1*"*")
    for i in range(h2):
        print(int((w1-w2)/2)*"*"+w2*" "+int((w1-w2)/2)*"*")
    for i in range(int((h1 - h2) / 2)):
        print(w1 * "*")
if h1>=h2 and w1<w2:
    for i in range(int((h1 - h2) / 2)):
        print(int((w2-w1)/2)*" "+w1*"*"+int((w2-w1)/2)*" ")
    for i in range(h2):
        print(int((w2-w1)/2)*"*"+w1*" "+int((w2-w1)/2)*"*")
    for i in range(int((h1 - h2) / 2)):
        print(int((w2 - w1) / 2) * " " + w1 * "*" + int((w2 - w1) / 2) * " ")
if h1<h2 and w1>=w2:
    for i in range(int((h2 - h1) / 2)):
        print(int((w1 - w2) / 2) * " " + w2 * "*" + int((w1 - w2) / 2) * " ")
    for i in range(h2):
        print(int((w1 - w2) / 2) * "*" + w2 * " " + int((w1 - w2) / 2) * "*")
    for i in range(int((h2 - h1) / 2)):
        print(int((w1 - w2) / 2) * " " + w2 * "*" + int((w1 - w2) / 2) * " ")
if h1<h2 and w1<w2:
    for i in range(int((h2-h1)/2)):
        print(w2*"*")
    for i in range(h1):
        print(int((w2-w1)/2)*"*"+w1*" "+int((w2-w1)/2)*"*")
    for i in range(int((h2 - h1) / 2)):
        print(w2 * "*")



