"""
Description:
array a of n numbers
Find the min amount of numbers to delete so
ai - aj <= 1 for any i and j
INPUT:
n
a
OUTPUT
min deletions

Solution:
count dict
sort by keys and check max cnt of neighbour values (diff <= 1)
"""
import unittest

def minDeletion(a, n):
    numCnt = dict()
    for num in a:
        numCnt[num] = numCnt.get(num, 0) + 1
    
    maxCnt = max(numCnt.values())
    prevKey = None
    for key in sorted(numCnt.keys()):
        if prevKey is not None and key - prevKey <= 1 and numCnt[key] + numCnt[prevKey] > maxCnt:
            maxCnt = numCnt[key] + numCnt[prevKey]
        prevKey = key
    
    return n - maxCnt

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(minDeletion(a, n))


class C_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()