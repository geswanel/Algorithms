"""
Description:
Anagram checking of 2 strings
INPUT:
s1
s2
OUTPUT
YES or NO
Solution:
dict of symbols. Compare dicts
"""
import unittest

def countSymbols(s1):
    ans = dict()
    for c in s1:
        ans[c] = ans.get(c, 0) + 1
    return ans

def main():
    s1 = input()
    s2 = input()
    s1Dict = countSymbols(s1)
    s2Dict = countSymbols(s2)
    print("YES" if s1Dict == s2Dict else "NO")

class B_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()