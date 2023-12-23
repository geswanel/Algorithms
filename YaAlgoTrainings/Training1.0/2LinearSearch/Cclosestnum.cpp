/*
Given a vector and a num
find the closest number in a vector to a num
If several => print any
*/

#include <iostream>
#include <algorithm>
#include <vector>


int closestNum(const std::vector<int>& v, int x) {
    int closest = v[0];
    int closestDiff = abs(v[0] - x);
    for (size_t i = 1; i < v.size(); ++i) {
        int diff = abs(v[i] - x);
        if (diff < closestDiff) {
            closest = v[i];
            closestDiff = diff;
        }
    }

    return closest;
}

int main() {
    int N;
    std::cin >> N;
    std::vector<int> v(N);
    for (auto& el : v) {
        std::cin >> el;
    }

    int x = 0;
    std::cin >> x;

    std::cout << closestNum(v, x);

    return 0;
}