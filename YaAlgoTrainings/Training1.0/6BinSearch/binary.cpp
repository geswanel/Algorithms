/*
Implementation of binary search in an array.

Numbers N and K
Next N elements of the first array
K elements of the second array

For each number from K, output whether it exists in the first array "YES" / "NO"
*/

#include "binary.h"
#include <vector>
#include <iostream>

bool checkCondition(const int& val, const int& checkVal) {
    return val <= checkVal;
}

int main() {
    int N, K;
    std::cin >> N >> K;
    std::vector<int> elements(N);
    for (int i = 0; i < N; i++) {
        std::cin >> elements[i];
    }
    
    std::vector<int> forSearch(K);
    for (int i = 0; i < K; i++) {
        std::cin >> forSearch[i];
    }

    for (int i = 0; i < K; i++) {
        int id = lBinSearch(elements, forSearch[i], checkCondition);
        if (id == N || elements[id] != forSearch[i]) {
            std::cout << "NO" << '\n';
        } else {
            std::cout << "YES" << '\n';
        }
    }
    return 0;
}