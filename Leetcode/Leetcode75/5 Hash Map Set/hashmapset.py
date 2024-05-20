class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_hash = set(nums1)
        nums2_hash = set(nums2)
        ans = []
        # nums1_dif = set()
        # for el in nums1:
        #     if el not in nums2_hash and el not in nums1_dif: #difference and distinct
        #         nums1_dif.add(el)
        # ans.append(list(nums1_dif))
        ans.append(list(nums1_hash.difference(nums2_hash))) # difference function
        ans.append(list(nums2_hash.difference(nums1_hash)))

        return ans
    
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurences_cnt = dict()
        for el in arr:
            occurences_cnt[el] = occurences_cnt.get(el, 0) + 1
        
        unique_occ = set(occurences_cnt.values())
        return len(unique_occ) == len(occurences_cnt)
    
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        w1_dict = dict()
        w2_dict = dict()
        for i in range(len(word1)):
            w1_dict[word1[i]] = w1_dict.get(word1[i], 0) + 1
            w2_dict[word2[i]] = w2_dict.get(word2[i], 0) + 1
        
        if w1_dict.keys() != w2_dict.keys() or sorted(w1_dict.values()) != sorted(w2_dict.values()):
            return False
        
        return True



import unittest

class Test(unittest.TestCase):
    def test_closeStrings(self):
        sol = Solution()
        word1 = "abc"
        word2 = "bca"
        self.assertTrue(sol.closeStrings(word1, word2))

        word1 = "aa"
        word2 = "a"
        self.assertFalse(sol.closeStrings(word1, word2))

        word1 = "cabbba"
        word2 = "abbccc"
        self.assertTrue(sol.closeStrings(word1, word2))

        word1 = "aaabbbbccddeeeeefffff"
        word2 = "aaaaabbcccdddeeeeffff"
        self.assertFalse(sol.closeStrings(word1, word2))


if __name__ == "__main__":
    unittest.main()