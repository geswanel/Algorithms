#include "../../utils/Deque.h"

#include <iostream>


int main() {
    std::string command;

    Deque<int> deque;
    do {
        std::cin >> command;
        if (command == "push_front") {
            int value;
            std::cin >> value;
            deque.push_front(value);
            std::cout << "ok" << '\n';
        } else if (command == "push_back") {
            int value;
            std::cin >> value;
            deque.push_back(value);
            std::cout << "ok" << '\n';
        } else if (command == "pop_front" || command == "front") {
            try {
                std::cout << deque.front() << '\n';
                if (command == "pop_front") {
                    deque.pop_front();
                }
            } catch (empty_error e) {
                std::cout << "error" << '\n';
            }
        } else if (command == "pop_back" || command == "back") {
            try {
                std::cout << deque.back() << '\n';
                if (command == "pop_back") {
                    deque.pop_back();
                }
            } catch (empty_error e) {
                std::cout << "error" << '\n';
            }
        } else if (command == "size") {
            std::cout << deque.size() << '\n';
        } else if (command == "clear") {
            deque.clear();
            std::cout << "ok" << '\n';
        } else if (command == "exit") {
            std::cout << "bye" << '\n';
        }
    } while (command != "exit");

    return 0;
}