/*
How many local maxes
*/
#include <iostream>
#include <vector>


int localMaxCnt(const std::vector<int>& v) {
    int cnt = 0;
    for (size_t i = 1; i + 1 < v.size(); ++i) {
        if (v[i - 1] < v[i] && v[i] > v[i + 1]) {
            ++cnt;
        }
    }

    return cnt;
}

int main() {
    std::vector<int> nums;
    int num = 0;
    while (std::cin >> num) {
        nums.push_back(num);
    }

    std::cout << localMaxCnt(nums);

    return 0;
}
