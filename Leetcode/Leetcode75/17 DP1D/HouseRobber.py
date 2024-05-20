from typing import List

# Cannot rob two adjacent houses
# dp[i] stores max money if i house is robbed
# dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
# Why not dp[i - 4], because it's already operated for i - 2
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) + 1)
        dp[1], dp[2] = nums[0], nums[1]
        
        for i in range(2, len(nums)):
            dp[i + 1] = max(dp[i - 1], dp[i - 2]) + nums[i]
        

        return max(dp[-1], dp[-2])


import unittest

class SolutionTest(unittest.TestCase):
    def testSolution(self):
        sol = Solution()

        nums = [1,2,3,1]
        ans = 4
        self.assertEqual(sol.rob(nums), ans)

        nums = [2,7,9,3,1]
        ans = 12
        self.assertEqual(sol.rob(nums), ans)

        nums = [1]
        ans = 1
        self.assertEqual(sol.rob(nums), ans)


if __name__ == "__main__":
    unittest.main()