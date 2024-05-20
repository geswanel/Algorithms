/*
Description:
N days, eat 1 fish a day
Fish can be stored for k days, including day when bought.
We have costs of fish for next N days

When and how many fish we have to buy to spend least amount of money.
INPUT:
N K ~ 1e5
Ci - N numbers - cost of fish
OUTPUT:
Min spent
N numbers - amount of fish bought everyday
Solution:
At first was thinking about dynamic programming or kind of greedy

1. Going backward for each day decide when it is most beneficial to buy it
O(nk) can be too long 1e10
How to optimize?
- Use c++ for red black tree multiset instead of python
    Construct sliding window O(k log k) with sorted costs
        nlogk to iterate


*/
#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct DayCost {
    int cost;
    int day;
};

bool operator<(const DayCost& lhs, const DayCost& rhs) {
    return lhs.cost < rhs.cost || lhs.cost == rhs.cost && lhs.day > rhs.day;
}

vector<int> buyFish(const int N, const int K, const vector<int>& costs) {
    vector<int> toBuy(N, 0);
    multiset<DayCost> minCostWindow;
    //construct window
    for (int day = N - 1; day > N - 1 - K && day >= 0; --day) {
        minCostWindow.insert({costs[day], day});
    }
    //cout << "size" << minCostWindow.size() << "\n";

    for (int day = N - 1; day >= 0; --day) {
        const DayCost& minDay = *(minCostWindow.begin());
        toBuy[minDay.day]++;
        //erase current day
        minCostWindow.erase({costs[day], day});
        //Add new prev day (day - K)
        if (day - K >= 0) {
            minCostWindow.insert({costs[day - K], day - K});
        }
    }

    return toBuy;
}

long long calculateSum(const int N, const vector<int>& costs, const vector<int>& toBuy) {
    long long sum = 0;
    for (int i = 0; i < N; ++i) {
        sum += ((long long) costs[i]) * toBuy[i];
    }

    return sum;
}

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> costs(N);
    for (int& cost : costs) {
        cin >> cost;
    }

    vector<int> toBuy = buyFish(N, K, costs);
    long long sum = calculateSum(N, costs, toBuy);
    cout << sum << "\n";
    for (int i = 0; i < N; ++i) {
        if (i != 0) {
            cout << " ";
        }
        cout << toBuy[i];
    }
    cout << "\n";
    return 0;
}