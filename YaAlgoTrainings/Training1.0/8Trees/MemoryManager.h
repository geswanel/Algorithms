#pragma once

#include <vector>
#include <string>
#include <iostream>
/*
According to the lecture, the memory manager is structured as follows:
- Variables
    - 3 dynamic arrays (vectors)
    - Index of the first free element
- How are elements stored?
    - Initially, the left index points to the next element (we will use the left index as a free index for free elements)
        - That is, we need to traverse from freeElement using left indices to access all possible free elements
    - When allocating memory, we take the element at the freeElement index, then update freeElement to leftId, and return the old index.
        - By saving this index, we can access the elements later.
    - When deleting an element
        - We set the leftId for the deleted element to freeElement. Then we set the freeElement to the ID of the deleted element.
            - Thus, the sequence of free elements is maintained.
*/


class NotEnoughMemoryException : public std::exception {
    public:
        const std::string message = "There is not enough memory to allocate.";
        const std::string& what() {
            return message;
        }
};

class ElementIsNotAllocated : public std::exception {
    public:
        const std::string message = "Element is not allocated";
        const std::string& what() {
            return message;
        }
};

template<typename T>
struct MemoryElement {
    T value;
    int leftId;
    int rightId;
};

const int FREE = - 0x000F91EE;

template<typename T>
class MemoryManager {
    public:
        MemoryManager(int maxSize) {
            freeElement = 0;
            values.resize(maxSize);

            for (int i = 0; i < values.size(); i++) {
                values[i].leftId = i + 1;  // next element
                values[i].rightId = FREE; // is free
            }
        };

        int newElement() {
            if (freeElement == values.size()) { //resize 2 times
                values.resize(2 * values.size() + 1);
                if (values.size() == freeElement) {
                    throw NotEnoughMemoryException();
                }

                for (int i = values.size() / 2; i < values.size(); i++) {
                    values[i].leftId = i + 1;
                    values[i].rightId = FREE;
                }
            }

            int newElementId = freeElement;
            values[newElementId].rightId = 0;
            freeElement = values[newElementId].leftId;

            return newElementId;
        }

        void deleteElement(const int id) {
            values[id].leftId = freeElement;    //next element
            freeElement = id;                   // current free
            values[id].rightId = FREE;
        }

        MemoryElement<T>& get(int id) {
            if (values[id].rightId == FREE) {
                throw ElementIsNotAllocated();
            }
            return values[id];
        }

        const MemoryElement<T>& get(int id) const {
            if (values[id].rightId == FREE) {
                throw ElementIsNotAllocated();
            }
            return values[id];
        }

    private:
        int freeElement;
        std::vector<MemoryElement<T>> values;
};

