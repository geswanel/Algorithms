/*
sorted most oftew words
*/

#include <fstream>
#include <iostream>
#include <unordered_map>
#include <set>
#include <string>

int main() {
    std::unordered_map<std::string, int> wordCnt;

    std::ifstream input("input.txt", std::ifstream::in);
    
    int maxCnt = 0;
    

    while (input) {
        std::string word;
        input >> word;
        if (!word.empty()) {
            if (!wordCnt.count(word)) {
                wordCnt[word] = 0;
            }
            wordCnt[word]++;
            if (wordCnt[word] > maxCnt) {
                maxCnt = wordCnt[word];
            }
        }
    }

    input.close();

    std::string resultWord = "";
    for (const auto& val : wordCnt) {
        if (val.second == maxCnt && (val.first < resultWord || resultWord == "")) {
            resultWord = val.first;
        }
    }

    std::cout << resultWord;

    


    return 0;
}