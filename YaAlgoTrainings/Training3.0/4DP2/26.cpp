/*
An NxM table with numbers
Start - top left
You can only move right or down
When traversing, the player takes the food written in the cell (also in the first and last cells)
You need to find the minimum weight that the player can give away to reach the bottom right corner

Solution:
Dynamic programming in two dimensions
    - In each cell, we write the minimum weight given away to reach that cell, including the cell itself
    - The answer is in the bottom right corner
*/



#include <iostream>
#include <algorithm>


int main() {
    int N, M;
    std::cin >> N >> M;
    int table[N][M];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            std::cin >> table[i][j];
        }
    }

    int dp[N][M] = {0};
    dp[0][0] = table[0][0];
    for (int j = 1; j < M; j++) {
        dp[0][j] = dp[0][j - 1] + table[0][j]; 
    }

    for (int i = 1; i < N; i++) {
        dp[i][0] = dp[i - 1][0] + table[i][0];
        for (int j = 1; j < M; j++) {
            dp[i][j] = std::min(dp[i - 1][j], dp[i][j - 1]) + table[i][j];
        }
    }

    std::cout << dp[N - 1][M - 1];


    return 0;
}