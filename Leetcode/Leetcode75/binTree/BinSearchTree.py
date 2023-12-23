from BinTree import TreeNode


def pushBST(root: TreeNode, val) -> TreeNode:
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = pushBST(root.left, val)
    elif val > root.val:
        root.right = pushBST(root.right, val)
    
    return root

def eraseRoot(root: TreeNode):
    l = root.left
    r = root.right
    if l is None or r is None:
        root.left = root.right = None
        return l or r
    else:
        maxL = root.left
        maxLParent = root
        while maxL.right is not None:
            maxLParent = maxL
            maxL = maxL.right
        if maxLParent is not root:
            maxLParent.right = maxL.left
            maxL.left = root.left
        maxL.right = root.right
        root.left = root.right = None

        return maxL

def eraseBST(root: TreeNode, val):
    """
    Erasing value in treeNode we can just change value from min in right subtree or max in left subtree
    """
    if root is None:
        return root
    
    if val < root.val:
        root.left = eraseBST(root.left, val)
    elif val > root.val:
        root.right = eraseBST(root.right, val)
    else:
        return eraseRoot(root)

    return root




def createBST(values: list):
    if len(values) == 0:
        return None
    
    root = TreeNode(values[0])
    for i in range(1, len(values)):
        pushBST(root, values[i])
    
    return root


def searchBST(root: TreeNode, val) -> TreeNode:
    if root is None or root.val == val:
        return root

    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)