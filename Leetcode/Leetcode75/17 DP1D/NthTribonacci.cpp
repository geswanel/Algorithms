#include <vector>

using namespace std;

class Solution {
public:
    int tribonacci(int n) {
        if (n <= 2) {
            return n == 1 || n == 2;
        }
        vector<int> tribonacci_nums(n + 1, 0);
        tribonacci_nums[1] = tribonacci_nums[2] = 1;
        for (int i = 3; i <= n; ++i) {
            tribonacci_nums[i] = tribonacci_nums[i - 1] + tribonacci_nums[i - 2] + tribonacci_nums[i - 3];
        }

        return tribonacci_nums[n];
    }
};