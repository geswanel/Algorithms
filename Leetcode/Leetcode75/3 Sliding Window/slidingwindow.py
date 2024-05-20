class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum += (nums[i] - nums[i - k])
            if max_sum < window_sum:
                max_sum = window_sum
        
        return max_sum / k
    
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'u', 'i', 'o'}
        window_vowels = 0
        for i in range(k):
            window_vowels += int(s[i] in vowels)

        max_vowels = window_vowels
        for i in range(k, len(s)):
            window_vowels += int(s[i] in vowels) - int(s[i - k] in vowels)
            if max_vowels < window_vowels:
                max_vowels = window_vowels
        
        return max_vowels
    
    def longestOnes(self, nums: list[int], k: int) -> int:
        w_l = w_r = 0
        longest_seq = 0
        cur_seq = 0
        while w_r < len(nums):
            #print(nums, w_l, w_r, k)
            if nums[w_r] == 1 or nums[w_r] == 0 and k > 0:
                k -= (1 if nums[w_r] == 0 else 0)
                w_r += 1
                cur_seq += 1
            else:
                k += (0 if nums[w_l] == 1 else 1)
                w_l += 1
                longest_seq = max(longest_seq, cur_seq)
                cur_seq -= 1
        
        longest_seq = max(longest_seq, cur_seq)
        return longest_seq
        
        
                
                





import unittest

class Test(unittest.TestCase):
    def test_longestOnes(self):
        sol = Solution()
        nums = [1,1,1,0,0,0,1,1,1,1,0]
        k = 2
        self.assertEqual(sol.longestOnes(nums, k), 6)

        nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        k = 3
        self.assertEqual(sol.longestOnes(nums, k), 10)

        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1]
        k = 3
        self.assertEqual(sol.longestOnes(nums, k), 9)

        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1]
        k = 2
        self.assertEqual(sol.longestOnes(nums, k), 5)

        nums = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
        k = 4
        self.assertEqual(sol.longestOnes(nums, k), 13)

        nums = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]
        k = 4
        self.assertEqual(sol.longestOnes(nums, k), 10)


if __name__ == "__main__":
    unittest.main()