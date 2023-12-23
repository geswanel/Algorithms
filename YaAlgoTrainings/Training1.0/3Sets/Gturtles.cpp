/*
N turtles one after another
Each turtle says how many ahead and behind

How many turtles speak truth
*/

#include <iostream>
#include <unordered_set>

int main() {
    int N;
    std::cin >> N;

    std::unordered_set<int> truth;
    for (int i = 0; i < N; i++) {
        int ai, bi;
        std::cin >> ai >> bi;
        if (ai >= 0 && bi >= 0 && ai + bi + 1 == N && truth.count(ai) == 0) {
            truth.insert(ai);
        }
    }

    std::cout << truth.size();

    return 0;
}