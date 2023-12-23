"""
Description:
nxm field, some cells are suitable for building and some aren't
+ sign with size of k => 5 squares kxk => 1 in the center and 1 by each side of center square
Find max k for it
INPUT:
n m ~ 2000
n lines of m symbols # for suitable and . for not
OUTPUT
max k
Solution:
1. Make prefix, suffix sum of contiguous cells for rows and columns O(n^2)
2. Binary search over k O(logn)
    3. for each k iterate over all cells that can be left top corner of middle square O(n^2)
        for O(k) check if the + sign can be build
"""
import unittest

# class CellPrefixSuffix:
#     def __init__(self):
#         self.prefLeft = 0
#         self.prefTop = 0
#         self.sufRight = 0
#         self.sufBottom = 0

# def buildPrefSuf(n, m, field):
#     # prefix or suffix value = how many contiguous cells are suitable including current
#     prefSufField = [[CellPrefixSuffix() for _ in range(m)] for _ in range(n)]
#     for i in range(n):  # over rows
#         prefSufField[i][0].prefLeft = int(field[i][0] == '#')
#         prefSufField[i][m - 1].sufRight = int(field[i][m - 1] == '#')
#     for j in range(m):
#         prefSufField[0][j].prefTop = int(field[0][j] == '#')
#         prefSufField[n - 1][j].sufBottom = int(field[n - 1][j] == '#')
    
#     for i in range(1, n - 1):
#         for j in range(1, m - 1):
#             if field[i][j] == '#':
#                 prefSufField[i][j].prefLeft = prefSufField[i][j - 1].prefLeft + 1
#                 prefSufField[i][j].prefTop = prefSufField[i - 1][j].prefTop + 1
#             else:
#                 prefSufField[i][j].prefLeft = prefSufField[i][j].prefTop = 0
            
#             if field[-1 - i][-1 - j] == '#':
#                 prefSufField[-1 - i][-1 - j].sufRight = prefSufField[-1 - i][-1 - j + 1].sufRight + 1
#                 prefSufField[-1 - i][-1 - j].sufBottom = prefSufField[-1 - i + 1][-1 - j].sufBottom + 1
#             else:
#                 prefSufField[-1 - i][-1 - j].sufRight = prefSufField[-1 - i][-1 - j].sufBottom = 0
    
#     return prefSufField

# def canBuild(n, m, k, field, prefSufField):
#     for i in range(k, n - 2 * k + 1):
#         for j in range(k, m - 2 * k + 1):
#             leftTopReq = k + 1
#             rightBottomReq = 2 * k
#             canBeBuild = True
#             for step in range(k):
#                 if prefSufField[i + step][j].prefLeft < leftTopReq or \
#                     prefSufField[i + step][j].sufRight < rightBottomReq or \
#                     prefSufField[i][j + step].prefTop < leftTopReq or \
#                         prefSufField[i][j + step].sufBottom < rightBottomReq:
#                     canBeBuild = False
#                     break
#             if canBeBuild:
#                 return True

#     return False

def countRow(field, i, j, k):
    for step in range(k):
        if field[i][j - step - 1] != '#':
            return False
    
    for step in range(2 * k - 1):
        if field[i][j + step + 1] != '#':
            return False
    
    return True

def countCol(field, i, j, k):
    for step in range(k):
        if field[i - step - 1][j] != '#':
            return False
    
    for step in range(2 * k - 1):
        if field[i + step + 1][j] != '#':
            return False
    
    return True

def canBuild(n, m, k, field):
    for i in range(k, n - 2 * k + 1):
        for j in range(k, m - 2 * k + 1):
            if field[i][j] == '#':
                canBeBuild = True
                for step in range(k):
                    if not countRow(field, i + step, j, k) or not countCol(field, i, j + step, k):
                        canBeBuild = False

                if canBeBuild:
                    return True

    return False


def maxOfficeSize(n, m, field):
    #prefSufField = buildPrefSuf(n, m, field)
    l = 1
    r = min(n, m) // 3
    while l < r:
        mid = (l + r + 1) // 2
        if canBuild(n, m, mid, field):
            l = mid
        else:
            r = mid - 1
    
    return l

def main():
    n, m = (int(x) for x in input().split())
    field = [input() for _ in range(n)]
    print(maxOfficeSize(n, m, field))

if __name__ == "__main__":
    main()