/*
Given nums

Find min amount of numbers to make nums symmetric
*/

#include <iostream>
#include <vector>


int countToMakeSym(const std::vector<int>& v) {
    int symSize = 0;
    size_t revInd = v.size() - 1;
    for (size_t i = 0; i < v.size(); ++i) {
        if (v[i] == v[revInd]) {
            symSize++;
            revInd--;
        } else {
            symSize = 0;
            revInd = v.size() - 1;
        }
    }

    return v.size() - symSize;
}

int main() {
    int N = 0;
    std::cin >> N;
    std::vector<int> v(N);
    for (auto& el : v) {
        std::cin >> el;
    }

    int symCnt = countToMakeSym(v);
    std::cout << symCnt << "\n";
    bool first = true;
    for (int i = symCnt - 1; i >= 0; --i) {
        if (!first) {
            std::cout << " ";
        }
        std::cout << v[i];
        first = false;
    }
    return 0;
}