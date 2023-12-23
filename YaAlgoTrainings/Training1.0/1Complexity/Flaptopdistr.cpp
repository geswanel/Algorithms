/*
2 rectangle laptops on the rectange table
Sides of laptop are parallel to sides of table

Sides of table so the area is min
INPUT: a1 b1 a2 b2
OUTPUT: A B

2 orientations for each laptop
4 possible values
max(a1, a2) * (b1 + b2)
max(a1, b2) * (b1 + a2)
max(b1, a2) * (a1 + b2)
max(b1, b2) * (a1 + a2)
loop

*/

#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    int a1, b1, a2, b2;
    std::cin >> a1 >> b1 >> a2 >> b2;
    int p1 = a1 + b1;
    int p2 = a2 + b2;

    int minArea = (a1 + a2) * (b1 + b2);
    int resA = a1 + a2, resB = b1 + b2;
    for (int A : {a1, b1}) {
        for (int B : {a2, b2}) {
            int area = std::max(A, B) * (p1 - A + p2 - B);
            if (area < minArea) {
                resA = std::max(A, B), resB = (p1 - A + p2 - B);
                minArea = area;
            }
        }
    }

    std::cout << resA << " " << resB << "\n";

    return 0;
}