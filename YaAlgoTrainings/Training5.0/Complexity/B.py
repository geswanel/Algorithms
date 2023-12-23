"""
home match + guest match
win = more goals or same goals and more goals as guest
    else => additional time

first match score
second match score. Match not finished not finished
How many goals for first team to win.

INPUT:
G1:G2 - first match score
GC1:GC2 - second match current score
1|2 - number of home game for the first team
"""
def requiredGoals(G1, G2, Gc1, Gc2, homeGame):
    diff = G2 - G1 + Gc2 - Gc1
    # diff goal to even the score
    if diff < 0:
        return 0
    
    if homeGame == 1 and Gc1 + diff > G2 or homeGame == 2 and G1 > Gc2:
        return diff
    else:
        return diff + 1

def main():
    G1, G2 = [int(x) for x in input().split(':')]
    Gc1, Gc2 = [int(x) for x in input().split(':')]
    homeGame = int(input())
    print(requiredGoals(G1, G2, Gc1, Gc2, homeGame))


if __name__ == "__main__":
    main()