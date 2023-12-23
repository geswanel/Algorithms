
#include "../../utils/Heap.h"

#include <iostream>


int main() {
    Heap<int> heap;

    int totalCommands;
    std::cin >> totalCommands;
    for (int i = 0; i < totalCommands; i++) {
        int command;
        std::cin >> command;
        if (command == 0) {
            int value;
            std::cin >> value;
            heap.Insert(value);
        } else {
            std::cout << heap.Extract() << "\n";
        }
    }

    return 0;
}