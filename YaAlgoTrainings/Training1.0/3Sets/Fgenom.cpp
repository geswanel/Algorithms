/*
26 type of base A-Z
Genom - sequence of chars
Consider pairs

Vicinity of genom - number of pairs from the first genome which exist in the second

ABBACAB
BCABB
Answer 4 - AB BB CA AB
*/
#include <iostream>
#include <string>
#include <unordered_set>
#include <string_view>

int main() {
    std::string firstGenome;
    std::string secondGenome;
    std::cin >> firstGenome >> secondGenome;

    std::string_view fgView(firstGenome);
    std::string_view sgView(secondGenome);

    std::unordered_set<std::string_view> pairs;
    for (int i = 0; i < sgView.size() - 1; i++) {
        pairs.insert(std::string_view(sgView.begin() + i, 2));
    }

    int vicinity = 0;
    for (int i = 0; i < fgView.size() - 1; i++) {
        if (pairs.count(std::string_view(fgView.begin() + i, 2))) {
            vicinity++;
        }
    }

    std::cout << vicinity;
    return 0;
}