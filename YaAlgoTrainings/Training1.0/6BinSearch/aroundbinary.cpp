/*
For each number in the sequence, find the closest one to it in the array

Perform left and right search to return the first one that is >= and the first one that is <= 

If they coincide, then the same number is present
If they do not coincide, then check which index is closer

The elements in the array are sorted in non-decreasing order
*/

#include "binary.h"
#include <iostream>
#include <vector>


bool checkLeftCondition(const int& value, const int& element) {
    return element >= value;  
}

bool checkRightCondition(const int& value, const int& element) {
    return element <= value;    
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
        int idLeft = lBinSearch(elements, forSearch[i], checkLeftCondition);
        int idRight = rBinSearch(elements, forSearch[i], checkRightCondition);
        if (idLeft == N) {  
            std::cout << elements[idRight] << '\n';
        } else if (idRight == -1) {
            std::cout << elements[idLeft] << '\n';
        } else {
            if (std::abs(elements[idRight] - forSearch[i]) <= std::abs(elements[idLeft] - forSearch[i])) {
                std::cout << elements[idRight] << '\n';
            } else {
                std::cout << elements[idLeft] << '\n';
            }
        }
    }

    return 0;
}