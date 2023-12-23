#pragma once

#include <vector>

/**
 * @brief exception type that thrown when there is attempt to get element from empty structure.
 * 
 */
class empty_error : public std::exception {
    const char* what() {
        return "There is no elements in structure";
    }
};

template<typename T>
class GreaterComparator {
    public:
    static bool compare(const T& value1, const T& value2) {
        return value1 > value2;
    }
};

/**
 * @brief Heap structure based on vector.
 * 
 * Heap is priority queue - binary tree that filled layer by layer and have some properties (Each node has children with less priority)
 * 
 * Element with index i has children in index 2i + 1 and 2i + 2
 * Element with index i has parent (i - 1) / 2
 * @tparam T type of values stored
 * @tparam Compar comparator for priorities
 */
template<class T, class PriorityComparator = GreaterComparator<T>>
class Heap {
public:
    void Insert(const T& value) {
        std::size_t pos = data.size();
        data.push_back(value);
        while (pos > 0) {
            std::size_t parentPos = (pos - 1) / 2;
            if (PriorityComparator::compare(value, data[parentPos])) {
                swap(pos, parentPos);
                pos = parentPos;
            } else {
                break;
            }
        }
    }

    T Extract() {
        if (data.size() == 0) {
            throw empty_error();
        }
        T ans = data[0];
        data[0] = data.back();
        data.pop_back();
        std::size_t pos = 0;
        while (pos * 2 + 2 < data.size()) {
            std::size_t maxPosId = pos * 2 + 1; //left Child
            if (PriorityComparator::compare(data[maxPosId + 1], data[maxPosId])) {
                maxPosId++;
            }
            if (PriorityComparator::compare(data[maxPosId], data[pos])) {
                swap(maxPosId, pos);
                pos = maxPosId;
            } else {
                break;
            }
        }

        if (pos * 2 + 1 < data.size() && PriorityComparator::compare(data[pos * 2 + 1], data[pos])) {
            swap(pos * 2 + 1, pos);
            pos = pos * 2 + 1;
        }
        return ans;
    }

private:
    std::vector<T> data;

    void swap(const std::size_t& id1, const std::size_t& id2) {
        T tmp = data[id1];
        data[id1] = data[id2];
        data[id2] = tmp;
    }
};