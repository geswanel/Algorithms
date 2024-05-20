# mxn grid. Number of path from 0,0 to m - 1, n - 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][:] = [1] * n
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]


import unittest

class SolutionTest(unittest.TestCase):
    def testSolution(self):
        sol = Solution()

        m, n = 3, 7
        ans = 28
        self.assertEqual(sol.uniquePaths(m, n), ans)

        m, n = 1, 1
        ans = 1
        self.assertEqual(sol.uniquePaths(m, n), ans)

        m, n = 1, 5
        ans = 1
        self.assertEqual(sol.uniquePaths(m, n), ans)

        m, n = 5, 1
        ans = 1
        self.assertEqual(sol.uniquePaths(m, n), ans)

        m, n = 3, 2
        ans = 3
        self.assertEqual(sol.uniquePaths(m, n), ans)


if __name__ == "__main__":
    unittest.main()
