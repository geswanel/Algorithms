# dp[i][j] = length of longest common subsequence of text1[:i] and text2[:j]
# dp[i + 1][j + 1] = 
#   if text1[i] == text2[j]: dp[i][j]
#   else: max dp[i + 1, j] dp[i, j + 1]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = self.initDP(text1, text2)

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[-1][-1]

    def initDP(self, text1: str, text2: str):
        dp = [[0] * len(text2) for _ in range(len(text1))]
        dp[0][0] = int(text1[0] == text2[0])
        for j in range(1, len(text2)):
            dp[0][j] = max(int(text1[0] == text2[j]), dp[0][j - 1])

        for i in range(1, len(text1)):
            dp[i][0] = max(int(text1[i] == text2[0]), dp[i - 1][0])
        
        return dp
        

import unittest

class SolutionTest(unittest.TestCase):
    def testSolution(self):
        sol = Solution()

        text1 = "abcde"
        text2 = "ace" 
        ans = 3
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), ans)

        text1 = "abc"
        text2 = "abc" 
        ans = 3
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), ans)

        text1 = "abc"
        text2 = "def" 
        ans = 0
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), ans)


if __name__ == "__main__":
    unittest.main()
