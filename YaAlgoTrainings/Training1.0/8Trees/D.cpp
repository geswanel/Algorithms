#include "Tree.h"

#include <iostream>


template<typename T>
void printTree(std::ostream& out, const Tree<T>& tree, const int& nodeId, const char delim) {
    const TreeNode<T>& node = tree.getNode(nodeId);

    if (node.leftId != -1) {
        printTree(out, tree, node.leftId, delim);
    }

    out << node.value << delim;

    if (node.rightId != -1) {
        printTree(out, tree, node.rightId, delim);
    }
}

template<typename T>
void printTree(std::ostream& out, const Tree<T>& tree, const char delim = ' ') {
    if (!tree.empty()) {
        printTree(out, tree, tree.getRootId(), delim);
    }
}

int main() {
    Tree<int> tree;

    int value;
    while(std::cin >> value && value != 0) {
        tree.insert(value);
    }

    printTree(std::cout, tree, '\n');

    return 0;
}