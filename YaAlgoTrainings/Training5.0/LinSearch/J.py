"""
Description:
mxn rectangle field
there is a picture on the field
check if the picture can be represented as 2 black rectangles without intersection
INPUT:
m n <= 200
description of field "." - blank, "#" - black cell
OUTPUT
YES
    field with a for first rectangle and b for second if it's possible
NO otherwise

Solution:
m n <= 200
algorithm 2 * 200^3
iterate through rows or columns as delimeters between two sectors
Identify if there is only one rectangle in each sector
"""
import unittest

def isRectangle(picture, rect):
    if rect is None:
        return False
    
    (frow, fcol), (lrow, lcol) = rect
    if (lrow - frow + 1) * (lcol - fcol + 1) <= 0:
        return False

    for row in range(frow, lrow + 1):
        for col in range(fcol, lcol + 1):
            if picture[row][col] != '#':
                return False
    
    return True

def fillRectangle(picture, rect, filler):
    (frow, fcol), (lrow, lcol) = rect

    for row in range(frow, lrow + 1):
        for col in range(fcol, lcol + 1):
            picture[row][col] = filler

def isInside(row, col, rectCand):
    if rectCand is None:
        return False
    
    (frow, fcol), (lrow, lcol) = rectCand
    return frow <= row <= lrow and fcol <= col <= lcol

def rectInSector(picture, sector):
    (frow, fcol), (lrow, lcol) = sector
    rectCand = None
    for row in range(frow, lrow + 1):
        for col in range(fcol, lcol + 1):
            if picture[row][col] == '#' and not isInside(row, col, rectCand):
                if rectCand is not None:
                    return None
                first = (row, col)
                lastRow = row
                lastCol = col
                while lastRow + 1 <= lrow and picture[lastRow + 1][col] == '#':
                    lastRow += 1
                
                while lastCol + 1 <= lcol and picture[row][lastCol + 1] == '#':
                    lastCol += 1
                last = (lastRow, lastCol)
                rectCand = (first, last)
    return rectCand if isRectangle(picture, rectCand) else None

def checkSectors(m, n, picture, sec1, sec2):
    rect1 = rectInSector(picture, sec1)
    rect2 = rectInSector(picture, sec2)
    if rect1 is not None and rect2 is not None:
        fillRectangle(picture, rect1, 'a'); fillRectangle(picture, rect2, 'b')
        return True
    else:
        return False

def isTwoRect(m, n, picture):
    for row in range(m - 1):
        sec1 = ((0, 0), (row, n - 1))
        sec2 = ((row + 1, 0), (m - 1, n - 1))
        if checkSectors(m, n, picture, sec1, sec2):
            return True

    for col in range(n - 1):
        sec1 = ((0, 0), (m - 1, col))
        sec2 = ((0, col + 1), (m - 1, n - 1))
        if checkSectors(m, n, picture, sec1, sec2):
            return True
    
    return False


def main():
    m, n = (int(x) for x in input().split())
    picture = [list(input()) for _ in range(m)]

    if isTwoRect(m, n, picture):
        print("YES")
        for rowItems in picture:
            print("".join(str(x) for x in rowItems))
    else:
        print("NO")


class J_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()