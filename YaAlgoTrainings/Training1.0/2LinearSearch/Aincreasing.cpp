/*
Check if a vector is monotonically increasing.
*/

#include <iostream>
#include <vector>

bool isIncreasing(const std::vector<int>& v) {
    for (size_t i = 1; i < v.size(); ++i) {
        if (v[i - 1] >= v[i]) {
            return false;
        }
    }

    return true;
}

int main() {
    std::vector<int> v;
    int num = 0;
    while (std::cin >> num) {
        v.push_back(num);
    }

    std::cout << (isIncreasing(v) ? "YES" : "NO");
    
    return 0;
}