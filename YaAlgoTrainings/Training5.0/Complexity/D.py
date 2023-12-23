"""
Bishops and rooks on 8x8 chess board
How many not beatable cells

B - bishop
R - rook

INPUT: *BR symbols 8x8 matrix

Brute Force
"""
rookStep = ((1, 0), (-1, 0), (0, 1), (0, -1))
bishopStep = ((1, 1), (1, -1), (-1, 1), (-1, -1))

def isValid(r, c):
    return 0 <= r < 8 and 0 <= c < 8

def processCell(board, r, c):
    steps = rookStep if board[r][c] == "R" else bishopStep

    for step in steps:
        pos = [r + step[0], c + step[1]]
        while isValid(*pos) and board[pos[0]][pos[1]] not in "RB":
            board[pos[0]][pos[1]] = board[r][c].lower()
            pos[0] += step[0]
            pos[1] += step[1]


def notBeatableCells(board):
    ans = 0
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell in "RB":
                processCell(board, r, c)
    
    return sum(row.count("*") for row in board)
    

def main():
    board = [["*" if x == "*" else x for x in input().strip()] for _ in range(8)]
    print(notBeatableCells(board))


if __name__ == "__main__":
    main()