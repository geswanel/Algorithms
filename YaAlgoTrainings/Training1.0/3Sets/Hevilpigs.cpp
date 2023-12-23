/*
Birds - points on a plane
One shoot kills first on the line of fire
Killed bird kills every bird below

Min number of shoots
*/
#include <iostream>
#include <unordered_set>

int main() {
    int N;
    std::cin >> N;

    std::unordered_set<int> birdsX;

    for (int i = 0; i < N; i++) {
        int x, y;
        std::cin >> x >> y;
        birdsX.insert(x);
    }

    std::cout << birdsX.size();
    return 0;
}