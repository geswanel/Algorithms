# Given nums
# Find 3 numbers which product is max
from typing import List


def prod3Ans(maxNum, max2Num, max3Num, minNum, min2Num):
    if maxNum and max2Num and max3Num and minNum and min2Num:
        if max2Num * max3Num >= minNum * min2Num:
            return max3Num, max2Num, maxNum
        else:
            return minNum, min2Num, maxNum
    elif max3Num:
        return max3Num, max2Num, maxNum
    elif maxNum and min2Num:
        return minNum, min2Num, maxNum
    elif min2Num:
        return None
    else:
        return 0, 0, 0


def max3ProdNums(nums : List[int]):
    maxNum, max2Num, max3Num, minNum, min2Num = None, None, None, None, None

    for num in nums:
        if num > 0:
            if maxNum is None or num > maxNum:
                max3Num = max2Num
                max2Num = maxNum
                maxNum = num
            elif max2Num is None or num > max2Num:
                max3Num = max2Num
                max2Num = num
            elif max3Num is None or num > max3Num:
                max3Num = num
        elif num < 0:
            if minNum is None or num < minNum:
                min2Num = minNum
                minNum = num
            elif min2Num is None or num < min2Num:
                min2Num = num
    
    ans = prod3Ans(maxNum, max2Num, max3Num, minNum, min2Num)
    if ans is None:
        for num in nums:
            if maxNum is None or num > maxNum:
                max3Num = max2Num
                max2Num = maxNum
                maxNum = num
            elif max2Num is None or num > max2Num:
                max3Num = max2Num
                max2Num = num
            elif max3Num is None or num > max3Num:
                max3Num = num
        ans = (max3Num, max2Num, maxNum)
    return ans


def main():
    nums = [int(x) for x in input().split()]
    if len(nums) == 3:
        print(*nums)
    else:
        print(*max3ProdNums(nums))


main()
