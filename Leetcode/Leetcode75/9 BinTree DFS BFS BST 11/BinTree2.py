class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(values: list) -> TreeNode:
    # create tree from list where i is parent 2i + 1 and 2i+2 are children
    if len(values) == 0:
        return
    elif values[0] == None:
        raise ValueError("The root is None in passed list!")
    
    tree = [None for _ in range(len(values))]
    for i in range(len(values)):
        if tree[i] is None:
            tree[i] = TreeNode(val=values[i])
        
        if 2 * i + 1 < len(values) and values[2 * i + 1] is not None:
            tree[2 * i + 1] = TreeNode(val=values[2 * i + 1])
            tree[i].left = tree[2 * i + 1]
        
        if 2 * i + 2 < len(values) and values[2 * i + 2] is not None:
            tree[2 * i + 2] = TreeNode(val=values[2 * i + 2])
            tree[i].right = tree[2 * i + 2]
    
    return tree[0]


# DFS - recursive to max depth

from enum import Enum

class SolutionDFS:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    def leafSequence(self, root: TreeNode) -> list:
        left_seq = []
        if root.left is not None:
            left_seq = self.leafSequence(root.left)

        cur_seq = []
        if root.left is None and root.right is None:
            cur_seq = [root.val]

        right_seq = []
        if root.right is not None:
            right_seq = self.leafSequence(root.right)
        
        return left_seq + cur_seq + right_seq

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leafSequence(root1) == self.leafSequence(root2)
    
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        stack = [(root, root.val)]  # save node and maxVal til node included node
        ans = 0
        while stack:
            node, maxVal = stack.pop()
            if node.val >= maxVal:
                ans += 1
            
            if node.right is not None:
                stack.append((node.right, max(node.right.val, maxVal)))

            if node.left is not None:
                stack.append((node.left, max(node.left.val, maxVal)))
        
        return ans
    
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        Idea dfs through nodes with prefix sum => check for current sum
        difference with all previous sums to get target sum
        N^2 (N ~ 1000)

        Another ideas:
        1. idea of passing targetSum - node.val! still O(N^2)
        2. The same as mine but we can save dict {prevSum: cnt} and not for N but for O(1)
            figure out how many paths to current node is targetted.
        """
        if root is None:
            return 0
        def dfs(root: TreeNode, prevSums: list):
            count = 0
            prevSums.append(prevSums[-1] + root.val)
            for i in range(len(prevSums) - 1):
                if (prevSums[-1] - prevSums[i]) == targetSum:
                    count += 1
            if root.left is not None:
                count += dfs(root.left, prevSums)
            
            if root.right is not None:
                count += dfs(root.right, prevSums)
            
            prevSums.pop()

            return count
        
        return dfs(root, [0])
    
    def longestZigZag(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root: TreeNode, dir: str, zlen: int = 0):
            nonlocal ans
            if root is None:
                return
            
            if dir == 'l':
                dfs(root.left, 'r', zlen + 1)
                dfs(root.right, 'l', 1)
            else:
                dfs(root.right, 'l', zlen + 1)
                dfs(root.left, 'r', 1)
            
            if zlen > ans:
                ans = zlen

        
        if root is None:
            return 0
        
        dfs(root.left, 'r', 1)
        dfs(root.right, 'l', 1)
        
        return ans


            


class TestDFS:
    def assertEqual(self, lhs, rhs):
        return lhs == rhs
    
    def test_leafSequence(self):
        sol = SolutionDFS()
        root = create_tree([1, 2, 3])
        seq = sol.leafSequence(root)
        print(self.assertEqual(seq, [2, 3]), seq)

        root = create_tree([1, 3, 2])
        seq = sol.leafSequence(root)
        print(self.assertEqual(seq, [3, 2]), seq)

        root = create_tree([3,5,1,6,2,9,8,None,None,7,4])
        seq = sol.leafSequence(root)
        print(self.assertEqual(seq, [6, 7, 4, 9, 8]), seq)
    
    def test_leafSimilar(self):
        sol = SolutionDFS()
        root1 = create_tree([3,5,1,6,2,9,8,None,None,7,4])
        root2 = create_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
        print(self.assertEqual(sol.leafSimilar(root1, root2), True))

        root1 = create_tree([1,2,3])
        root2 = create_tree([1,3,2])
        print(self.assertEqual(sol.leafSimilar(root1, root2), True))

    def test_maxDepth(self):
        sol = SolutionDFS()
        root = create_tree([3, 9, 20, None, None, 15, 7])
        print(self.assertEqual(sol.maxDepth(root), 3))
        root = create_tree([1, None, 2])
        print(self.assertEqual(sol.maxDepth(root), 2))
        root = create_tree([])
        print(self.assertEqual(sol.maxDepth(root), 0))
        root = create_tree([1])
        print(self.assertEqual(sol.maxDepth(root), 1))
    
    sol = SolutionDFS()
    def testGoodNodes(self):
        root = create_tree([3,1,4,3,None,1,5])
        self.assertEqual(self.sol.goodNodes(root), 4)

        root = create_tree([3,3,None,4,2])
        self.assertEqual(self.sol.goodNodes(root), 3)

        root = create_tree([1])
        self.assertEqual(self.sol.goodNodes(root), 1)
        

# BFS - level by level using queue
from collections import deque

class SolutionBFS:
    def rightSideView(self, root: TreeNode) -> list[int]:
        """
            In the beginning was thinking why can't we just go to most right child
            But it won't help at all, because deepness of left subtree may be much bigger.
            So I need to use BFS algorithms
        """
        ans = []
        if root is None:
            return ans
        
        q = deque()
        q.append(root)
        cur_level = 1
        while cur_level != 0:
            next_level = 0
            while cur_level > 0:
                cur_level -= 1
                node: TreeNode = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                    next_level += 1
                if node.right is not None:
                    q.append(node.right)
                    next_level += 1
                if cur_level == 0:
                    ans.append(node.val)
            cur_level = next_level
        
        return ans
    
    def maxLevelSum(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        max_level = 1
        on_level = 1
        max_val = root.val
        lvl = 1
        while len(q) != 0:
            on_cur_level = 0
            cur_max = 0
            while on_level > 0:
                on_level -= 1
                node: TreeNode = q.popleft()
                cur_max += node.val
                if node.left is not None:
                    q.append(node.left)
                    on_cur_level += 1
                if node.right is not None:
                    q.append(node.right)
                    on_cur_level += 1 
            if cur_max > max_val:
                max_val = cur_max
                max_level = lvl
            on_level = on_cur_level
            lvl += 1
        
        return max_level


class TestBFS:
    def assertEqual(self, lhs, rhs):
        return lhs == rhs

    def test_rightSideView(self):
        sol = SolutionBFS()
        root = create_tree([1,2,3,None,5,None,4])
        print(self.assertEqual(sol.rightSideView(root), [1, 3, 4]))
        
        root = create_tree([1, None, 3])
        print(self.assertEqual(sol.rightSideView(root), [1, 3]))

        root = create_tree([])
        print(self.assertEqual(sol.rightSideView(root), []))

        root = create_tree([1,2,3,None,5,None,4,None, None, 3, 4])
        print(self.assertEqual(sol.rightSideView(root), [1, 3, 4, 4]))
    
    def test_maxLevelSum(self):
        sol = SolutionBFS()
        root = create_tree([1,7,0,7,-8,None,None])
        print(self.assertEqual(sol.maxLevelSum(root), 2))
        
        root = create_tree([989,None,10250,98693,-89388,None,None,None,-32127])
        print(self.assertEqual(sol.maxLevelSum(root), 2))


def put_into_binsearch_tree(root: TreeNode, val):
    """
        Puts element into BST and return True, parent_node if succeed
        and False, val_node otherwise, where val_node is node with passed value
    """
    cur_node = root
    while True:
        if val < cur_node.val:
            if cur_node.left is None:
                cur_node.left = TreeNode(val)
                return True, cur_node
            else:
                cur_node = cur_node.left
        elif val > cur_node.val:
            if cur_node.right is None:
                cur_node.right = TreeNode(val)
                return True, cur_node
            else:
                cur_node = cur_node.right
        else:
            return False, cur_node


def create_binsearch_tree(values: list):
    if len(values) == 0:
        return None
    
    root = TreeNode(val=values[0])
    for i in range(1, len(values)):
        put_into_binsearch_tree(root, val=values[i])


class SolutionBST:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        notExist, node = put_into_binsearch_tree(root, val)
        if not notExist:
            return node
        else:
            if node.left is not None and node.left.val == val:
                node.left = None
            elif node.right is not None and node.right.val == val:
                node.right = None
            return None
        



root = create_tree([1,None,1,None, None,1,1,1,1,None,1,None,None,None,1])
print(SolutionDFS().longestZigZag(root))

root = create_tree([1,1,1,None,1,None,None,1,1,None,1])
print(SolutionDFS().longestZigZag(root))

root = create_tree([1])
print(SolutionDFS().longestZigZag(root))