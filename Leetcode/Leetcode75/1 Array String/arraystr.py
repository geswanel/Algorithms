class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        char_list = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                char_list.append(word1[i])
            if i < len(word2):
                char_list.append(word2[i])
        return "".join(char_list)

    def isDivided(self, stri : str, divider: str):
        div = divider
        while len(div) < len(stri):
            div += divider
        
        return div == stri

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divider = ""
        res = ""
        i = 0
        while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
            divider += str1[i]
            if self.isDivided(str1, divider) and self.isDivided(str2, divider):
                res = divider
            
            i += 1
        
        return res
    
    def reverseWords(self, s: str) -> str:
        words_list = s.split()
        return " ".join(words_list[::-1])
    
    def increasingTriplet(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 2):
            while 0 < i < len(nums) - 3 and nums[i] >= nums[i + 1]:
                i += 1
            for j in range(i + 1, len(nums) - 1):
                while j < len(nums) - 2 and nums[j] >= nums[j + 1] and nums[j + 1] > nums[i]:
                    j += 1
                for k in range(j + 1, len(nums)):
                    while k < len(nums) - 1 and nums[k] >= nums[k + 1] and nums[k + 1] > nums[j]:
                        k += 1
                    if nums[i] < nums[j] < nums[k]:
                        return True
        
        return False
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_product = [1]
        suffix_product = [1]
        for i in range(1, len(nums)):
            prefix_product.append(prefix_product[-1] * nums[i - 1])
            suffix_product.append(suffix_product[-1] * nums[-i])
        
        ans = []
        for i in range(len(prefix_product)):
            ans.append(prefix_product[i] * suffix_product[-(i + 1)])
        
        return ans
    
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_cand = max(candies)
        return [cand + extraCandies >= max_cand for cand in candies]

    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] != 1 and \
                (i == 0 or flowerbed[i - 1] != 1) and \
                    (i == (len(flowerbed) - 1) or flowerbed[i + 1] != 1):
                n -= 1
                i += 1
            i += 1
        
        return n == 0
    
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'u', 'o', 'i', 'e'}
        s_list = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and s_list[l].lower() not in vowels:
                l += 1
            while l < r and s_list[r].lower() not in vowels:
                r -= 1
            if l < r:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1  
        
        return "".join(s_list)
    
    def compress(self, chars: list[str]) -> int:
        cur_id = -1
        for i in range(len(chars)):
            if cur_id == -1 or chars[cur_id] != chars[i]:
                cur_id = i
            cnt = 0
            while i < len(chars):
                pass
        return 0





import unittest
class Test(unittest.TestCase):
    def test_reverseVowels(self):
        sol = Solution()
        s = "hello"
        self.assertEqual(sol.reverseVowels(s), "holle")

        s = "leetcode"
        self.assertEqual(sol.reverseVowels(s), "leotcede")

        s = ""
        self.assertEqual(sol.reverseVowels(s), "")

        s = "a"
        self.assertEqual(sol.reverseVowels(s), "a")

        s = "aue"
        self.assertEqual(sol.reverseVowels(s), "eua")

        s = "au"
        self.assertEqual(sol.reverseVowels(s), "ua")

        s = "aA"
        self.assertEqual(sol.reverseVowels(s), "Aa")
        




if __name__ == "__main__":
    unittest.main()