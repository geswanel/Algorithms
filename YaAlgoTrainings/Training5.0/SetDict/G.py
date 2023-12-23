"""
Description:
N points on the plane
all coords => integer numbers
min number of points so 4 points on the square vertices
INPUT:
N <= 2000
xi yi - N lines
OUTPUT
number of points
xj yj - their coords
Solution:
N points
1. Create set of points
2. If len(set)
    1 => 3 points
    2 => 2 points
    more =>
    3. Pair of points generate 2 possible rectangles => 2 points 
        iterate over all pairs of points
            generate another possible pairs of points that alltogether make a rectangle
            check if this points exists in the set
                if 2 exists => rectangle found => answer 0
                if 1 exist => 3 points found => save this points
    4. generate rectangle using 2 or 3 points if there wasn't rectangle

"""
import unittest
import time


def makeRect(points):
    if len(points) == 0:    # O(1)
        return (0, 0), (0, 1), (1, 0), (1, 1)
    elif len(points) == 1:  # O(1)
        x, y = points.pop()
        return (x + 1, y), (x, y + 1), (x + 1, y + 1)
    else:
        pList = list(points)    # O(n)
        rect = tuple()
        rectPoints = 0
        for i in range(len(pList)):
            for j in range(i + 1, len(pList)):
                p1, p2 = pList[i], pList[j]
                dx = p1[0] - p2[0]; dy = p1[1] - p2[1]
                np11, np12 = (p1[0] + dy, p1[1] - dx), (p2[0] + dy, p2[1] - dx)
                np21, np22 = (p1[0] - dy, p1[1] + dx), (p2[0] - dy, p2[1] + dx)
                rectPoints1 = 2 + (np11 in points) + (np12 in points)
                rectPoints2 = 2 + (np21 in points) + (np22 in points)
                if rectPoints1 >= rectPoints2 and rectPoints1 > rectPoints:
                    rectPoints = rectPoints1
                    rect = (p1, p2, np11, np12)
                elif rectPoints2 > rectPoints1 and rectPoints2 > rectPoints:
                    rectPoints = rectPoints2
                    rect = (p1, p2, np21, np22)
                
                if rectPoints == 4:
                    return tuple()
        
        return tuple(p for p in rect if p not in points)


def main():
    N = int(input())
    points = set()
    for _ in range(N):  # O(n)
        p = input().split()
        points.add((int(p[0]), int(p[1])))
    
    newPoints = makeRect(points)
    print(len(newPoints))
    for p in newPoints:
        print(p[0], p[1])

if __name__ == "__main__":
    main()