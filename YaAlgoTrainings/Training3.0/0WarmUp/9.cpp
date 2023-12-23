/*
An N x M matrix

Top left corner and bottom right corner 
Need to find the sum of all elements in the numerical matrix in this rectangle

1) Using prefix sums along rows, then iterate over columns and calculate all.

Calculating sums in each row is O(N^2), the answer to one query is O(N) for a total of K queries => O(K*N), which is better than O(K*N^2)

2) Computing prefix sums for the entire matrix. At element i j, the sum of all elements from row 1 to i and from column 1 to j.
Computing prefix sums is O(NM), and the answer to a query is O(1)

How to compute sums in this case?
- It's straightforward in the first row and column, just like in a regular array
- If we want to find Aij, then Aij = A(i-1)j + Ai(j-1) - A(i-1)(j-1) + bij
    - b - matrix of original elements. In the first two terms, we calculate elements up to i-1 j-1 twice, and all others except bij once
        - so we subtract what we counted twice, and we get the answer

The response to the query is given similarly. We subtract x2y1 and x1y2 from x2y2 and add x1y1
*/



#include <iostream>
#include <vector>


std::vector<std::vector<int>> matrixPrefixSumms(const std::vector<std::vector<int>>& matrix) {
    int N = matrix.size();
    int M = matrix[0].size();

    std::vector<std::vector<int>> result(N + 1, std::vector(M + 1, 0));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            result[i + 1][j + 1] = matrix[i][j] + result[i][j + 1] + result[i + 1][j] - result[i][j];
        }
    }

    return result;
}

int rectSumByPrefix(const std::vector<std::vector<int>>& prefix, const int x1, const int y1, const int x2, const int y2) {
    return prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1];
}

int main() {
    int N, M, K;
    std::cin >> N >> M >> K;
    std::vector<std::vector<int>> matrix(N, std::vector<int>(M));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            std::cin >> matrix[i][j];
        }
    }

    std::vector<std::vector<int>> prefixSumms(matrixPrefixSumms(matrix));

    for (int i = 0; i < K; i++) {
        int x1, y1, x2, y2;
        std::cin >> x1 >> y1 >> x2 >> y2;
        std::cout << rectSumByPrefix(prefixSumms, x1, y1, x2, y2) << '\n';
    }

    return 0;
}