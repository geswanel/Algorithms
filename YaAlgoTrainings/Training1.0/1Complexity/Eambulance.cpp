/*
K1 - flat number
K2, P2, N2 - flat number, building entrance, floor number
M floors
Number of flats on a floor is the same
Find out P1 and N1

INPUT: K1 M K2 P2 N2 - from 1 to 1e6
OUTPUT:
    Definite P1 N1
    Not Definite - 0
    Contradiction - -1

F - flats on a floor
F * M - flats in a building entrance

1. Make K, P, N from 0
K = PFM + NF + K % F = (P * M + N) * F + K % F
P = K / MF
N = (K - P * MF) / F
2. iterate over all possible values for F from 1 until (P * M + N) * F <= K
*/

#include <iostream>
#include <vector>
#include <utility>


int main() {
    int K1, M, K2, P2, N2;
    std::cin >> K1 >> M >> K2 >> P2 >> N2;
    if (N2 > M) {
        std::cout << "-1 -1\n";
        return 0;
    }


    K1--, K2--, P2--, N2--;

    int div = (P2 * M + N2);
    if (div == 0) {
        // P2 = 1, N2 = 1
        if (K1 <= K2) {
            std::cout << "1 1\n";
        } else {
            int n1 = M == 1;
            int p1 = (K1 + 1) <= M * (K2 + 1);
            std::cout << p1 << " " << n1 << "\n";
        }
    } else {
        int f = 0;
        std::vector<std::pair<int, int>> pn;
        while (++f * div <= K2) {
            if (K2 == div * f + K2 % f) {
                int p = K1 / (M * f);
                int n = (K1 - p * M * f) / f;
                pn.push_back({p, n});
            }
        }

        if (pn.empty()) {
            std::cout << -1 << " " << -1 << "\n";
        } else {
            auto [p1, n1] = pn.front();
            for (const auto& [p, n] : pn) {
                if (p1 != p) {
                    p1 = -1;
                }

                if (n1 != n) {
                    n1 = -1;
                }
            }
            std::cout << p1 + 1 << " " << n1 + 1 << "\n";
        }
    }

    return 0;
}