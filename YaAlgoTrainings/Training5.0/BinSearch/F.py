"""
Description:
main square => wxh rectangle filled with tiles 1x1
Build 2 bike paths with the same width. Vertical and horizontal
Some tiles are broken

Find min width of paths so that all tiles are intact
INPUT:
w h n   - w, h ~ 1e9. n ~ 3*1e5 - number of broken tiles
xi yi - position of broken tiles
OUTPUT
min width of paths
Solution: O(n logn log(max(w,h))
0. Create sorted array of points (x, y) O(n log n)
        Create array of prefix and suffixes max and min y for lines
1. Bin search over width of O(log max(w,h))
2. for pathW check if all broken tiles covered:
3. Check function
    iterate over vertical path positions sticked to some lines with points O(n)
        identify what lines banned O(log n)
        identify difference O(1)
        
"""
import unittest


def createPrefix(h, lines, vertLines):
    prefix = []
    for line in lines:
        miny = h + 1; maxy = 0
        for linePoint in vertLines[line]:
            if linePoint[1] < miny:
                miny = linePoint[1]
            if linePoint[1] > maxy:
                maxy = linePoint[1]
        
        if prefix:
            pMiny, pMaxy = prefix[-1]
            prefix.append((min(pMiny, miny), max(pMaxy, maxy)))
        else:
            prefix.append((miny, maxy))
    
    return prefix

def createSuffix(h, lines, vertLines):
    suffix = []
    for line in lines[::-1]:
        miny = h + 1; maxy = 0
        for linePoint in vertLines[line]:
            if linePoint[1] < miny:
                miny = linePoint[1]
            if linePoint[1] > maxy:
                maxy = linePoint[1]
        
        if suffix:
            pMiny, pMaxy = suffix[-1]
            suffix.append((min(pMiny, miny), max(pMaxy, maxy)))
        else:
            suffix.append((miny, maxy))
    
    return suffix[::-1]

def lowerBound(arr, val):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < val:
            l = mid + 1
        else:
            r = mid
    
    return l

def horPath(prefix, suffix, leftEdge, rightEdge):
    minyl, maxyl = (1e9 + 1, 0) if leftEdge < 0 else prefix[leftEdge]
    minyr, maxyr = (1e9 + 1, 0) if rightEdge >= len(suffix) else suffix[rightEdge]
    return max(maxyl, maxyr) - min(minyl, minyr) + 1

def minPathWidth(w, h, n, vertLines):
    lines = sorted(vertLines)
    prefix = createPrefix(h, lines, vertLines) # for i line => miny, maxy in lines [:i]
    suffix = createSuffix(h, lines, vertLines) # for i line => miny, maxy in lines [i:]
    #print(prefix, suffix)

    # bin search for path width O(logw)
    l = 1
    r = w
    while l < r:
        mid = (l + r) // 2
        minDh = mid + 1
        #print("current path w =", mid)
        # TODO sliding window, not log lowerbound
        for id, line in enumerate(lines):   #O(n)
            leftEdge = id - 1
            rightEdge = lowerBound(lines, line + mid)   #O(log n)
            #print(lines, leftEdge, rightEdge)
            dh = horPath(prefix, suffix, leftEdge, rightEdge)
            if dh < minDh:
                minDh = dh
                break
        
        if mid < minDh:
            l = mid + 1
        else:
            r = mid
    
    return l


def main():
    w, h, n = (int(x) for x in input().split())
    vertLines = dict()    # x -> array[points]
    for _ in range(n):
        x, y = (int(x) for x in input().split())
        if x not in vertLines:
            vertLines[x] = []
        vertLines[x].append((x, y))

    print(minPathWidth(w, h, n, vertLines))


class TASK_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()