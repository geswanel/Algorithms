#include "Tree.h"


#include <iostream>

int heightOfTree(const Tree<int>& tree);
void heightOfTree(const Tree<int>& tree, const int nodeId, int& curHeight, int& maxHeight);

int heightOfTree(const Tree<int>& tree) {
    if (tree.empty()) {
        return 0;
    }
    int maxHeight = 0;
    int curHeight = 0;
    heightOfTree(tree, tree.getRootId(), curHeight, maxHeight);
    return maxHeight;
}

void heightOfTree(const Tree<int>& tree, const int nodeId, int& curHeight, int& maxHeight) {
    curHeight++;
    const TreeNode<int>& node = tree.getNode(nodeId);
    if (node.leftId == -1 && node.rightId == -1 && curHeight > maxHeight) {
        maxHeight = curHeight;
    } else {
        if (node.leftId != -1) {
            heightOfTree(tree, node.leftId, curHeight, maxHeight);
        }

        if (node.rightId != -1) {
            heightOfTree(tree, node.rightId, curHeight, maxHeight);
        }
    }

    curHeight--;
}


int main() {
    Tree<int> tree(2);

    int value;
    while (std::cin >> value && value != 0) {
        tree.insert(value);
    }

    std::cout << heightOfTree(tree) << "\n";
    tree.printTree(std::cout);
    return 0;
}