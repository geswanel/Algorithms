/*
n diplomas
wxh - sizes
Square board for diplomas
the program calculates the minimum size of the board to accommodate the diplomas

An array is needed from 1 to (h + w) * n
which needs to be traversed by left binary search checking the condition
how to check the condition?
If the side length is a, then there are a/w diplomas in a row and a/h diplomas in a column
then if a/w * a/h >= n then everything is fine

What values of a need to be checked? starting from max(h, w) and ending at max(h, w) * n
*/


#include "binary2.h"
#include <iostream>
#include <algorithm>


struct DiplomaParams {
    int n;
    int w;
    int h;
};


bool checkFunction(const long long& sideSize, const DiplomaParams& params) {
    return (sideSize / params.w) * (sideSize / params.h) >= params.n;
}

int main() {
    DiplomaParams params;
    std::cin >> params.w >> params.h >> params.n;

    long long l = 1;
    long long r = ((long long)params.n) * std::max(params.h, params.w);
    long long ans = lBinSearch<long long, DiplomaParams>(l, r, params, checkFunction);
    std::cout << ans;
    return 0;
}