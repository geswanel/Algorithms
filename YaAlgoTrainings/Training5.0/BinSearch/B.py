"""
Description:
1xn field for sea battle
max k, so 1xk, 2 * 1x(k-1), ... k * 1x1 ships
INPUT:
n 1e18
OUTPUT
k ans
Solution:
1. BinSearch for k from 0 to n  log(n)
    2. Check if can be placed. how Long? for 1e18 3 sec
    3. Needed space = sum{i_1^k}(i * (k - i + 1) + i) - 1
    sum{i_1^k}(i *(k + 1)) - sum{i_1^k}(i^2) + (1 + k) / 2 * k - 1 = 
    k * (k + 1) *(k + 2) / 2 - 1 - sum(i^2) =
    1/6 (n) (n + 1) (2n + 1)


"""
import unittest

def canBePlaced(n, k):
    if k * (k + 1) * (k + 2) // 2 <= n:
        return True

    for i in range(1, k + 1):
        # i ships * (k + 1 - i) size
        n -= i * (k + 1 - i) + i - (i == k)
        if n < 0:
            return False
    return True

def maxK(n):    
    l = 0
    r = n
    while l < r:
        mid = (l + r + 1) // 2
        if canBePlaced(n, mid):
            l = mid
        else:
            r = mid - 1
    
    return l

def main():
    n = int(input())
    print(maxK(n))


class TASK_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()