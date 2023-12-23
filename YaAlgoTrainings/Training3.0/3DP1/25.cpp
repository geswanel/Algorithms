/*
Nails are driven in, any 2 can be connected by a thread
It is required to connect some pairs so that everyone is attached to something and the length of the thread is minimized

N <= 100
coordinates of the nails

4 nails ideally will never be connected, as you can cut the thread between pairs and shorten it

We keep dp[i] storing the minimum length when everything is already good
If the i-th nail arrives then either
    - connect i - 1 and i
    - connect i - 2, i - 1, and i
*/


#include <iostream>
#include <vector>
#include <algorithm>


int main() {
    int N;
    std::cin >> N;
    std::vector<int> coords(N);
    for(int i = 0; i < N; i++) {
        std::cin >> coords[i];
    }
    sort(coords.begin(), coords.end());


    std::vector<int> dp(N);
    dp[0] = -1;
    dp[1] = coords[1] - coords[0];
    dp[2] = coords[2] - coords[0];
    for (int i = 3; i < N; i++) {
        dp[i] = std::min(dp[i - 2] + coords[i] - coords[i - 1], dp[i - 1] + coords[i] - coords[i - 1]);
    }

    std::cout << dp[N - 1];
    return 0;
}

