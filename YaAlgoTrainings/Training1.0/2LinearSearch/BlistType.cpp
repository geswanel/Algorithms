/*
Figure out type of a vector

CONSTANT
ASCENDING
WEAKLY ASCENDING
DESCENDING
WEAKLY DESCENDING
RANDOM
*/

#include <iostream>
#include <vector>
#include <unordered_map>

const int sequenceEnd = -2e9;

const std::vector<std::string> types {
    "CONSTANT",
    "ASCENDING",
    "WEAKLY ASCENDING",
    "DESCENDING",
    "WEAKLY DESCENDING",
    "RANDOM"
};

std::string sequenceType(const std::vector<int>& v) {
    std::unordered_map<std::string, bool> typeBool;
    for (const std::string& type : types) {
        typeBool[type] = true;
    }

    for (size_t i = 1; i < v.size(); ++i) {
        typeBool[types[0]] = typeBool[types[0]] && (v[i - 1] == v[i]);
        typeBool[types[1]] = typeBool[types[1]] && (v[i - 1] < v[i]);
        typeBool[types[2]] = typeBool[types[2]] && (v[i - 1] <= v[i]);
        typeBool[types[3]] = typeBool[types[3]] && (v[i - 1] > v[i]);
        typeBool[types[4]] = typeBool[types[4]] && (v[i - 1] >= v[i]);
    }

    for (const std::string& type : types) {
        if (typeBool[type]) {
            return type;
        }
    }

    return types[5];
}


int main() {
    int num = 0;
    std::vector<int> v;
    do {
        std::cin >> num;
        v.push_back(num);
    } while (num != sequenceEnd);
    v.pop_back();

    std::cout << sequenceType(v);

    return 0;
}
