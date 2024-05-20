from typing import List


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        for bit in range(32):
            abit, bbit, cbit = self.getBits(a, b, c, bit=bit)
            if abit | bbit != cbit:
                if cbit == 1:
                    cnt += 1
                else:
                    cnt += abit + bbit
                
        return cnt

    def getBits(self, *nums: List[int], bit: int):
        return tuple(num >> bit & 1 for num in nums)


import unittest

class SolutionTest(unittest.TestCase):
    def testSolution(self):
        sol = Solution()

        a = 2
        b = 6
        c = 5
        ans = 3
        self.assertEqual(sol.minFlips(a, b, c), ans)

        a = 4
        b = 2
        c = 7
        ans = 1
        self.assertEqual(sol.minFlips(a, b, c), ans)

        a = 1
        b = 2
        c = 3
        ans = 0
        self.assertEqual(sol.minFlips(a, b, c), ans)


if __name__ == "__main__":
    unittest.main()
