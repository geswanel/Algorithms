# by digits return possible strings
# digits.length = 4
# 3^4 variants

from typing import List

# class Solution:
#     letters = {
#         '2': "abc",
#         '3': "def",
#         '4': "ghi",
#         '5': "jkl",
#         '6': "mno",
#         '7': "pqrs",
#         '8': "tuv",
#         '9': "wxyz"
#     }

#     def letterCombinations(self, digits: str) -> List[str]:
#         s = [[]] if digits else []
#         for digit in digits:
#             sLen = len(s)
#             letter = self.letters[digit]
#             for cId in range(1, len(letter)):
#                 for i in range(sLen):
#                     s.append(s[i] + [letter[cId]])
            
#             for i in range(sLen):
#                 s[i].append(letter[0])
        
#         return ["".join(sList) for sList in s]


class Solution:
    letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def backtracking(combination, digitId):
            if digitId == len(digits):
                output.append(combination)
            else:
                for c in self.letters[digits[digitId]]:
                    backtracking(combination + c, digitId + 1)
        
        output = []
        backtracking("", 0)
        return output

import unittest

class TestSolution(unittest.TestCase):
    sol = Solution()

    def testLetterCombinations(self):
        digits = "23"
        ans = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertSetEqual(set(self.sol.letterCombinations(digits)), set(ans))

        digits = ""
        ans = []
        self.assertSetEqual(set(self.sol.letterCombinations(digits)), set(ans))

        digits = "2"
        ans = ["a","b","c"]
        self.assertSetEqual(set(self.sol.letterCombinations(digits)), set(ans))


unittest.main()
