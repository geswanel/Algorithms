"""
n piles
piles[i] bananas
h hours

k - bananas eating per hour
Can choose pile and eat <= k bananas in an hour but only from chosen pile

min k so all bananas can be eaten

h >= n => max(piles) - max value
0 - min value

before minK => cannot eat all in h
after K => can eat all in h

log(1e9) - iterating for K
n - checking if can eat everything
O(n * log(1e9))
"""
from typing import List

class Solution:
    def time(self, bananas, k):
        return bananas // k + (bananas % k > 0)

    def canEat(self, piles, k, h):
        t = 0
        for pile in piles:
            t += self.time(pile, k)
        
        return t <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kMin = 1
        kMax = max(piles)
        while kMin < kMax:
            kMid = (kMin + kMax) // 2
            if self.canEat(piles, kMid, h):
                kMax = kMid
            else:
                kMin = kMid + 1
        
        return kMin


import unittest

class TestSolution(unittest.TestCase):
    sol = Solution()
    def testMinEatingSpeed(self):
        piles = [3,6,7,11]
        h = 8
        self.assertEqual(self.sol.minEatingSpeed(piles, h), 4)

        piles = [3,6,7,11]
        h = 4
        self.assertEqual(self.sol.minEatingSpeed(piles, h), 11, "h == piles.size()")

        piles = [30,11,23,4,20]
        h = 5
        self.assertEqual(self.sol.minEatingSpeed(piles, h), 30)

        piles = [30,11,23,4,20]
        h = 6
        self.assertEqual(self.sol.minEatingSpeed(piles, h), 23)

unittest.main()