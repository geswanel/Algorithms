class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix_sum = [0]
        for num in gain:
            prefix_sum.append(prefix_sum[-1] + num)
        
        return max(prefix_sum)

    def pivotIndex(self, nums: list[int]) -> int:
        prefix_sum = 0
        suffix_sum = sum(nums[1:])
        i = 0
        while i < len(nums):
            if prefix_sum == suffix_sum:
                return i
            i += 1
            prefix_sum += nums[i - 1]
            if i < len(nums):
                suffix_sum -= nums[i]
            
        return -1



def main():
    sol = Solution()
    print(sol.pivotIndex([1,7,3,6,5,6]))
    print(sol.pivotIndex([1,2,3]))
    print(sol.pivotIndex([2,1,-1]))

if __name__ == "__main__":
    main()