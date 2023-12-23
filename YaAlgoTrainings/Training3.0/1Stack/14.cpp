/*
There is a train with numbered cars

In a dead end, you can drive in several cars along one path and exit along another

Is it possible to arrange it so that all the exited cars go in order in the end?

Solution: Keep track of the car number in the correct order that has not yet exited
Put cars into the dead end until we encounter the one that should exit
Then, release them as long as they go in order
and repeat this operation
*/

#include "../../utils/Stack.h"

#include <iostream>
#include <vector>

bool isRightOrderPossible(const std::vector<int>& carriages) {
    Stack<int> deadEnd;

    int nextRightOrder = 1;
    for (int i = 0; i < carriages.size(); i++) {
        deadEnd.push(carriages[i]);
        while (deadEnd.size() > 0 && deadEnd.back() == nextRightOrder) {
            deadEnd.pop();
            nextRightOrder++;
        }
    }

    return deadEnd.size() == 0;
}

int main() {
    int N;
    std::cin >> N;
    std::vector<int> carriages(N);
    for (int i = 0; i < N; i++) {
        std::cin >> carriages[i];
    }

    std::cout << (isRightOrderPossible(carriages) ? "YES" : "NO");

    return 0;
}