/*
Need to find a segment with a value.

Given sequence of numbers and how closer each number compared with previous
*/

#include <iostream>
#include <climits>
#include <string>
#include <iomanip>

int main() {
    long double bounds[2] = {30, 4000};

    int n;
    std::cin >> n;

    long double fprev;
    std::cin >> fprev;
    
    for (int i = 1; i < n; i++) {
        long double fcur;
        std::string dist;
        std::cin >> fcur >> dist;
        
        if (fcur != fprev) {
            long double newbound = (fcur + fprev) / 2;

            if (bounds[0] <= newbound && newbound <= bounds[1]) {
                if (dist == "further") {
                    if (fcur > fprev) {
                            bounds[1] = newbound;
                    } else {
                            bounds[0] = newbound;
                    }
                } else {
                    if (fcur > fprev) {
                            bounds[0] = newbound;
                    } else {
                            bounds[1] = newbound;
                    }
                }
            }
        }

        fprev = fcur;
    }

    std::cout << std::fixed << std::setprecision(7) << bounds[0] << " " << std::setprecision(7) << bounds[1] << '\n';
    return 0;
}