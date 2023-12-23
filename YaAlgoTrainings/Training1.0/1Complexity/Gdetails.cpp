/*
N kg of metal
Templates K kg each -  N / K
Detail M kg each => K / M details + K % M metal remained
Remained used again as metal

Number of details?

*/

#include <iostream>

int main() {
    int N, K, M;
    std::cin >> N >> K >> M;

    int details = 0;
    if (K >= M) {
        int templates = 0;
        int templateDetails = K / M;
        int templateRemained = K % M;
        while ((templates = N / K) > 0) {
            details += templates * templateDetails;
            N = N % K + templates * templateRemained;
        }
    }

    std::cout << details;
    return 0;
}