class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        next0_id = 0
        nextnum_id = 0
        while next0_id < len(nums) and nextnum_id < len(nums):
            while next0_id < len(nums) and nums[next0_id] != 0:
                next0_id += 1
            
            nextnum_id = next0_id + 1
            while nextnum_id < len(nums) and nums[nextnum_id] == 0:
                nextnum_id += 1

            if next0_id < len(nums) and nextnum_id < len(nums):
                nums[next0_id], nums[nextnum_id] = nums[nextnum_id], nums[next0_id]
    
    def isSubsequence(self, s: str, t: str) -> bool:
        # s subsequence of t
        s_id = 0
        t_id = 0
        while s_id < len(s) and t_id < len(t):
            if s[s_id] == t[t_id]:
                s_id += 1
            t_id += 1
        
        return s_id == len(s)
    
    def maxArea(self, height: list[int]) -> int:
        area = lambda st, fi: min(height[st], height[fi]) * (fi - st)
        s = 0
        max = 0
        for f in range(len(height)):
            ar = area(s, f)
            if ar > max:
                max = ar
            if height[f] > height[s]:
                s = f
        return max
    
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                ans += 1
                l += 1
                r -= 1
        
        return ans
            

class Test:
    def test_maxArea(self):
        sol = Solution()
        height = [1,8,6,2,5,4,8,3,7]
        print(sol.maxArea(height) == 49)

        height = [1, 1]
        print(sol.maxArea(height) == 1)
    
    def test_maxOperations(self):
        sol = Solution()
        nums = [1,2,3,4]
        k = 5
        print(sol.maxOperations(nums, k) == 2)

        nums = [3,1,3,4,3]
        k = 6
        print(sol.maxOperations(nums, k) == 1)

        nums = []
        k = 1
        print(sol.maxOperations(nums, k) == 0)
        
        nums = [1]
        k = 1
        print(sol.maxOperations(nums, k) == 0)













def main():
    test = Test()
    test.test_maxOperations()


if __name__ == "__main__":
    main()