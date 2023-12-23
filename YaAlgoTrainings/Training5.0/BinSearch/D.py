"""
Description:
report = 2 parts
first part
    n words
    ai characters for i word
second part
    m words
    bj characters for j word
Report should be written on checkered paper roll with the width w
2 parts will be divided by vertical line on the roll

characters takes 1 check
spaces should be placed between words and they take 1 check
if a word cannot be placed in line => placed in next line

max word length <= w

Figure out min length of roll

INPUT:
w n m - w ~ 1e9, n, m ~1e5
ai - first part length of words
bj - second part length of words
OUTPUT
min length of roll
Solution:
Length of roll maxed on the edge cases and min somewhere in between.
=> bin derivative search to find the minumum point.
Min roll length mean that length on the left and right part are the same. so we can divide by 2
using this fact
1. bin search over vertical line position O(logw)
    2. count left and right sizes O(n + m)
        if left size < right size
            move left
        else:
            move right
"""
import unittest

def placeWords(width, wordSizes):
    ans = 1
    remainedLine = width
    for size in wordSizes:
        if remainedLine == width:
            remainedLine -= size
        elif remainedLine >= size + 1:
            remainedLine -= size + 1
        else:
            ans += 1
            remainedLine = width - size
    
    return ans

def minRollLen(w, a, b):
    l = max(a)
    r = w - max(b)
    #print(l, r)
    minRoll = max(len(a), len(b))
    while l < r:
        mid = (l + r) // 2
        leftLen = placeWords(mid, a)
        rightLen = placeWords(w - mid, b)
        if max(leftLen, rightLen) < minRoll:
            minRoll = max(leftLen, rightLen)
        if leftLen > rightLen:
            l = mid + 1
        elif leftLen < rightLen:
            r = mid
        else:
            return leftLen
    
    return min(max(placeWords(l, a), placeWords(w - l, b)), minRoll)

def main():
    w, n, m = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(minRollLen(w, a, b))



if __name__ == "__main__":
    main()