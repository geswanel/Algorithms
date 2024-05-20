#include "settings.h"

/*
Two pointers
Return maxArea of containers with "height" ~ 1e5 borders
so we have i < j that
min(height[i], height[j]) * (j - i) = area

1. Brute n^2 too long

2. Approach -> maximize height from widest to narrowest area. (greedy?)

*/

class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        int ans = min(height[l], height[r]) * (r - l);
        while (l < r) {
            if (height[l] < height[r]) {
                ++l;
            } else if (height[l] > height[r]) {
                --r;
            } else {
                ++l;
                --r;
            }
            int area = min(height[l], height[r]) * (r - l);
            if (ans < area) {
                ans = area;
            }
        }

        return ans;
    }
};