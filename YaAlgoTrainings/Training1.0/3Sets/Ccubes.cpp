/*
Coloured cubes
2 sets
In a set every cube with unique colour
Intersection of sets
*/
#include <unordered_set>
#include <set>
#include <iostream>

int main() {
    std::set<int> intersection;
    std::set<int> remainB;
    std::unordered_set<int> cubesA;

    int N, M;
    std::cin >> N >> M;
    for (int i = 0; i < N; i++) {  //O(N)
        int cube;
        std::cin >> cube;
        cubesA.insert(cube);
    }

    for (int i = 0; i < M; i++) {   // ~ M log M 
        int cube;
        std::cin >> cube;
        if (cubesA.count(cube)) {   // O(1) search
            intersection.insert(cube);
            cubesA.erase(cube);
        } else {
            remainB.insert(cube);
        }
    }

    std::set<int> remainA(cubesA.begin(), cubesA.end());  //sorting

    std::cout << intersection.size() << '\n';
    for (const auto& cube : intersection) {
        std::cout << cube << ' ';
    }

    std::cout << '\n' << remainA.size() << '\n';
    for (const auto& cube : remainA) {
        std::cout << cube << ' ';
    }

    std::cout << '\n' << remainB.size() << '\n';
    for (const auto& cube : remainB) {
        std::cout << cube << ' ';
    }

    return 0;
}