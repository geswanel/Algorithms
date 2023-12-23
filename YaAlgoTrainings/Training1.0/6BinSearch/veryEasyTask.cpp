/*
1 instance and N copies are needed
the first one takes x seconds, the second one takes y seconds to copy
What is the minimum time required

1 <= N <= 2 * 10^8
1 <= x y <= 10

The first time we can only use one printer because there is only one copy, and then both, so that it works faster,
but in the end, too, from some point only one printer is needed because one can make several copies faster than the second one
Then let's say we make M copies on the x printer, then N - M copies on the second one
At the same time, the runtime is max(M*x, (N-M)*y), this function is minimal around Mx = (N-M)y
Therefore, we will look for M such that Mx <= (N - M)y - right binary search
will return M at the boundary. If Mx = (N-M)y - then everything is fine
If Mx < (N-M)y - then compare max(Mx, N-My) and max(M + 1 x, N - M - 1 y)
and choose the minimum of them - compare 2 values close to the minimum
*/

#include "binary2.h"
#include <iostream>
#include <algorithm>

struct CopyParams {
    int N;
    int x;
    int y;
};


bool checkCopiesDistr(const int& M, const CopyParams& params) {
    return M * params.x <= (params.N - M) * params.y;
}

int main() {
    CopyParams params;
    std::cin >> params.N >> params.x >> params.y;
    params.N--;
    int M = rBinSearch(0, params.N, params, checkCopiesDistr);  
    
    int minTime = std::min(std::max(M * params.x, (params.N - M) * params.y), 
        std::max((M + 1)* params.x, (params.N - M - 1) * params.y)) +
        std::min(params.x, params.y);

    std::cout << minTime;
    return 0;
}