/*
Build a Saper field
*/

#include <iostream>
#include <vector>
#include <utility>


using Cell = std::pair<int, int>;


std::vector<std::vector<int>> buildField(const int N, const int M, const std::vector<Cell>& mines) {
    std::vector<std::vector<int>> field(N, std::vector<int>(M, 0));

    for (const auto& [p, q] : mines) {
        field[p - 1][q - 1] = -1;
    }

    for (int i = 0; i != N; ++i) {
        for (int j = 0; j != M; ++j) {
            if (field[i][j] != -1) {
                for (int row = i - 1; row <= i + 1; ++row) {
                    for (int col = j - 1; col <= j + 1; ++col) {
                        if (0 <= row && row < N && 0 <= col && col < M && field[row][col] == -1) {
                            field[i][j]++;
                        }
                    }
                }
            }
        }
    }

    return field;
}

std::ostream& operator<<(std::ostream& out, const std::vector<std::vector<int>>& field) {
    for (const auto& row : field) {
        bool first = true;
        for (const auto& el : row) {
            if (!first) {
                out << " ";
            }
            if (el == -1) {
                out << '*';
            } else {
                out << el;
            }
            first = false;
        }
        out << "\n";
    }

    return out;
}


int main() {
    int N, M;
    std::cin >> N >> M;
    int K;
    std::cin >> K;
    std::vector<Cell> mines;
    for (int i = 0; i < K; ++i) {
        int p, q;
        std::cin >> p >> q;
        mines.push_back({p, q});
    }

    std::vector<std::vector<int>> field = buildField(N, M, mines);
    std::cout << field;
    return 0;
}