#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, std::vector<int>, std::less<int>> pq(nums.begin(), nums.end());
        for (int i = 0; i + 1 < k; ++i) {
            pq.pop();
        }

        return pq.top();
    }
};