"""
Description:
Sequence of measurements of some magnitude
Figure out if any number repeats so that there are less than k measurements between repeats.
INPUT:
n k
n numbers
OUTPUT
YES or NO
Solution
Sliding window with cntDict to check if were repeats
"""
import unittest


def isRepeated(n, k, a):
    numCnt = dict()
    # fill numCnt
    for i in range(min(n, k)):
        numCnt[a[i]] = numCnt.get(a[i], 0) + 1
        if numCnt[a[i]] == 2:
            return True
    
    for i in range(k, n):
        numCnt[a[i]] = numCnt.get(a[i], 0) + 1
        if numCnt[a[i]] == 2:
            return True
        numCnt[a[i - k]] -= 1
    
    return False

def main():
    n, k = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    print("YES" if isRepeated(n, k, a) else "NO")


class TASK_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()