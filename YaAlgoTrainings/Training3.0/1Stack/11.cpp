#include "../../utils/Stack.h"

#include <iostream>

int main() {
    std::string command;

    Stack<int> stack;
    do {
        std::cin >> command;
        if (command == "push") {
            int value;
            std::cin >> value;
            stack.push(value);
            std::cout << "ok" << '\n';
        } else if (command == "pop" || command == "back") {
            try {
                std::cout << stack.back() << '\n';
                if (command == "pop") {
                    stack.pop();
                }
            } catch (EmptyException e) {
                std::cout << "error" << '\n';
            }
        } else if (command == "size") {
            std::cout << stack.size() << '\n';
        } else if (command == "clear") {
            stack.clear();
            std::cout << "ok" << '\n';
        } else if (command == "exit") {
            std::cout << "bye" << '\n';
        }
    } while (command != "exit");

    return 0;
}