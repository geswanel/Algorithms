#include "settings.h"

/*
n spells and m potions

success
spells * potions > success

return pairs length n
pairs[i] - number of potions that will form successful pair

Idea:
Sort potions
For each pair - lowerBound - binsearch
*/

class Solution {
public:
    int pairsCnt(long long spell, const vector<int>& potions, long long success) {
        int i = 0, j = potions.size();
        while (i < j) {
            int mid = (i + j) / 2;
            if (spell * potions[mid] < success) {
                i = mid + 1;
            } else {
                j = mid;
            }
        }

        return potions.size() - i;
    }

    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        
        vector<int> pairs(spells.size());
        for (size_t i = 0; i != pairs.size(); ++i) {
            pairs[i] = pairsCnt(spells[i], potions, success);
        }

        return pairs;
    }
};