/*
Given N
Determine the number of sequences of 0 and 1 of length N
In which no 3 ones stand together

Condition - no 3 ones stand together

N <= 35

Idea: Let there be a sequence of length k that satisfies the condition. Then we will build a sequence of length k + 1 satisfying the condition

1. k0 will always satisfy the condition. That is, this will give us as many options as sequences of length k
2. k1 will satisfy the condition if k != (k - 2)11
   - At the same time, (k-2)11 = (k-3)011.
   - In the end, this will give us k - (k - 3) options

dp[k] = dp[k - 1] + dp[k - 1] - dp[k - 4]

At the same time
N = -1 -2 -3 = 0 options
N = 0 -> 1 option (empty sequence)
N = 1 -> 2 options
N = 2 -> 4 options
N = 3 -> 7 options
N = 4 -> 13 options
N = 5 -> 24 options

*/


#include <iostream>
#include <vector>

int rightSequences(const int N) {
    std::vector<int> rightSeq(N + 4);
    rightSeq[0] = 1;
    rightSeq[1] = 2;
    rightSeq[2] = 4;
    rightSeq[3] = 7;
    for (int i = 4; i <= N; i++) {
        rightSeq[i] = rightSeq[i - 1] * 2 - rightSeq[i - 4];
    }


    return rightSeq[N];
}


int main() {
    int N;
    std::cin >> N;
    std::cout << rightSequences(N);
    return 0;
}