/*
Train stays 1 minute on a platform
Intervals between trains on first and second platforms are a and b.
a - 1 - a - 1 - ...

There were n trains on first platform and m trains on the second

min and max time on platform? or -1
Counting starting when no trains on the platforms

a + 1 + a + ... 1 + a - 
MAX = (interval + 1) * count + interval
MIN = (interval + 1) * count - interval

Intersect two intervals
*/

#include <iostream>
#include <utility>
#include <algorithm>

using Interval = std::pair<int, int>;

Interval intersect(const Interval& i1, const Interval& i2) {
    const auto& [l1, r1] = i1;
    const auto& [l2, r2] = i2;
    return {std::max(l1, l2), std::min(r1, r2)};
}


int main() {
    int a, b, n, m;
    std::cin >> a >> b >> n >> m;
    Interval i1 = {(a + 1) * n - a, (a + 1) * n + a};
    Interval i2 = {(b + 1) * m - b, (b + 1) * m + b};

    auto [s, f] = intersect(i1, i2);

    if (f < s) {
        std::cout << -1 << "\n";
    } else {
        std::cout << s << " " << f << "\n";
    }

    return 0;
}