/*
Manhattan
S->N an avenue each 100 meters 
W->E a street each 100 meters
numbered: less -> Western or Southern

=> Cartesian system
x - avenue and y - street
The distance is  abs(x1 - x2) + abs(y1 - y2)

From 0 0 - a random path
Each minute either stay on the same point or move in a random direction
Each t minutes a navigator tells where we are located.
    Shows with precision - any point with the distance <= d

After t * n minutes - Where are we?

In t minutes have Rt of possible positions
Also has Rd - circle of possible positions from navigator
Their intersection - possible positions 
*/
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

struct DiagRect {
    //Described with diagonals y = {x + p1, x + p2, q1 - x, q2 - x}; where p1 > p2 and q1 > q2
    int p1;
    int p2;
    int q1;
    int q2;

    DiagRect(int x, int y, int dist) {
        p1 = y + dist - x;
        p2 = y - dist - x;
        q1 = y + dist + x;
        q2 = y - dist + x;
    }

    friend std::ostream& operator<<(std::ostream& out, const DiagRect& dr) {
        out << dr.p1 << " " << dr.p2 << " " << dr.q1 << " " << dr.q2;
        return out;
    }

    void intersect(const DiagRect& dr) {
        p1 = std::min(p1, dr.p1);
        p2 = std::max(p2, dr.p2);

        q1 = std::min(q1, dr.q1);
        q2 = std::max(q2, dr.q2);
    }

    void expand(int t) {
        p1 += t;
        p2 -= t;
        q1 += t;
        q2 -= t;
    }

    std::vector<std::pair<int, int>> getPoints() const {
        std::vector<std::pair<int, int>> points;
        int left = (q2 - p1) / 2 + ((q2 - p1) > 0 && (q2 - p1) % 2 == 1);
        int right = (q1 - p2) / 2 - ((q1 - p2) < 0 && (q1 - p2) % 2 == -1);;
        for (int x = left; x <= right; ++x) {
            int down = std::max(q2 - x, x + p2);
            int up = std::min(x + p1, q1 - x);
            for (int y = down; y <= up; ++y) {
                points.push_back({x, y});
            }
        }

        return points;
    }
};




int main() {
    int t, d, n;
    std::cin >> t >> d >> n;
    DiagRect prev(0, 0, 0);
    for (int i = 0; i < n; ++i) {
        int xi, yi;
        std::cin >> xi >> yi;
        DiagRect cur(xi, yi, d);
        prev.expand(t);
        cur.intersect(prev);
        prev = cur;
    }

    std::vector<std::pair<int, int>> points = prev.getPoints();
    std::cout << points.size() << "\n";
    for (const auto& [x, y] : points) {
        std::cout << x << ' ' << y << '\n';
    }

    return 0;
}