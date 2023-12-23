#include "Tree.h"

#include <iostream>
#include <unordered_map>
#include <vector>

void getDeeps(const Tree<int>& tree, std::unordered_map<int, int>& deeps);
void getDeeps(const Tree<int>& tree, int nodeId, std::unordered_map<int, int>& deeps, int& deepLevel);


void getDeeps(const Tree<int>& tree, std::unordered_map<int, int>& deeps) {
    int deepLevel = 0;
    if (!tree.empty()) {
        getDeeps(tree, tree.getRootId(), deeps, deepLevel);
    }
}

void getDeeps(const Tree<int>& tree, int nodeId, std::unordered_map<int, int>& deeps, int& deepLevel) {
    deepLevel++;
    const TreeNode<int>& node = tree.getNode(nodeId);
    if (node.leftId != -1) {
        getDeeps(tree, node.leftId, deeps, deepLevel);
    }

    deeps[node.value] = deepLevel;

    if (node.rightId != -1) {
        getDeeps(tree, node.rightId, deeps, deepLevel);
    }

    deepLevel--;
}

int main() {
    std::vector<int> values;
    Tree<int> tree;
    int value;

    while (std::cin >> value && value != 0) {    
        if (tree.find(value) == -1) {
            values.push_back(value);
            tree.insert(value);
        }
    }

    std::unordered_map<int, int> deeps;
    getDeeps(tree, deeps);

    for (const auto& value : values) {
        std::cout << deeps[value] << " ";
    }
    return 0;
}