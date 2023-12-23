import unittest

def coloredTrees(P, V, Q, M):
    fSegment = (P - V, P + V)
    sSegment = (Q - M, Q + M)
    if P + V < Q - M or Q + M < P - V:  # no intersection
        return 2 * (V + M + 1)
    else:
        return max(P + V, Q + M) - min(P - V, Q - M) + 1

def main():
    P, V = [int(x) for x in input().split()]
    Q, M = [int(x) for x in input().split()]
    print(coloredTrees(P, V, Q, M))


class ATest(unittest.TestCase):
    def testColoredTreesNoIntersection(self):
        P, V = 0, 5
        Q, M = 12, 5
        ans = 22
        self.assertEqual(coloredTrees(P, V, Q, M), ans)

        P, V = 12, 5
        Q, M = 0, 5
        ans = 22
        self.assertEqual(coloredTrees(P, V, Q, M), ans)
    
    def testColoredTreesSideIntersection(self):
        P, V = 0, 5
        Q, M = 7, 5
        ans = 18
        self.assertEqual(coloredTrees(P, V, Q, M), ans)

        P, V = 7, 5
        Q, M = 0, 5
        ans = 18
        self.assertEqual(coloredTrees(P, V, Q, M), ans)
    
    def testColoredTreesInnerIntersection(self):
        P, V = 0, 10
        Q, M = 0, 5
        ans = 21
        self.assertEqual(coloredTrees(P, V, Q, M), ans)

        P, V = 0, 5
        Q, M = 0, 10
        ans = 21
        self.assertEqual(coloredTrees(P, V, Q, M), ans)


if __name__ == "__main__":
    #unittest.main()
    main()