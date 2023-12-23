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
 * @brief implementation of queue structure based on std::vector.
 * 
 * Vector is used as ring buffer.
 * Elements are pushed at the back of the buffer and pop from the front.
 * Tail points to the next free space for the element. head points to the front element
 * 
 * When head equals tail it means there is no elements in structure.
 * If tail % size equals head % size and tail > head - this means there is no free space and more memory should be allocated.
 * 
 * @tparam T 
 */
template<typename T>
class Queue {
public:
    const static std::size_t DEFAULT_SIZE = 10;

    Queue(const std::size_t maxSize = DEFAULT_SIZE) {
        _data.resize(maxSize);
        _size = maxSize;
        _head = 0;
        _tail = 0;
    }

    void push(const T& value) {
        if (_size == 0 || (_tail % _size == _head % _size) && (_tail > _head)) {
            allocateMemory();
        }
        _data[_tail % _size] = value;
        _tail++;
    }

    T pop() {
        T ans = front();
        _head++;

        if (_head >= _size && _tail >= _size) {
            _head -= _size;
            _tail -= _size;
        }
        return ans;
    }

    T front() const {
        if (_head == _tail) {
            throw empty_error();
        }

        return _data[_head % _size];
    }

    std::size_t size() const {
        return _tail - _head;
    }

    void clear() {
        _head = _tail = 0;
        _data.resize(DEFAULT_SIZE);
        _size = DEFAULT_SIZE;
    }

private:

    std::vector<T> _data;
    std::size_t _size;
    std::size_t _head;
    std::size_t _tail;

    
    /**
     * @brief allocates new memory when data is full.
     */
    void allocateMemory() {
        if (_size == 0) {
            clear();
        } else {
            _data.resize(2 * _size);
            if (_tail % _size < _head % _size) {
                for (std::size_t i = _size; i < _size + (_tail % _size); i++) {
                    _data[_size + i] = _data[i];
                }
            }
            // There is no need to change _tail because if _tail < _head => _tail = _size + _tail % size;
            _size *= 2;
        }
    }
};