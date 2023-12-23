#include "../../utils/Queue.h"
#include <iostream>



int main() {
    std::string command;

    Queue<int> queue;
    do {
        std::cin >> command;
        if (command == "push") {
            int value;
            std::cin >> value;
            queue.push(value);
            std::cout << "ok" << '\n';
        } else if (command == "pop" || command == "front") {
            try {
                std::cout << queue.front() << '\n';
                if (command == "pop") {
                    queue.pop();
                }
            } catch (empty_error e) {
                std::cout << "error" << '\n';
            }
        } else if (command == "size") {
            std::cout << queue.size() << '\n';
        } else if (command == "clear") {
            queue.clear();
            std::cout << "ok" << '\n';
        } else if (command == "exit") {
            std::cout << "bye" << '\n';
        }
    } while (command != "exit");

    return 0;
}

