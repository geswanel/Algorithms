/*
Table with values
A turtle moves from the top left to the bottom right only moving right or down

Find the maximum sum and path

Solution:
In dp[i][j], we store the maximum sum when the turtle reached here + the cell from which it arrived
*/


#include <iostream>
#include <vector>

using Code = int;

int main() {
    int N, M;
    std::cin >> N >> M;
    int values[N][M];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            std::cin >> values[i][j];
        }
    }

    int dp[N][M];
    dp[0][0] = values[0][0];
    for (int j = 1; j < M; j++) {
        dp[0][j] = dp[0][j - 1] + values[0][j];
    }

    for (int i = 1; i < N; i++) {
        dp[i][0] = dp[i - 1][0] + values[i][0];
        for (int j = 1; j < M; j++) {
            dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]) + values[i][j];
        }
    }

    std::cout << dp[N - 1][M - 1] << '\n';

    int i = N - 1;
    int j = M - 1;
    std::vector<char> steps(N - 1 + M - 1);
    int stepId = steps.size() - 1;
    while (stepId >= 0) {
        if (i != 0 && j != 0) {
            if (dp[i - 1][j] + values[i][j] == dp[i][j]) {
                steps[stepId] = 'D';
                i--;
            } else {
                steps[stepId] = 'R';
                j--;
            }
        } else {
            if (i == 0) {
                steps[stepId] = 'R';
                j--;
            } else {
                steps[stepId] = 'D';
                i--;
            }
        }

        stepId--;
    }

    for (const char& step : steps) {
        std::cout << step << ' ';
    }

    return 0;
}