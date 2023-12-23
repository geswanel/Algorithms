/*
We need to find the second largest element.

Where can the second largest element be found?

The maximum element is located in the rightmost child.

- If the child has no children, then its parent is the next largest
- If it has children, only to the left of it. Then the next largest is the rightmost in the left subtree
- If there is no right subtree at all, then also, the rightmost element in the left subtree of the root.
*/


#include "Tree.h"

#include <iostream>


int secondStatistic(const Tree<int>& tree) {
    const TreeNode<int>* nodePtr = &(tree.getNode(tree.getRootId()));

    if (nodePtr->rightId != -1) {
        const TreeNode<int>* parentPtr = nullptr;
        while (nodePtr->rightId != -1) {
            parentPtr = nodePtr;
            nodePtr = &(tree.getNode(nodePtr->rightId));
        }

        if (nodePtr->leftId == -1) {
            return parentPtr->value;
        } else {
            nodePtr = &(tree.getNode(nodePtr->leftId));
            while(nodePtr->rightId != -1) {
                nodePtr = &(tree.getNode(nodePtr->rightId));
            }

            return nodePtr->value;
        }
    } else {
        nodePtr = &(tree.getNode(nodePtr->leftId));
        while(nodePtr->rightId != -1) {
            nodePtr = &(tree.getNode(nodePtr->rightId));
        }
        return nodePtr->value;
    }
}

int main() {

    Tree<int> tree;
    int value;
    while (std::cin >> value && value != 0) {
        tree.insert(value);
    }

    std::cout << secondStatistic(tree);
    return 0;
}