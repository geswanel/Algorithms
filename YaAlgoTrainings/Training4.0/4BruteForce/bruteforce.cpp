#include <iostream>
#include <vector>

using namespace std;

using AnsType = pair<int, vector<int>>;

int getSliceId(int gen, int i) {
    return (gen & (1 << i)) >> i;
}

vector<int> getSlices(int gen, int N) {
    vector<int> slices(N);
    for (int i = 0; i < N; ++i) {
        slices[i] = (getSliceId(gen, i) + 1);
    }
    return slices;
}

AnsType maxSlice(vector<vector<int>> graph, int N) {
    int gen = 2;
    const int MAX_GEN = 1 << N;
    int maxSum = 0, maxSumGen=0;

    while (gen < MAX_GEN) {
        int sum = 0;
        for (int i = 0; i < N; ++i) {
            int sliceId = getSliceId(gen, i);
            for (int j = i + 1; j < N; ++j) {
                if (getSliceId(gen, j) != sliceId && graph[i][j] > 0) {
                    sum += graph[i][j];
                } 
            }
        }

        if (sum > maxSum) {
            maxSum = sum;
            maxSumGen = gen;
        }

        gen += 2;
    }

    return {maxSum, getSlices(maxSumGen, N)};
}

int main() {
    int N = 0;
    cin >> N;
    vector<vector<int>> graph(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> graph[i][j];
        }
    }
    AnsType ans = maxSlice(graph, N);

    cout << ans.first << "\n";
    bool first = true;
    for (const auto& el : ans.second) {
        if (!first) {
            cout << " ";
        }
        cout << el;
        first = false;
    }

    return 0;
}