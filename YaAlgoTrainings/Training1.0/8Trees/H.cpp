#include "Tree.h"

#include <iostream>
#include <algorithm>


struct AvlCheck {
    int maxDeep;
    bool isAVL;
};

// template<typename T>
// void debug(T value, AvlCheck leftAvlCheck, AvlCheck curAvlCheck, AvlCheck rightAvlCheck) {
//     std::cout << "Cur element = " << value 
//         << ";\n left = {" << leftAvlCheck.maxDeep << ", " << (leftAvlCheck.isAVL ? "AVL" : "NOT AVL")
//         << "}\n right = {" << rightAvlCheck.maxDeep << ", " << (rightAvlCheck.isAVL ? "AVL" : "NOT AVL")
//         << "}\n cur = {" << curAvlCheck.maxDeep << ", " << (curAvlCheck.isAVL ? "AVL" : "NOT AVL") << "}\n";    
// }

template <typename T>
AvlCheck isAVLTree(const Tree<T>& tree, const int nodeId) {
    const TreeNode<T>& node = tree.getNode(nodeId);
    
    AvlCheck leftAvlCheck = (node.leftId == -1) ? AvlCheck{0, true} : isAVLTree(tree, node.leftId);
    AvlCheck rightAvlCheck = (node.rightId == -1) ? AvlCheck{0, true} : isAVLTree(tree, node.rightId);

    AvlCheck curAvlCheck = AvlCheck{std::max(leftAvlCheck.maxDeep, rightAvlCheck.maxDeep) + 1,
            std::abs(leftAvlCheck.maxDeep - rightAvlCheck.maxDeep) <= 1 && leftAvlCheck.isAVL && rightAvlCheck.isAVL};

    //debug(node.value, leftAvlCheck, curAvlCheck, rightAvlCheck);
    return curAvlCheck;
}

template <typename T>
bool isAVLTree(const Tree<T>& tree) {
    if (tree.empty()) {
        return true;
    }

    return (isAVLTree<int>(tree, tree.getRootId())).isAVL;
}


int main() {
    Tree<int> tree;

    int value;
    while(std::cin >> value && value != 0) {
        tree.insert(value);
    }

    std::cout << (isAVLTree(tree) ? "YES" : "NO");

    return 0;
}