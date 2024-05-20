# all valid combination of k numbers to sum up to n
# 1-9 numbers
# each number is used at most once
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        numbers = [i for i in range(1, 10)]

        def backtracking(combination, sum, numId):
            if sum == n and len(combination) == k:
                output.append(combination)
            elif sum < n and len(combination) < k:
                for id in range(numId, 9):
                    backtracking(combination + [numbers[id]], sum + numbers[id], id + 1)

        output = []
        backtracking([], 0, 0)
        return output



import unittest

class TestSolution(unittest.TestCase):
    sol = Solution()

    def testCombinationSum3(self):
        k = 3
        n = 7
        ans = [[1,2,4]]
        self.assertListEqual(self.sol.combinationSum3(k, n), ans)

        k = 3
        n = 9
        ans = [[1,2,6],[1,3,5],[2,3,4]]
        self.assertListEqual(self.sol.combinationSum3(k, n), ans)

        k = 4
        n = 1
        ans = []
        self.assertListEqual(self.sol.combinationSum3(k, n), ans)

unittest.main()
