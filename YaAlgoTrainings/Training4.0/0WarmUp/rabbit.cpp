/**
 * @file rabbit.cpp
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2023-12-07
 * 
 * Given a grid field of size N × M containing 0 or 1,
 * find the side length of the largest square entirely filled with 1.
 * 
 * N x M < 1000
 * 
 * ~ N^3 - brute force (for each i j check every square with this corner)
 * 
 * DP? lets in dp[i][j] - the side of square with i j right bottom corner.
 * for i, j we have to check
 * - i - 1, j - how many 1 before i, j and above them
 * - i, j - 1 - how many 1 above i and before them
 * - i - 1, j - 1
 * dp[i][j] = 
 *  - 0 if field[i][j] = 0
 *  - else 1 + min(above, before, diag) + 1
 */
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


size_t largetSquareSide(const vector<vector<int>>& field) {
    
    const size_t N = field.size();
    const size_t M = N == 0 ? 0 : field[0].size();
    vector<vector<int>> dp = field;
    
    int ans = count(field[0].begin(), field[0].end(), 1) > 0;
    if (!ans) {
        for (size_t i = 0; i < N; ++i) {
            if (field[i][0] == 1) {
                ans = 1;
                break;
            }
        }
    }
    
    for (size_t i = 1; i < N; ++i) {
        for (size_t j = 1; j < M; ++j) {
            if (field[i][j] == 0) {
                dp[i][j] = 0;
            } else {
                dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                if (dp[i][j] > ans) {
                    ans = dp[i][j];
                }
            }
        }
    }
    
    return ans;
}

int main() {
    size_t N = 0, M = 0;
    cin >> N >> M;
    vector<vector<int>> field(N, vector<int>(M));
    for (size_t i = 0; i < N; ++i) {
        for (size_t j = 0; j < M; ++j) {
            cin >> field[i][j];
        }
    }

    size_t largestSide = largetSquareSide(field);
    cout << largestSide << "\n";
    return 0;
}