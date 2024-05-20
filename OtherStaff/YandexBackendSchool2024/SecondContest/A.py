"""
Description:
Infinite tic tac toe
5 in line or diagonal

You have log of rounds => identify who won or if players continued 
    after won wihtout noticing
INPUT:
n - 1e4 - number of steps
r c - row and column of next step (x or o)
OUTPUT:
First | Second | Draw | Inattention (if continued)
Solution:
0. For each step check if this step finished the game
1. How to save steps? dict[row: dict[col: player]]
2. How to check? check 4 directions
    - hor [col - 1 , col + 1] and try to make 5
    - vert [row -1, row + 1] and try to make 5
    - Diag1[row + 1, col + 1], [row - 1, col - 1]
    - Diag2[row + 1, col + 1], [row - 1, col - 1]
"""
def checkForWin(field, r, c):
    player = field[r][c]
    empty = dict()
    # hor
    cnt = 1
    i = 1
    while field[r].get(c - i, -1) == player:
        i += 1
        cnt += 1
    
    i = 1
    while field[r].get(c + i, -1) == player:
        i += 1
        cnt += 1
    
    if cnt >= 5:
        return True
    
    # ver
    cnt = 1
    i = 1
    while field.get(r - i, empty).get(c, -1) == player:
        i += 1
        cnt += 1
    
    i = 1
    while field.get(r + i, empty).get(c, -1) == player:
        i += 1
        cnt += 1
    
    if cnt >= 5:
        return True
    
    # diag1
    cnt = 1
    i = 1
    while field.get(r + i, empty).get(c + i, -1) == player:
        i += 1
        cnt += 1
    
    i = 1
    while field.get(r - i, empty).get(c - i, -1) == player:
        i += 1
        cnt += 1
    
    if cnt >= 5:
        return True
    
    # diag2
    cnt = 1
    i = 1
    while field.get(r + i, empty).get(c - i, -1) == player:
        i += 1
        cnt += 1
    
    i = 1
    while field.get(r - i, empty).get(c + i, -1) == player:
        i += 1
        cnt += 1
    
    if cnt >= 5:
        return True
    
    return False


def processGame(n, steps):
    """
    i % 2 == 0 => First
    i % 2 == 1 => Second
    """
    field = dict()
    for i in range(n):
        r, c = steps[i]
        if r not in field:
            field[r] = dict()
        field[r][c] = i % 2
        if (checkForWin(field, r, c)):
            if i == n - 1:
                return "First" if i % 2 == 0 else "Second"
            else:
                return "Inattention"
    
    return "Draw"

def main():
    n = int(input())
    steps = []
    for i in range(n):
        r, c = [int(x) for x in input().split()]
        steps.append((r, c))

    ans = processGame(n, steps)
    print(ans)


if __name__ == "__main__":
    main()