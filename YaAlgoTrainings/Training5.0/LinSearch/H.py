"""
Description:
n races and m classes of characters
character - {race and class} - unique pair
aij - power if character {i race, j class}

First player choosing character. Before that second player can prohibit one race and one class
What race and class should second player prohibit

INPUT:
n m <= 1000
aij - i row, j col
OUTPUT:
ip jp - numbers of prohibited race and class

Solution:
1. find the strongest character
2. Ban his race -> find next strongest -> ban next's class -> find last strongest
3. Ban his class -> find next strongest -> ban next's race -> find last strongest
4. Compare last strongests and choose what to ban according to it
"""
import unittest

def findStrongest(n, m, aij, pRace=-1, pClass=-1):
    strongest = None
    for race in range(n):
        for cclass in range(m):
            if race != pRace and cclass != pClass and \
                    (strongest is None or aij[race][cclass] > aij[strongest[0]][strongest[1]]):
                strongest = (race, cclass)
    
    return strongest
    
def banRaceClass(n, m, aij):
    """
    Return ids of race and class to ban. Index = id + 1
    """
    strongest = findStrongest(n, m, aij)
    # ban race, find next max -> ban class -> find last max
    nextRStrongest = findStrongest(n, m, aij, pRace=strongest[0])
    lastRStrongest = findStrongest(n, m, aij, pRace=strongest[0], pClass=nextRStrongest[1])
    
    # ban class, find next max -> ban race -> find last max
    nextCStrongest = findStrongest(n, m, aij, pClass=strongest[1])
    lastCStrongest = findStrongest(n, m, aij, pRace=nextCStrongest[0], pClass=strongest[1])

    # print(strongest)
    # print(nextRStrongest, nextCStrongest)
    # print(lastRStrongest, lastCStrongest)
    # print(aij[lastRStrongest[0]][lastRStrongest[1]], aij[lastCStrongest[0]][lastCStrongest[1]])
    if aij[lastRStrongest[0]][lastRStrongest[1]] <= aij[lastCStrongest[0]][lastCStrongest[1]]:
        return strongest[0], nextRStrongest[1]
    else:
        return nextCStrongest[0], strongest[1]

def main():
    n, m = [int(x) for x in input().split()]
    aij = [[int(x) for x in input().split()] for _ in range(n)]
    race, charClass = banRaceClass(n, m, aij)
    print(race + 1, charClass + 1)


class H_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()