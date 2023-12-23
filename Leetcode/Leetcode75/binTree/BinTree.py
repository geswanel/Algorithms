class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self.val)


def createTree(values: list):
    n = len(values)
    if n == 0:
        return

    root = TreeNode(values[0])
    lvl = [root]
    valId = 1
    while valId < n:
        nextLvl = []
        for node in lvl:
            if valId < n and values[valId] is not None:
                node.left = TreeNode(values[valId])
                nextLvl.append(node.left)
            valId += 1
            if valId < n and values[valId] is not None:
                node.right = TreeNode(values[valId])
                nextLvl.append(node.right)
            valId += 1
        
        lvl.clear()
        lvl = nextLvl
    
    return root

def visualizeTree(root: TreeNode):
    print("PRINTNG TREE")
    lvl = [root]
    output = []
    isNotNone = True
    while isNotNone:
        isNotNone = False
        nextLvl = []
        lvlOutput = []
        for node in lvl:
            if node is None:
                nextLvl += [None, None]
            else:
                nextLvl += [node.left, node.right]
                isNotNone = node.left is not None or node.right is not None
            
            lvlOutput.append('*' if node is None else node.val)
        
        output.append(lvlOutput)
        lvl.clear()
        lvl = nextLvl

    for lvlNum, lvlOutput  in enumerate(output):
        delimeter = " " * 2 ** (len(output) - lvlNum - 1)
        print(delimeter, delimeter.join(str(x) for x in lvlOutput))
    
    print("END PRINTING TREE")

def DFSRecursy(root: TreeNode):
    if root is None:
        return float('-inf')
    #inorder
    maxLeftVal = DFSRecursy(root.left)
    maxVal = root.val
    maxRightVal = DFSRecursy(root.right)

    return max(maxLeftVal, maxVal, maxRightVal)

def DFSStack(root: TreeNode):
    if root is None:
        return None
    
    st = [root]

    maxVal = root.val
    while len(st) > 0:
        node = st.pop()
        if node.val > maxVal:
            maxVal = node.val
        
        if node.right is not None:
            st.append(node.right)
        
        if node.left is not None:
            st.append(node.left)
    
    return maxVal
        


if __name__ == "__main__":
    root = createTree([])
    visualizeTree(root)
    print(DFSRecursy(root), DFSStack(root))

    root = createTree([1, 2, 3])
    visualizeTree(root)
    print(DFSRecursy(root), DFSStack(root))

    root = createTree([1,None,2,3])
    visualizeTree(root)
    print(DFSRecursy(root), DFSStack(root))

    root = createTree([5,4,7,3,None,2,None,1,None,9])
    visualizeTree(root)
    print(DFSRecursy(root), DFSStack(root))
