/*
Get an intersection of two sets.
*/

#include <iostream>
#include <unordered_set>
#include <set>

int main() {
    std::set<int> intersection;
    std::unordered_set<int> firstSet;

    while (std::cin.peek() != '\n') {
        int num;
        std::cin >> num;
        firstSet.insert(num);
    }
    std::cin.get();
    while (std::cin.peek() != '\n') {
        int num;
        std::cin >> num;
        if (firstSet.count(num)) {
            intersection.insert(num);
        }
    }

    for (const auto& num : intersection) {
        std::cout << num << ' ';
    }

    return 0;
}