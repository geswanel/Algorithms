/*
Find the maximum length substring of a string such that each character occurs no more than k times.

Input:
n k - number of characters and maximum characters
Lowercase Latin letters
n characters
Output the length of the substring and the index of the first character.

The problem is solved using two pointers, moving the left one when the condition is no longer met, and the right one while it is met.

At the same time, checking the condition takes 26 operations (26 characters) using an unordered_map.
*/

#include <unordered_map>
#include <iostream>


bool checkCondition(const std::unordered_map<char, int>& charCnt, const int k) {
    for (const auto& ch : charCnt) {
        if (ch.second > k) {
            return false;
        }
    }

    return true;
}

int main() {
    int n, k;
    std::cin >> n >> k;
    
    std::string text;
    std::cin >> text;

    int l = 1;
    int r = 1;
    int maxLen = 0;
    int startPos = 1;
    std::unordered_map<char, int> charCnt;
    while (l <= n && r <= n) {
        while (checkCondition(charCnt, k) && r <= n) {
            if (charCnt.count(text[r - 1]) == 0) {
                charCnt[text[r - 1]] = 0;
            }
            charCnt[text[r - 1]]++;
            
            r++;
        }
        
        if (!checkCondition(charCnt, k)) {
            if (r - l - 1 > maxLen) {
                maxLen = r - l - 1;
                startPos = l;
            }
            while (!checkCondition(charCnt, k)) {

                --charCnt[text[l - 1]];
                l++;
            }
        } else {
            if (r - l > maxLen) {
                maxLen = r - l;
                startPos = l;
            }

        }

    }

    std::cout << maxLen << " " << startPos;
    return 0;
}

