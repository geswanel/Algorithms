/*
n funny monuments along the street
2 boys, date at the same time
To avoid being seen, the distance between them should be more than r meters
How many ways?

Input:
n r
d1 .. dn - coordinates of the monuments, all different. Monuments are in ascending order

Output - the number of ways such that the distance between monuments is r

Solution:
2 Pointers.
Both start at the beginning
If the difference in distances is less, move the right one.
When it is greater - add all the remaining ones (because the distance will always be greater for a fixed left one)
and move the left pointer

*/

#include <iostream>
#include <vector>

int main() {
    int n, r;
    std::cin >> n >> r;
    std::vector<int> distances(n);
    for(int i = 0; i < n; i++) {
        std::cin >> distances[i];
    }

    int first = 0;
    int last = 0;
    long long possibleWays = 0;
    while (first < n && last < n) {
        if (distances[last] - distances[first] <= r) {
            last++;
        } else {
            possibleWays += n - last;
            first++;
        }
    }

    std::cout << possibleWays;

    return 0;
}
