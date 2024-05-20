from typing import List

"""
Bin search
m - 1 m m + 1
increasing => right segment
decresing => left segment
Minimum => any segment
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            elif nums[m - 1] > nums[m]:
                r = m
            else:
                return m

        return l

import unittest


class SolutionTest(unittest.TestCase):
    sol = Solution()
    def testfindPeakElement(self):
        nums = [1,2,3,1]
        self.assertIn(self.sol.findPeakElement(nums), [2], "Inside")

        nums = [2,1,0,-1]
        self.assertIn(self.sol.findPeakElement(nums), [0], "At the start")

        nums = [1,2,3,4]
        self.assertIn(self.sol.findPeakElement(nums), [3], "At the end")

        nums = [1, 2, 3, 1, 0, 1, 0]
        self.assertIn(self.sol.findPeakElement(nums), [2, 5], "2 inside")

unittest.main()