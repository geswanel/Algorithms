/*
N student
Each knows Mi languages
What languages are know by every student and languages are know at least by one student
*/

#include <iostream>
#include <unordered_map>
#include <string>


int main() {
    int N;
    std::cin >> N;
    std::unordered_map<std::string, int> languages;

    for (int i = 0; i < N; i++) {
        int M;
        std::cin >> M;
        for (int j = 0; j < M; j++) {
            std::string lang;
            std::cin >> lang;
            if (languages.count(lang) == 0) {
                languages[lang] = 0;
            }
            languages[lang]++;
        }
    }

    int knownByAll = 0;
    for (const auto& lang : languages) {
        knownByAll += (lang.second == N);
    }
    std::cout << knownByAll << '\n';

    for (const auto& lang : languages) {
        if (lang.second == N) {
            std::cout << lang.first << '\n';
        }
    }

    std::cout << languages.size() << '\n';

    for (const auto& lang : languages) {
        std::cout << lang.first << '\n';
    }


    return 0;
}