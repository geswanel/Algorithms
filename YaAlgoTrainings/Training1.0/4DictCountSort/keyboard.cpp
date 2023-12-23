/*
Number of presses for each key until wear.
given key presses - need to understand which keys are wearing out

Input n keys
c1 - cn - number of presses until wear
k - number of presses
p1 - pk - indices of pressed keys
*/


#include <unordered_map>
#include <iostream>


int main() {
    std::unordered_map<int, int> keysPresses;   //index -> presses until break

    int n;
    std::cin >> n;
    for (int i = 1; i <= n; i++) {
        std::cin >> keysPresses[i];
    }

    int k;
    std::cin >> k;
    for (int i = 0; i < k; i++) {
        int id;
        std::cin >> id;
        keysPresses[id]--;
    }

    for (int i = 1; i <= n; i++) {
        std::cout << (keysPresses[i] < 0 ? "YES" : "NO") << '\n';
    }
    return 0;
}