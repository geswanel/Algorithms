/*
Given set of digits and a value
Find out how many digits needed to be able to write the value.
*/

#include <unordered_set>
#include <iostream>


int main() {
    std::unordered_set<int> keys;
    int x, y, z;
    std::cin >> x >> y >> z;
    keys.insert({x, y, z});

    int N;
    std::cin >> N;
    std::unordered_set<int> digitsDiff;
    while (N > 0) {
        int digit = N % 10;
        if (!keys.count(digit)) {
            digitsDiff.insert(digit);
        }

        N /= 10;
    }

    std::cout << digitsDiff.size();
    return 0;
}