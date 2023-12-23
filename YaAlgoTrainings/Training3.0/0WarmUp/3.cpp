/*
Each sticker has a number
We want all the numbers
N stickers, some of which are the same
K collectors arrived, i of them collected all stickers with numbers not less than pi
For each collector, determine how many of the missing stickers Diego has (without repetitions)

Input:
N   <= 100,000
Next, sticker numbers <= 1,000,000,000

Then K collectors <= 100,000
Then numbers pi <= 1,000,000,000

1) 1st solution option using prefix sums, but an array of 1,000,000,000 elements is too much
   However, creating the array requires ~ 1,000,000,000 operations + 100,000 for output. (in terms of memory, 4*10^9 bytes -> 4 * 10^3 Mb, not suitable)
2) Option number 2 - using binary search.
   There are N stickers, 4*10^5 bytes -> 0.4 Mb. Sorting takes NlogN = log(100,000) ~ 15 -> 1,500,000 operations to create the array
   Binary search over the array for K elements takes KlogN operations, approximately the same number of operations

During binary search, you need to find the first element greater than or equal to pi, then its index will be the number of stickers. lBinSearch

Since it is necessary to know how many elements there are before this, set cannot be used because it is not possible to add and subtract iterators from it.
Then unordered_set is used to store existing stickers and check in O(1) time.
*/


#include "../../utils/binary2.h"

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

struct CardParams {
    std::vector<int> diegoCards;
    int minCard;
};

bool checkGreater(const int& index, const CardParams& params) {
    return params.diegoCards[index] >= params.minCard;
}

int main () {
    int N;
    std::cin >> N;
    CardParams params = {std::vector<int>(), 0};
    std::unordered_set<int> existCards;
    for (int i = 0; i < N; i++) {
        int card;
        std::cin >> card;
        if (!existCards.count(card)) {
            params.diegoCards.push_back(card);
            existCards.insert(card);
        }   
    }

    sort(params.diegoCards.begin(), params.diegoCards.end());

    int K;
    std::cin >> K;
    for (int i = 0; i < K; i++) {
        int minCard;
        std::cin >> minCard;
        params.minCard = minCard;
        //std::cout << minCard;
        std::cout << lBinSearch<int, CardParams>(0, params.diegoCards.size(), params, checkGreater) << '\n';
    }

    return 0;
}