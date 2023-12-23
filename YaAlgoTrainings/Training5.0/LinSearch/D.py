"""
Side length of figure sawn from chess board.

INPUT:
N - number of sawn cells
row col - [1, 8] of cell in N lines
OUTPUT:
perimeter

Solution:
Create a 2D array 8x8 of cells. True - cells in sawn figure, False - not in sawn figure
For each cell in sawn figure identify if it's surrounded by another sawn cells
    perimeter += 4 - surrounded
"""

def cntAround(figure, r, c):
    return (c - 1 >= 0 and figure[r][c - 1]) + \
        (c + 1 < 8 and figure[r][c + 1]) + \
        (r - 1 >= 0 and figure[r - 1][c]) + \
        (r + 1 < 8 and figure[r + 1][c])

def perimeter(figure):
    ans = 0
    for r, row in enumerate(figure):
        for c, cell in enumerate(row):
            if cell:
                ans += 4 - cntAround(figure, r, c)
    
    return ans

def main():
    N = int(input())
    figure = [[False for _ in range(8)] for _ in range(8)]
    for _ in range(N):
        r, c = [int(x) for x in input().split()]
        figure[r - 1][c - 1] = True
    
    print(perimeter(figure))


if __name__ == "__main__":
    main()