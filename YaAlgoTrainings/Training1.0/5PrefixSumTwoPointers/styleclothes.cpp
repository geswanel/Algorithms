/*
Style is more important than the smaller difference in color.
N T-shirts and M pants
color - a number from 1 to 10,000,000
Choose one T-shirt and one pair of pants for the smallest difference.

Numbers are input in ascending order without repetitions.
Output a pair - the color of the T-shirt and pants. If there are multiple, any option is acceptable.

Solution:
2 pointers, one at the beginning of the T-shirts and the other at the beginning of the pants.
Move the pointer that is smaller, and store the colors for maximum style.
*/

#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int N;
    std::cin >> N;
    std::vector<int> tshirts(N);
    for(int i = 0; i < N; i++) {
        std::cin >> tshirts[i];
    }

    int M;
    std::cin >> M;
    std::vector<int> shorts(M);
    for(int i = 0; i < M; i++) {
        std::cin >> shorts[i];
    }

    int tshirtPtr = 0;
    int shortsPtr = 0;
    int minDiff = std::abs(tshirts[tshirtPtr] - shorts[shortsPtr]);
    int tshirtColor = tshirts[tshirtPtr];
    int shortsColor = shorts[shortsPtr];
    while (tshirtPtr < N && shortsPtr < M) {
        if (tshirts[tshirtPtr] < shorts[shortsPtr]) {
            tshirtPtr++;
        } else {
            shortsPtr++;
        }
        
        if (std::abs(tshirts[tshirtPtr] - shorts[shortsPtr]) < minDiff) {
            minDiff = std::abs(tshirts[tshirtPtr] - shorts[shortsPtr]);
            tshirtColor = tshirts[tshirtPtr];
            shortsColor = shorts[shortsPtr];
        }
    }

    std::cout << tshirtColor << " " << shortsColor;


    return 0;
}