"""
Description:
sorted squads of soldiers

Choosed contiguous subsequence of squads with total soldiers = sum for exploring
INPUT:
n 2*1e5 squads m 2*1e5 explorations
ai - n numbers - squads 1e9
lj sj - number of squads and number of soldiers for an exploration j
    so need to choose contiguous subsequence of lj elements so their sum = sj
OUTPUT
1. prefix sum of squad sum to check in O(1)
2. bin search for the first squad
Solution:

"""
import unittest


def findSquads(n, m, squads, explorations):
    prefixSum = [0]
    for squad in squads:
        prefixSum.append(prefixSum[-1] + squad)
    
    ans = []
    for sqCnt, totalSum in explorations:
        l = 0
        r = n - sqCnt
        while l < r:
            mid = (l + r) // 2
            if prefixSum[mid + sqCnt] - prefixSum[mid] < totalSum:
                l = mid + 1
            else:
                r = mid
        ans.append(l + 1 if prefixSum[l + sqCnt] - prefixSum[l] == totalSum else -1)
    
    return ans

def main():
    n, m = (int(x) for x in input().split())
    squads = [int(x) for x in input().split()]
    explorations = []
    for _ in range(m):
        l, s = (int(x) for x in input().split())
        explorations.append((l, s))
    ans = findSquads(n, m, squads, explorations)
    for an in ans:
        print(an)


class TASK_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()