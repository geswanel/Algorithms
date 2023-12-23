#pragma once

#include <vector>

/**
 * @brief exception type that thrown when there is attempt to get element from empty structure.
 * 
 */
class empty_error : public std::exception {
    const char* what() {
        return "There is no elements in structure";
    }
};


/**
 * @brief Simplest implementation of deque based on vector.
 * 
 * head and tail starts from center of vector and then goes in different directions.
 * When head == 0 or tail == size new memory is allocated.
 * 
 * @tparam T 
 */
template<typename T>
class Deque {
public:
    const static std::size_t DEFAULT_SIZE = 10;

    Deque(const std::size_t& maxSize = 10) {
        _data.resize(maxSize);
        _head = _tail = maxSize / 2;
    }

    void push_front(const T& value) {
        if (_head == 0) {
            allocateMemory();
        }
        _data[--_head] = value;
    }

    void push_back(const T& value) {
        if (_tail == _data.size()) {
            allocateMemory();
        }
        _data[_tail++] = value;
    }

    T pop_front() {
        T res = front();
        _head++;
        return res;
    }

    T pop_back() {
        T res = back();
        _tail--;
        return res;
    }

    T front() const {
        if (_head == _tail) {
            throw empty_error();
        }

        return _data[_head];
    }

    T back() const {
        if (_head == _tail) {
            throw empty_error();
        }

        return _data[_tail - 1];
    }

    std::size_t size() {
        return _tail - _head;
    }

    void clear() {
        _tail = _head = DEFAULT_SIZE;
        _data.resize(DEFAULT_SIZE);
    }


private:
    std::vector<T> _data;
    std::size_t _head;
    std::size_t _tail;

    void allocateMemory() {
        if (_data.size() == 0) {
            clear();
        } else {
            std::size_t oldSize = _data.size();
            _data.resize(2 * oldSize);
            std::size_t deqSize = size();
            std::size_t newFinish = oldSize + deqSize / 2;

            for (std::size_t i = newFinish; i > newFinish - deqSize; i--) {
                //Write from end to not overwrite elements
                _data[i] = _data[_tail - 1 - (newFinish - i)];
            }

            _tail = newFinish + 1;
            _head = _tail - deqSize;
        }
    }
};
