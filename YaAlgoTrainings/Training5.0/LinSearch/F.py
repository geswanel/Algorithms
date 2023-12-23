"""
Fortune wheel
v - anglular velocit
When changing a sector => v reduced by 5
v<= k => stop at the current sector

v in range [a, b] in any direction

INPUT:
n - number of sectors <=100
n numbers <=1000. Clockwise order. Initially the arrow points to the first number
a b k
OUTPUT:
max prize

SOLUTION:
1. using a b and k => find sector window where the arrow can stop in both directions
    [minSector, maxSector] or [-maxSector, -minSector]
    use % n to find out index
2. Find max prize within this windows

v = r1*k + r2
lastSector = r1 - (r2 == 0 and r1 != 0)
if r1 == r2 == 0:
    0 sector
elif r2 == 0:   v <= k
    r1 - 1 sector
else:
    r1
"""
import unittest

def farthestSector(v, k):
    return v // k - (v % k == 0 and v // k > 0)

def maxPrize(n, prizes, a, b, k):
    minSectors = farthestSector(a, k)
    maxSectors = farthestSector(b, k)
    if maxSectors - minSectors + 1 >= n:
        return max(prizes)

    maxPrize = 0
    for sector in range(minSectors, maxSectors + 1):
        maxPrize = max(maxPrize, prizes[sector % n], prizes[(-sector) % n])
    
    return maxPrize

def main():
    n = int(input())
    prizes = [int(x) for x in input().split()]
    a, b, k = [int(x) for x in input().split()]
    print(maxPrize(n, prizes, a, b, k))


class F_Test(unittest.TestCase):
    def test_maxPrize(self):
        n = 5
        prizes = [1, 2, 3, 4, 5]
        a, b, k = 3, 5, 2
        self.assertEqual(maxPrize(n, prizes, a, b, k), 5)

        n = 5
        prizes = [5, 4, 3, 2, 1]
        a, b, k = 2, 5, 2
        self.assertEqual(maxPrize(n, prizes, a, b, k), 5)

        n = 5
        prizes = [1, 2, 3, 4, 5]
        a, b, k = 15, 15, 2
        self.assertEqual(maxPrize(n, prizes, a, b, k), 4)




if __name__ == "__main__":
    #unittest.main()
    main()