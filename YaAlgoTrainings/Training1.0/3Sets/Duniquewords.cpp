/*
Unique words in a file

*/

#include <fstream>
#include <iostream>
#include <unordered_set>
#include <string>

int main() {
    std::ifstream input("input.txt", std::ifstream::in);

    std::unordered_set<std::string> words;

    while (input) {
        std::string word;
        input >> word;
        if (!word.empty()) {
            words.insert(word);
        }
    }
    input.close();

    std::cout << words.size();
    return 0;
}