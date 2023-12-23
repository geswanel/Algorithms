/*
LCS with answer reconstruction
Given two sequences, find the longest common subsequence

Solution:
2 parameters - elements of the sequences

In dp[i][j], we will store the length of the longest possible subsequence
    - If the symbols at positions i and j are the same, then the length of the subsequence is 1 more than at positions i - 1 and j - 1 (because then this symbol was not present)
    - If the symbols are different, then the length is the maximum of the top and left.
    You can reconstruct the answer backward.
*/


#include <iostream>
#include <vector>
#include <algorithm>

std::istream& operator>>(std::istream& in, std::vector<int>& l) {
    for (int i = 0; i < l.size(); i++) {
        in >> l[i];
    }
    return in;
}

std::ostream& operator<<(std::ostream& out, const std::vector<int>& l) {
    for (int i = 0; i < l.size(); i++) {
        out << l[i] << ' ';
    }
    return out;
}


int main() {
    int N;
    std::cin >> N;
    std::vector<int> fSeq(N);
    std::cin >> fSeq;

    int M;
    std::cin >> M;
    std::vector<int> sSeq(M);
    std::cin >> sSeq;

    int dp[N][M] = {};
    dp[0][0] = (fSeq[0] == sSeq[0] ? 1 : 0);
    for (int j = 1; j < M; j++) {
        dp[0][j] = (dp[0][j - 1] == 1 || fSeq[0] == sSeq[j] ? 1 : 0);
    }

    for (int i = 1; i < N; i++) {
        dp[i][0] = (dp[i - 1][0] == 1 || fSeq[i] == sSeq[0] ? 1 : 0);
    }

    for (int i = 1; i < N; i++) {
        for (int j = 1; j < M; j++) {
            if (fSeq[i] == sSeq[j]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    std::vector<int> sequence;
    int fPos = N - 1;
    int sPos = M - 1;
    while (fPos >= 0 && sPos >= 0) {
        if (fSeq[fPos] == sSeq[sPos]) {
            sequence.push_back(fSeq[fPos]);
            fPos--;
            sPos--;
        } else {
            if (dp[fPos][sPos] == dp[fPos - 1][sPos]) {
                fPos--;
            } else {
                sPos--;
            }
        }
    }
    std::reverse(sequence.begin(), sequence.end());
    
    std::cout << sequence;
    return 0;
}