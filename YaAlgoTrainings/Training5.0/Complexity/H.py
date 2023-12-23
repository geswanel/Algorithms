"""
Circle L meters
2 participants: x1, x2 coordinates
clock wise
v1 v2

When participants at the same distance from the start

INPUT:
L, x1, x2, v1, v2

x1 = x10 + v1t
x2 = x20 + v2t

x10 + v1t = x20 + v2t + kL
t = (x20 - x10 + kL) / (v1 - v2)

x10 + v1t = -x20 - v2t + kL
t = (kL - x10 - x20) / (v1 + v2)

"""

def getTime(L, xpar, vpar):
    if vpar > 0 and xpar >= 0 or vpar < 0 and xpar <= 0:
        k = abs(xpar) // L
        xpar = xpar + k * L if xpar < 0 else xpar - k * L
        return xpar / vpar
    else:
        k = abs(xpar) // L + 1
        if vpar > 0:
            return (k * L + xpar) / vpar
        elif vpar < 0:
            return (xpar - k * L) / vpar

def distTime(L, x1, x2, v1, v2):
    if x1 % L == x2 % L or x1 % L == (L - x2) % L:
        return 0

    t1 = getTime(L, x2 - x1, v1 - v2)
    t2 = getTime(L, - x1 - x2, v1 + v2)
    if t1 is not None and t2 is not None:
        return round(min(t1, t2), 10)
    else:
        return t1 or t2

def main():
    L, x1, v1, x2, v2 = [int(x) for x in input().split()[:5]]
    t = distTime(L, x1, x2, v1, v2)

    if t is None:
        print("NO")
    else:
        print("YES")
        print(round(t, 10))

if __name__ == "__main__":
    main()