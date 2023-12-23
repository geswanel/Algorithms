/*
Build a histogram of character occurrences

Input: text
Each line is no longer than 200 characters
For each character, except spaces and newline characters, display a histogram using the '#' symbol

Solution:
Store the count of each character in a map (a map is used for sorting)
+ keep track of the maximum count of any character m

Then, iterate over the map m times and print a star if the count is >= m
*/


#include <iostream>
#include <map>


int main () {
    std::map<char, int> charCnt;
    std::string word;
    int maxCharCnt = 0;
    while (std::cin >> word) {
        if (word != "") {
            for (const char& ch : word) {
                charCnt[ch]++;
                if (charCnt[ch] > maxCharCnt) {
                    maxCharCnt = charCnt[ch];
                }
            }
        }
    }

    for (int i = maxCharCnt; i > 0; i--) {
        for (const auto& ch : charCnt) {
            std::cout << (ch.second >= i ? '#' : ' ');
        }
        std::cout << '\n';
    }

    for (const auto& ch : charCnt) {
        std::cout << ch.first;
    }



    return 0;
}