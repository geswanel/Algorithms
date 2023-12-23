/*
Possible operations
X*2
X*3
X + 1

The minimum number of operations to make 1 into N

N <= 10^6
Answer <= 10^6 because we can simply add 1

Output - the minimum number of operations - Order of numbers
*/


#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

struct MinWays {
    int minWays;
    int prevValue;
};

struct MinWaysAns {
    std::vector<int> sequence;
    int minWays;
};

MinWaysAns minStepToGetN(const int N) {
    std::vector<MinWays> dp(N + 1);
    dp[1] = MinWays{0, -1};
    for (int i = 2; i <= N; i++) {
        dp[i] = {dp[i - 1].minWays + 1, i - 1};
        if (i % 2 == 0 && dp[i / 2].minWays + 1 < dp[i].minWays) {
            dp[i] = {dp[i / 2].minWays + 1, i / 2};
        }

        if (i % 3 == 0 && dp[i / 3].minWays + 1 < dp[i].minWays) {
            dp[i] = {dp[i / 3].minWays + 1, i / 3};
        }
    }

    MinWaysAns ans;
    ans.minWays = dp[N].minWays;
    int val = N;
    while (val != -1) {
        ans.sequence.push_back(val);
        val = dp[val].prevValue;
    }

    std::reverse(ans.sequence.begin(), ans.sequence.end());
    return ans;
}

int main() {
    int N;
    std::cin >> N;
    
    MinWaysAns ans = minStepToGetN(N);
    std::cout << ans.minWays << '\n';

    for(int i = 0; i < ans.sequence.size(); i++) {
        std::cout << ans.sequence[i] << ' ';
    }

    return 0;
}