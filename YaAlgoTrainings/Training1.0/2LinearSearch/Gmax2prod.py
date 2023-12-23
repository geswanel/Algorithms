# Find the biggest production of 2 numbers

# print them in ASC order
# Answer is definite
from typing import List


def prod2Ans(maxNum, max2Num, minNum, min2Num, zero):
    if maxNum and max2Num and minNum and min2Num:
        if maxNum * max2Num >= minNum * min2Num:
            return max2Num, maxNum
        else:
            return minNum, min2Num
    elif maxNum and max2Num:
        return max2Num, maxNum
    elif minNum and min2Num:
        return minNum, min2Num
    elif (maxNum or max2Num) and (minNum or min2Num):
        # if 0 exists => 0 pos and 0 neg - 2 different answers
        return minNum or min2Num, maxNum or max2Num
    else:
        # either 0 0 or 0 neg or pos 0
        if maxNum or max2Num:
            return 0, maxNum or max2Num
        elif minNum or min2Num:
            return minNum or min2Num, 0
        else:
            return 0, 0


def max2ProdNums(nums : List[int]):
    maxNum, max2Num, minNum, min2Num = None, None, None, None
    zero = None

    for num in nums:
        if num > 0:
            if maxNum is None or num > maxNum:
                max2Num = maxNum
                maxNum = num
            elif max2Num is None or num > max2Num:
                max2Num = num
        elif num < 0:
            if minNum is None or num < minNum:
                min2Num = minNum
                minNum = num
            elif min2Num is None or num < min2Num:
                min2Num = num
        else:
            zero = 0
    
    return prod2Ans(maxNum, max2Num, minNum, min2Num, zero)
    

def main():
    nums = [int(x) for x in input().split()]
    print(*max2ProdNums(nums))


main()