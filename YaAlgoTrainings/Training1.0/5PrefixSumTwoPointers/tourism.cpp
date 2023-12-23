/*
2D mountain range
points on the plane, each to the right of the previous one
A track on the mountain range - a part between two fixed endpoints of segments
Ascent -> y grows. The amount of ascent is the difference in height
Several tracks
for each track determine the height of the ascent
The track can go from left to right as well as from right to left

Solution
Need 2 arrays of prefix sums with total ascent and total descent
then for given start < end point, the difference in ascent
for start > end - the difference in descents

3
1 1 2 2 4 4
5
1 3
1 2
1 1
3 1
3 2

3
4 4 2 2 1 1
5
1 3
1 2
1 1
3 1
3 2

*/

#include <iostream>
#include <vector>

struct Point {
    int x;
    int y;
};

std::istream& operator>>(std::istream& input, Point& p) {
    input >> p.x >> p.y;
    return input;
}

int main() {
    int N;
    std::cin >> N;
    std::vector<int> prefixSumUp(N);
    std::vector<int> prefixSumDown(N);
    prefixSumDown[0] = prefixSumUp[0] = 0;
    
    Point prev, cur;
    std::cin >> prev;
    for (int i = 1; i < N; i++) {
        std::cin >> cur;
        prefixSumUp[i] = prefixSumUp[i - 1] + (cur.y > prev.y) * (cur.y - prev.y);
        prefixSumDown[i] = prefixSumDown[i - 1] + (cur.y < prev.y) * (prev.y - cur.y);
        prev = cur;
    }

    int M;
    std::cin >> M;
    for (int i = 0; i < M; i++) {
        int start, final;
        std::cin >> start >> final;
        if (final > start) {
            std::cout << prefixSumUp[final - 1] - prefixSumUp[start - 1] << '\n';
        } else {
            std::cout << prefixSumDown[start - 1] - prefixSumDown[final - 1] << '\n';
        }
    }

    return 0;
}