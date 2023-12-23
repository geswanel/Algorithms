/*
Map of synonyms, find a synonym
*/

#include <unordered_map>
#include <unordered_set>
#include <string>
#include <iostream>

int main() {
    std::unordered_map<std::string, std::string> dict;
    int N;
    std::cin >> N;
    for (int i = 0; i < N; i++) {
        std::string first, second;
        std::cin >> first >> second;
        dict[first] = second;
        dict[second] = first;
    }
    std::string word;
    std::cin >> word;

    std::cout << dict[word];

    return 0;
}