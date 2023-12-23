from BinTree import TreeNode, createTree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:     # means that we have one descedant in left subtree and one in right
            return root
        return l or r   # either have 1 descedant or None

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     return self.lca(root, p, q)[0]

    # def lca(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
    #     """
    #         LCA for p and q. p and q are also considered as ancestors.
    #         DFS that returns tuple (p is descedant, q is descendant)
    #     """
    #     if root is None:
    #         return (None, False, False)
        
    #     left = self.lca(root.left, p, q)
    #     right = self.lca(root.right, p, q)

    #     hasP = root is p or left[1] or right[1]
    #     hasQ = root is q or left[2] or right[2]
    #     lca = None
    #     if hasP and hasQ:
    #         if left[0] is not None:
    #             lca = left[0]
    #         elif right[0] is not None:
    #             lca = right[0]
    #         else:
    #             lca = root
        
    #     return lca, hasP, hasQ

root = createTree([3,5,1,6,2,0,8,None,None,7,4])
p, q = 5, 1
print(Solution().lowestCommonAncestor(root, p, q))

root = createTree([3,5,1,6,2,0,8,None,None,7,4])
p, q = 5, 4
print(Solution().lowestCommonAncestor(root, p, q))

root = createTree([1, 2])
p, q = 1, 2
print(Solution().lowestCommonAncestor(root, p, q))


        
