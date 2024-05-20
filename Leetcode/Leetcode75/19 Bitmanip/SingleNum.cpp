#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        //all numbers appear twice except one that need to be found. XOR property
        // a xor a = 0.  x xor a xor a = x => make xor of all values
        int ans = 0;
        for (size_t i = 0; i != nums.size(); ++i) {
            ans ^= nums[i];
        }

        return ans;
    }
};