/*
K - a lucky number
N cars are parked along the street
How many sets of cars are parked in spaces from L to R
such that the sum of their numbers is equal to K

Solution - prefix sums for the car numbers

To find the required sums, use 2 pointers. Since the car numbers are positive, the prefix sums always increase.
So if the sum between [L, R) is greater than K, move the left pointer; if it is less, move the right pointer.
If L = R, always move the right pointer.
*/

#include <iostream>
#include <vector>

int main() {
    int N, K;
    std::cin >> N >> K;

    std::vector<int> prefixSum(N + 1);
    prefixSum[0] = 0;
    for (int i = 1; i <= N; i++) {
        int num;
        std::cin >> num;
        prefixSum[i] = prefixSum[i - 1] + num;
    }

    int l = 0;
    int r = 0;
    int cntK = 0;
    while (l <= N && r <= N) {
        if (prefixSum[r] - prefixSum[l] == K) {
            cntK++;
        }

        if (l == r || prefixSum[r] - prefixSum[l] < K) {
            r++;
        } else if (prefixSum[r] - prefixSum[l] > K) {
            l++;
        } else {
            r++;
            l++;
        }
    }
    std::cout << cntK;
    
    return 0;
}