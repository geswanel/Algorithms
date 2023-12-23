/*
we have a1 .. am - length of bricks. Have 2 bricks of each type

Can reach length N using this bricks

N ~ 10^9
M ~ 15
ai ~ 10^9

Min number of bricks to get exactly N and what bricks should be used
0 If we can do it by breaking some bricks
-1 if we cannot reach N

Use greedy + Brute force?
1. Sort bricks
2. Starting with the longest go into recursy and choose next brick


Tests:
N M
a1 a2 a3 .. am

10 3
2 4 5
10 = 4 + 4 + 2 = 5 + 5
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;


void putBricks(vector<int>& border, const int bLen, vector<int>& takenBricks, 
               const vector<int>& bricks, int remSum, const size_t id = 0) {
    if (bLen == 0 && (border.empty() || takenBricks.size() < border.size())) {
        border = takenBricks;
    } else if (bLen > 0 && bLen <= remSum) {
        for (size_t i = id; i < bricks.size(); ++i) {
            takenBricks.push_back(bricks[i]);
            remSum -= bricks[i];
            putBricks(border, bLen - bricks[i], takenBricks, bricks, remSum, i + 1);
            takenBricks.pop_back();
        }
    }
}

vector<int> makeBorder(const int bLen, vector<int>& bricks) {
    int sum = accumulate(bricks.begin(), bricks.end(), 0);
    if (sum < bLen) {
        return {-1};
    } else if (sum == bLen) {
        return bricks;
    } else {
        vector<int> takenBricks;
        vector<int> border;
        sort(bricks.begin(), bricks.end(), [](const int lhs, const int rhs) {return lhs > rhs;});

        putBricks(border, bLen, takenBricks, bricks, sum);

        if (border.empty()) {
            return {0};
        } else {
            return border;
        }
    }
}


int main() {
    int N, M;
    cin >> N >> M;
    vector<int> bricks(2 * M);
    for (int i = 0; i < 2 * M; i += 2) {
        cin >> bricks[i];
        bricks[i + 1] = bricks[i];
    }

    vector<int> border = makeBorder(N, bricks);

    if (border[0] == -1 || border[0] == 0) {
        cout << border[0];
    } else {
        cout << border.size() << "\n";

        bool first = true;
        for (const auto& brick : border) {
            if (!first) {
                cout << " ";
            }
            cout << brick;
            first = false;
        }
    }

    return 0;
}