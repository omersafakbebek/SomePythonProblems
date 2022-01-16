e = False
l = False
f = False


def elfish(s):
    global e
    global l
    global f
    if len(s) == 0:
        return False

    if s[0] == "e":
        e = True
    elif s[0] == "l":
        l = True
    elif s[0] == "f":
        f = True
    if e and l and f:
        return True
    return elfish(s[1:])
print(elfish("elakinf"))
