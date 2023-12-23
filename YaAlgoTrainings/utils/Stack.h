#pragma once

#include <vector>
#include <string>

class EmptyException : public std::exception {
    std::string what() {
        return "Stack is empty!";
    }
};

template <typename T>
class Stack {
    public:
        void push(const T& el) {
            data.push_back(el);
        }

        void pop() {
            if (data.empty()) {
                throw EmptyException();
            }
            data.pop_back();
        }

        T back() const {
            if (data.empty()) {
                throw EmptyException();
            }
            return data.back();
        }

        int size() const {
            return data.size();
        }

        void clear() {
            data.clear();
        }


    private:
        std::vector<T> data;
};