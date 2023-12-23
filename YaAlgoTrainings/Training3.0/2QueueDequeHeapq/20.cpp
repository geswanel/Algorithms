/*
Pyramid sort
*/
#include "../../utils/Heap.h"
#include <vector>
#include <iostream>


class LesserComparator {
    public:
    static bool compare(const int& v1, const int& v2) {
        return v1 < v2;
    }
};

int main() {
    Heap<int, LesserComparator> heap;
    int N;
    std::cin >> N;
    for (int i = 0; i < N; i++) {
        int value;
        std::cin >> value;
        heap.Insert(value);
    }

    std::vector<int> sortedVector;
    for (int i = 0; i < N; i++) {
        sortedVector.push_back(heap.Extract());
        std::cout << sortedVector[i] << ' ';
    }
    return 0;
}