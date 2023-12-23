/*
2D pyramid - width and height of each block are given
One block can be placed on top of another only if the width of the upper block is strictly less than the lower one
The bottommost block can be of any width
The maximum height of the pyramid based on the given blocks

Solution:
It is logical to arrange the blocks from greater width to smaller width. That is, each width in the pyramid is unique.
Then, among the blocks with the same width, we need to choose the one with the maximum height. Therefore, it is sufficient to store only one block with the maximum height for a given width.
Then, simply sum up all the heights.
*/


#include <iostream>
#include <algorithm>
#include <unordered_map>

int main() {
    std::unordered_map<int, int> blocks; //width -> height

    int N;
    std::cin >> N;
    for (int i = 0; i < N; i++) {
        int width, height;
        std::cin >> width >> height;
        blocks[width] = std::max(blocks[width], height);
    }

    long long resultHeight = 0;
    for (const auto& block : blocks) {
        resultHeight += block.second;
    }

    std::cout << resultHeight;

    return 0;
}