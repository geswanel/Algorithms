#include <vector>

using namespace std;


class Solution {
public:
    int countNumBits(int num, int size) {
        int ans = 0;
        for (int i = 0; i < size; ++i) {
            ans += (num >> i) & 1;
        }

        return ans;
    }

    vector<int> countBits(int n) {
        vector<int> ans(n + 1);
        for (int i = 0; i <= n; ++i) {
            ans[i] = countNumBits(i, sizeof(n) * 8);
        }

        return ans;
    }
};