"""
Description:
image A -> image B
using matches
matches have no common segment but can intersect
min number of matches moves to get B from A
INPUT:
n - number of matches   <= 1000
x1i y1i x2i y2i - pos of i match's ends
    n lines for A
    n lines for B
OUTPUT:
min number of matches moves to get B from A up to parallel translation
Solution:
BigOmega(n^2) ~ BigO(n^3)
1. How to save matches
dict matchesVector : list(matches)
    so if matches have the same vector we can cover them up by each other

0. Create set of pairs of matches that already checked or matched.
1. iterate over vectors in A:
        iterate over matches inside a vector in A:  O(n)
            iterate over matches inside the same vector in B: O(n)
                check if m1 and m2 in set from step 0
                move matches from A to cover B
                    count how many matched O(n)
                    add matched into the set -> optimization
                check if covered > maxCovered
    return len(a) - maxCovered

Another solution:
1. Save all possible moves N^2
2. Iterate over moves N^2
    check covered N

N^2 solution
count pairs with same parallel moves
"""
import unittest

def normalizeMatch(x1, y1, x2, y2):
    if x1 < x2 or x1 == x2 and y1 < y2:
        nx1 = x1
        nx2 = x2
        ny1 = y1
        ny2 = y2
    else:
        nx1 = x2
        nx2 = x1
        ny1 = y2
        ny2 = y1
    vec = (nx2 - nx1, ny2 - ny1)

    return vec, (nx1, ny1, nx2, ny2)
        

def readMatches(matches: dict, n: int):
    for _ in range(n):
        x1, y1, x2, y2 = (int(x) for x in input().split())
        vec, m = normalizeMatch(x1, y1, x2, y2)
        if vec not in matches:
            matches[vec] = set()
        matches[vec].add(m)

def minMoves(n: int, A: dict, B: dict):
    parallelMoves = dict()
    for vec in A:   # O(n^2)
        for m1 in A[vec]:
            for m2 in B.get(vec, set()):
                dx = m2[0] - m1[0]
                dy = m2[1] - m1[1]
                #print(m1, m2)
                parallelMoves[(dx, dy)] = parallelMoves.get((dx, dy), 0) + 1
    
    return n - (max(parallelMoves.values()) if parallelMoves else 0)


# # vec -> set of matches with vec
# def minMoves(n: int, A: dict, B: dict):
#     checkedMoves = set() # set of checked covered pairs
#     maxCovered = 0
#     for vec in A:
#         for m1 in A[vec]:   # O(n)
#             for m2 in B.get(vec, set()):    # O(n)
#                 dx = m2[0] - m1[0]
#                 dy = m2[1] - m1[1]
#                 if (dx, dy) not in checkedMoves:
#                     checkedMoves.add((dx, dy))
#                     covered = 0
                    
#                     for vec in A:
#                         for ma in A[vec]:   #O(n)
#                             movedA = move(ma, dx, dy)
#                             if movedA in B.get(vec, set()):
#                                 covered += 1
                    
#                     if covered > maxCovered:
#                         maxCovered = covered

#     return n - maxCovered

def main():
    n = int(input())
    A = dict()
    readMatches(A, n)
    B = dict()
    readMatches(B, n)
    
    print(minMoves(n, A, B))


if __name__ == "__main__":
    main()