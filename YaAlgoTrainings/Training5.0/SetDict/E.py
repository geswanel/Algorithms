"""
Description:
3 lists of numbers
find all numbers that exists at least in two of three lists
INPUT:
3 lists
    n - size
    list - sequence of numbers separated by space
OUTPUT
answer in ASC order
Solution:
unify pair intersections
"""
import unittest


def findExistedInTwo(a, b, c):
    ab = a & b
    ac = a & c
    bc = b & c
    return ab | bc | ac

def main():
    n = int(input())
    a = {int(x) for x in input().split()}
    m = int(input())
    b = {int(x) for x in input().split()}
    k = int(input())
    c = {int(x) for x in input().split()}
    print(" ".join(str(x) for x in sorted(findExistedInTwo(a, b, c))))


class E_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()