#pragma once

#include "MemoryManager.h"
#include <iostream>

template<typename T>
using TreeNode = MemoryElement<T>;

template<typename T>
class Tree {
    public:
        Tree() : memory(0) {
            treeRootId = -1;
            size = 0;
        }

        Tree(int possibleSize) : memory(possibleSize) {
            treeRootId = -1;
            size = 0;
        }

        int find(const T& value) {
            return empty() ? -1 : find(treeRootId, value);
        }

        void insert(const T& value) {
            if (empty()) {
                treeRootId = memory.newElement();
                fillNewElement(treeRootId, value);
            } else {
                insert(treeRootId, value);
            }
        }

        int getRootId() const {
            return treeRootId;
        }

        const TreeNode<T>& getNode(int id) const {
            return memory.get(id);
        }

        bool empty() const {
            return treeRootId == -1;
        }

        int size() {
            return size;
        }

    private:
        MemoryManager<T> memory;
        int treeRootId;
        int size;

        void fillNewElement(const int elementId, const T& value) {
            TreeNode<T>& node = memory.get(elementId);
            node.value = value;
            node.leftId = -1;
            node.rightId = -1;
        }

        void insert(const int root, const T& value) {
            if (value < memory.get(root).value) {
                if (memory.get(root).leftId == -1) {
                    int newNodeId = memory.newElement();
                    fillNewElement(newNodeId, value);
                    memory.get(root).leftId = newNodeId;
                    size++;
                } else {
                    insert(memory.get(root).leftId, value);
                }
            } else if (value > memory.get(root).value) {
                if (memory.get(root).rightId == -1) {
                    int newNodeId = memory.newElement();
                    fillNewElement(newNodeId, value);
                    memory.get(root).rightId = newNodeId;
                    size++;
                } else {
                    insert(memory.get(root).rightId, value);
                }
            }
        }

        int find(const int rootId, const T& value) {
            const TreeNode<T>& node = memory.get(rootId);
            const T& key = node.value;

            if (key == value) {
                return rootId;
            }

            if (value < key) {
                if (node.leftId == -1) {
                    return -1;
                } else {
                    return find(node.leftId, value);
                }
            } else {
                if (node.rightId == -1) {
                    return -1;
                } else {
                    return find(node.rightId, value);
                }
            }
        }
};