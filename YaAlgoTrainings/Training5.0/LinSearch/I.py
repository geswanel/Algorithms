"""
Description:
NxN board
N ships - each takes a cell
Linear tactic => All N ships in the same col
Each round a ship can be moved in 4 directions by sides of the cell.
Number of col is not important
Figure out the minimal rounds to place all ships in the same column.
Ships cannot be in the same cell

INPUT:
N <= 100
rowi coli - position of the i ship. i []
OUTPUT
min number of rounds
Solution:
1. Make effective moves so each ship placed on different rows
2. Iterate through columns an count a number of moves. Sum of differences
"""
import unittest

def oneInRow(N, rowsCnt):
    blankRows = []
    moves = 0
    for row, cnt in enumerate(rowsCnt):
        if cnt > 1:
            # from left
            while blankRows and cnt > 1:
                moves += row - blankRows.pop()
                cnt -= 1
            # from right
            nextRow = row + 1
            while cnt > 1:
                if rowsCnt[nextRow] == 0:
                    cnt -= 1
                    rowsCnt[nextRow] = 1
                    moves += nextRow - row
                nextRow += 1
        elif cnt == 0:
            blankRows.append(row)
    
    return moves

def minMovesToCol(N, colCnt):
    prefix = [0] * N
    suffix = [0] * N
    movesToCol = 0
    for col in range(N):
        prefix[col] = colCnt[col] + (prefix[col - 1] if col > 0 else 0)
        suffix[-1 - col] = colCnt[-1 - col] + (suffix[-1 - col + 1] if col > 0 else 0)
        movesToCol += (col - 0) * colCnt[col]
    
    minMoves = movesToCol
    col = 0
    while col + 1 < N:
        movesToCol += prefix[col] - suffix[col + 1]
        col += 1
        if movesToCol < minMoves:
            minMoves = movesToCol
    
    return minMoves
        


def minMoves(N, coords):
    rowsCnt = [0] * N
    colCnt = [0] * N
    for row, col in coords:
        rowsCnt[row - 1] += 1
        colCnt[col - 1] += 1
    
    # 1 step
    return oneInRow(N, rowsCnt) + minMovesToCol(N, colCnt)


def main():
    N = int(input())
    coords = [tuple(int(coord) for coord in input().split()) for _ in range(N)]
    print(minMoves(N, coords))


class I_Test(unittest.TestCase):
    def test_oneInRow(self):
        rowCnt = [5, 0, 0, 0, 0]
        moves = 10
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [0, 0, 0, 0, 5]
        moves = 10
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [0, 0, 5, 0, 0]
        moves = 6
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [0, 5, 0, 0, 0]
        moves = 7
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [0, 0, 0, 5, 0]
        moves = 7
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [4, 0, 0, 0, 1]
        moves = 6
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [4, 0, 0, 1, 0]
        moves = 7
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [1, 0, 0, 0, 4]
        moves = 6
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [0, 1, 0, 0, 4]
        moves = 7
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [1, 0, 0, 4, 0]
        moves = 4
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [0, 1, 0, 4, 0]
        moves = 5
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)

        rowCnt = [0, 3, 0, 2, 0]
        moves = 3
        self.assertEqual(oneInRow(len(rowCnt), rowCnt), moves)
    
    def test_movesToCol(self):
        colCnt = [5, 0, 0, 0, 0]
        moves = 0
        self.assertEqual(minMovesToCol(len(colCnt), colCnt), moves)

        colCnt = [4, 0, 0, 0, 1]
        moves = 4
        self.assertEqual(minMovesToCol(len(colCnt), colCnt), moves)
        
        colCnt = [4, 0, 0, 1, 0]
        moves = 3
        self.assertEqual(minMovesToCol(len(colCnt), colCnt), moves)

        colCnt = [3, 0, 0, 0, 2]
        moves = 8
        self.assertEqual(minMovesToCol(len(colCnt), colCnt), moves)

        colCnt = [2, 4, 5, 5, 1]
        moves = 15
        self.assertEqual(minMovesToCol(len(colCnt), colCnt), moves)


if __name__ == "__main__":
    #unittest.main()
    main()