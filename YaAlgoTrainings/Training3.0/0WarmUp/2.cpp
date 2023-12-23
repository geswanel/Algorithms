/*
The beauty of a string is the number of consecutive identical characters

You can change k characters in the string

Solution using two pointers.
- Two pointers define a substring in which we can count the occurrences of characters
    - Change the characters in the substring to the character that appears the most. If there are still characters that can be changed, move the right pointer and check again
        - If not, move the left pointer along with the right pointer, as we have already obtained the maximum window.
    - That is, always move the right pointer
- The loop ends when the right pointer reaches the end of the string

*/


#include <iostream>
#include <algorithm>

int beautyOfString(const std::string& s, const int& canBeChanged) {
    int ans = 0;
    int charCnt[26] = {0};
    int l = 0, r = 0;
    int maxChar = 0;
    while (r < s.size()) {
        charCnt[s[r] - 'a']++;
        maxChar = std::max(maxChar, charCnt[s[r] - 'a']); 
        if (r - l + 1 - maxChar > canBeChanged) {   
            charCnt[s[l] - 'a']--;
            l++;
        } else {
            ans = std::max(ans, r - l + 1);
        }
        
        r++;
    }
    

    return ans;
}

int main() {
    int k;
    std::string s;
    std::cin >> k >> s;

    std::cout << beautyOfString(s, k);

    return 0;
}