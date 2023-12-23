/*
Given nums

1. Needed number ending with 5
2. The largest number before needed
3. Next number is less than needed

min position of needed number in descending nums
*/

#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>


size_t findMaxId(const std::vector<int>& v) {
    int maxNum = v[0];
    size_t maxId = 0;
    for (size_t i = 1; i < v.size(); ++i) {
        if (v[i] > maxNum) {
            maxNum = v[i];
            maxId = i;
        }
    }

    return maxId;
}

int findMaxNeeded(const std::vector<int>& v, const size_t startPos) {
    int maxNeeded = std::numeric_limits<int>::min();
    for (size_t i = startPos; i + 1 < v.size(); ++i) {
        if (v[i] % 10 == 5 && v[i] > v[i + 1] && v[i] > maxNeeded) {
            maxNeeded = v[i];
        }
    }

    return maxNeeded;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> v(n);
    for (auto& el : v) {
        std::cin >> el;
    }

    size_t maxId = findMaxId(v);
    int maxNeeded = findMaxNeeded(v, maxId + 1);
    size_t bigger = std::count_if(v.begin(), v.end(), 
        [maxNeeded](const int& num) { return num > maxNeeded; }
    );

    std::cout << (bigger == v.size() ? 0 : bigger + 1);

    return 0;
}