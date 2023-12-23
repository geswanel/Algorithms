#include "../../settings.h"

/*
find i < j < k so nums[i] < nums[j] < nums[k]
n ~ 1e5

true false

1. brute force n^3 too much
2. 
    a. Suffix max to find out if there is needed k for i and j O(1)
    b. i = 0
    move i until local min
    move j from i until nums[j + 1] <= nums[j] and nums[j + 1] > nums[i]

    have two options.
        1. max suffix > nums[j] => true
        2. than move i = j + 1

3. Max suffix and min prefix

*/

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if (nums.size() < 3) {
            return false;
        }

        vector<int> suffixMax(nums.size());
        suffixMax[nums.size() - 1] = numeric_limits<int>::min(); 
        for (int i = nums.size() - 2; i >= 0; --i) {
            suffixMax[i] = max(suffixMax[i + 1], nums[i + 1]);
        }

        vector<int> prefixMin(nums.size());
        prefixMin[0] = numeric_limits<int>::max(); 
        for (int i = 0; i + 1 < nums.size(); ++i) {
            prefixMin[i + 1] = min(prefixMin[i], nums[i]);
        }

        for (int i = 1; i + 1 < nums.size(); ++i) {
            if (prefixMin[i] < nums[i] && nums[i] < suffixMax[i]) {
                return true;
            }
        }

        return false;
    }
};