/*
Text in file
How many times the word existed before
*/
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    std::unordered_map<std::string, int> wordCnt;

    std::ifstream input("input.txt", std::ifstream::in);

    while (input) {
        std::string word;
        input >> word;
        if (!word.empty()) {
            if (!wordCnt.count(word)) {
                wordCnt[word] = 0;
            }
            std::cout << wordCnt[word]++ << ' ';
        }
    }

    input.close();

    return 0;
}