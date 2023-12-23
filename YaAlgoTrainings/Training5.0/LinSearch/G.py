"""
Description:
a - array of n positive numbers
divide into min number of segments
    so each number in the segment is >= its length

INPUT:
1.t - number of test cases 1000
2. t testcases:
    n - length of array <= 1e5. sum(ni) <= 2 1e5 
    a - n positive numbers 1 <= ai <= n
OUTPUT:
For each testcase
    k - number of segments
    len1 len2 ... lenk - length of segments

Solution:
Just divide from left to right

"""
import unittest

def segmentation(n, a):
    segmentMin = n + 1
    segLength = []
    for num in a:
        if not segLength or segmentMin < segLength[-1] + 1 or num < segLength[-1] + 1:
            segmentMin = num
            segLength.append(1)
        else:
            if num < segmentMin:
                segmentMin = num
            segLength[-1] += 1
    
    return segLength

def main():
    testCases = int(input())
    for _ in range(testCases):
        n = int(input())
        a = [int(x) for x in input().split()]
        segments = segmentation(n, a)
        print(len(segments))
        print(" ".join(str(x) for x in segments))

class G_Test(unittest.TestCase):
    def test_segmentation(self):
        n = 5
        a = [1, 3, 3, 3, 2]
        self.assertListEqual(segmentation(n, a), [1, 3, 1])

        n = 16
        a = [1, 9, 8, 7, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        self.assertListEqual(segmentation(n, a), [1, 6, 9])

        n = 7
        a = [7, 2, 3, 4, 3, 2, 7,]
        self.assertListEqual(segmentation(n, a), [2, 3, 2])

        n = 5
        a = [5, 5, 5, 5, 5]
        self.assertListEqual(segmentation(n, a), [5])

        n = 5
        a = [1, 2, 3, 4, 5]
        self.assertListEqual(segmentation(n, a), [1, 2, 2])

        n = 6
        a = [1, 1, 1, 1, 1, 1]
        self.assertListEqual(segmentation(n, a), [1, 1, 1, 1, 1, 1])

        n = 6
        a = [2, 2, 2, 2, 2, 2]
        self.assertListEqual(segmentation(n, a), [2, 2, 2])

        n = 10
        a = [5, 8, 1, 1, 1, 6, 3, 4, 7, 6]
        self.assertListEqual(segmentation(n, a), [2, 1, 1, 1, 3, 2])


if __name__ == "__main__":
    main()