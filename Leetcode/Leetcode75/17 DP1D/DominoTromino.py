
# Have two kind of tiles. How many ways it's possible to fill 2xn field
# dp[i] stores how many ways for 2xi field
# Previous combination should't repeat in next calculation
# dp[i] = 
#           dp[i - 1] + (last domino vertical)
#           dp[i - 2] + (two last dominos horizontal, not vertical because it's considered before)
#           dp[i - 3] * 2 (2 tromino combinations to fill 2x3 field, all domino combinations considered)
#           dp[i - 4] * 2 (2 tromino and domino combinations to fill 2x4)
#           all sum till dp[0] * 2 (2 tromino and horizontal domino combinations)
#           Let's also have prefix sum not to sum every time
class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 1:
            return n
        
        prefix_sum = [0] * (n + 1)  # p[i] sum of combinations 2xj for j in [1, i]
        prefix_sum[0] = 1   # So formula works well for i = 3
        dp = [0] * (n + 1)
        dp[1], prefix_sum[1] = 1, 2
        dp[2], prefix_sum[2] = 2, 4
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + prefix_sum[i - 3] * 2
            prefix_sum[i] = prefix_sum[i - 1] + dp[i]
        
        return dp[n] % (int(1e9) + 7)


import unittest

class SolutionTest(unittest.TestCase):
    def testSolution(self):
        sol = Solution()

        n = 1
        ans = 1
        self.assertEqual(sol.numTilings(n), ans)

        n = 3
        ans = 5
        self.assertEqual(sol.numTilings(n), ans)

        n = 0
        ans = 0
        self.assertEqual(sol.numTilings(n), ans)

        n = 10
        ans = 1225
        self.assertEqual(sol.numTilings(n), ans)


if __name__ == "__main__":
    unittest.main()

