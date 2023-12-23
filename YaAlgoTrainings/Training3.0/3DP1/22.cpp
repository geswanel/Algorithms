/*
One-dimensional board
A grasshopper jumps along it
N cells on the board
can jump from 1 to k cells forward

In how many ways can it jump from the first to the last cell?

N <= 30 -> 2^30 is enough for int
k <= 10

For each N, we need to add up the previous k -> complexity O(N)

Solution: remember the count at the previous steps.
Since the sum of the previous k elements
dp[i] = dp[i - 1] + (dp[i - 1] - dp[i - k])
- dp[i - 1] from the previous step
- dp[i - 1] - dp[i - k] from the remaining k - 1 steps
- Problem with the base case

Another option - store the sum of previous possible steps

*/


#include <iostream>
#include <vector>

int totalWaysToReachEnd(const int squares, const int maxStep) {
    std::vector<int> dp(squares, 0);
    dp[0] = 1; 
    int possibleCases = dp[0];
    for (int i = 1; i < squares; i++) {
        dp[i] = possibleCases;
        possibleCases += dp[i];
        if (i >= maxStep) {
            possibleCases -= dp[i - maxStep];
        }
    }

    return dp.back();
}

int main() {
    int squares, maxStep;
    std::cin >> squares >> maxStep;

    std::cout << totalWaysToReachEnd(squares, maxStep);
    return 0;
}

