/*
Given filled cells

Find the minimum rectangle that covers all cells
*/


#include <iostream>
#include <climits>


int main() {
    int totalSquares;
    std::cin >> totalSquares;

    int maxX, maxY;
    maxX = maxY = INT_MIN;
    int minX, minY;
    minX = minY = INT_MAX;

    for (int i = 0; i < totalSquares; i++) {
        int xi, yi;
        std::cin >> xi >> yi;

        if (xi < minX) {
            minX = xi;
        }

        if (xi > maxX) {
            maxX = xi;
        }

        if (yi < minY) {
            minY = yi;
        }

        if (yi > maxY) {
            maxY = yi;
        }
    }

    std::cout << minX << " " << minY << " " << maxX << " " << maxY;


    return 0;
}