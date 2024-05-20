#include "settings.h"

/*
n ~ 1e5
Given binary array 010101
0 MUST be deleted
get max subarray consist of 1's.


Sliding window.
Have maxSubarray with length max
than we should move window max and try to increase it.

If we have only 1 zero => 
    can move r if next val is 1
    else move all window after contained 0.
*/

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int l = 0, r = 0;
        int ans = 0;
        int zeroId = -1;
        while (r < nums.size()) {
            if (nums[r] == 1) {
                r++;
            } else {
                if (l <= zeroId && zeroId < r) {
                    ans = max(ans, (r - l) - (l <= zeroId && zeroId < r));
                    l = zeroId + 1;
                }

                zeroId = r;
                r++;
            }
        }

        ans = max(ans, (r - l) - (l <= zeroId && zeroId < r || zeroId == -1));

        return ans;
    }
};