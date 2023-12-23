"""
n lines
i line => ai spaces needed
Keys:
    space + 1 space
    tab + 4 spaces
    backspace - 1 space
Min number of pressing keys
ai % 4 == 0 => tabs => a // 4
ai % 4 == 1 or 2 => tabs till (ai - 1) + 1 space or 2 spaces = ai // 4 + ai % 4
ai % 4 == 3 => tabs till (ai + 1) + 1 backspace = ai // 4 + 1 + 1
"""
def minKeyPress(a):
    keyPressCnt = 0
    for ai in a:
        keyPressCnt += ai // 4 + (ai % 4 == 1) + 2 * (ai % 4 == 2 or ai % 4 == 3)
    
    return keyPressCnt

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    print(minKeyPress(a))


if __name__ == "__main__":
    main()