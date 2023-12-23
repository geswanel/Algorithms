/*
The knight starts from the top left and needs to reach the bottom right
The knight can move L - 2 cells down and one cell right, or one cell down and two cells right
How many different routes exist?

The knight can only reach a row from the previous rows, so we can fill the table row by row.

dp[i][j] - stores the number of different routes to reach this cell
dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2];
*/

#include <iostream>
#include <vector>

struct Point {
    int row;
    int col;
};

int main() {
    int N, M;
    std::cin >> N >> M;

    int dp[N][M] = {};
    dp[0][0] = 1;   
    for (int i = 1; i < N; i++) {
        for (int j = 1; j < M; j++) {
            if (i - 2 >= 0 && j - 1 >= 0) {
                dp[i][j] += dp[i - 2][j - 1];
            }

            if (i - 1 >= 0 && j - 2 >= 0) {
                dp[i][j] += dp[i - 1][j - 2];
            }
        }
    }

    std::cout << dp[N - 1][M - 1] << '\n';
    return 0;
}