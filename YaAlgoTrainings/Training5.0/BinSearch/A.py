"""
Description:
N numbers
How many from L to R
INPUT:
N 1e5
N numbers
K 1e5 - requests
Li Ri - i request
OUTPUT
K numbers
Solution:
1. Sort array
2. Find L and R position using Bin search O(logN)
3. return answer
"""
import unittest

def lowerBound(nums, val):
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < val:
            l = mid + 1
        else:
            r = mid
    
    return l

def response(nums, requests):
    nums.sort()
    ans = []
    for l, r in requests:
        lId = lowerBound(nums, l)
        rId = lowerBound(nums, r + 1)
        ans.append(rId - lId)

    return ans

def main():
    N = int(input())
    nums = [int(x) for x in input().split()]
    K = int(input())
    requests = []
    for _ in range(K):
        l, r = (int(x) for x in input().split())
        requests.append((l, r))

    print(" ".join(str(x) for x in response(nums, requests)))

class TASK_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()