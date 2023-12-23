/**
 * Solve equation sqrt(ax + b) = c
 * 
 * INPUT: a, b, c
 * OUTPUT:
 * X1, X2 ... IN ASC ORDER
 * NO SOLUTION
 * MANY SOLUTIONS
 * 
 * Conditions:
 * c >= 0
 *  a != 0
 *      x = (c^2 - b) / a
 *          check if x is int
 *  a == 0
 *      b == c^2 => MANY SOLUTIONS
 *      b != c^2 => NO SOLUTION
 * c < 0
 *  NO SOLUTION
 * 
 * tests:
 * 
 */

#include <iostream>


int main() {
    int a = 0, b = 0, c = 0;
    std::cin >> a >> b >> c;
    
    if (c >= 0) {
        if (a == 0) {
            if (b == c * c) {
                std::cout << "MANY SOLUTIONS\n";
            } else {
                std::cout << "NO SOLUTION\n";
            }
        } else {
            int ax = c * c - b;
            if (ax % a == 0) {
                std::cout << ax / a << "\n";
            } else {
                std::cout << "NO SOLUTION\n";
            }
        }
    } else {
        std::cout << "NO SOLUTION\n";
    }

    return 0;
}