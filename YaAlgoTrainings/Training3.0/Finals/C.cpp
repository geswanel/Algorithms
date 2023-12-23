/*
2 warehouses
1 courier, 1 order simultaneously

N orders, can be delivered from either warehouse

For each order and each of the two warehouses, we know the return time to the warehouse

Order of orders is arbitrary

Execution of the next order after returning to the warehouse

For each order, determine the courier. So that the last of the two returns earlier.

N orders with up to 1e3 deliveries
ai bi - delivery and return times for couriers

Output N numbers 1 or 2, specifying the courier number

Dynamic Programming

Let's say I have distributed i orders for minimum time. I distribute i - 1 and choose the minimum, whether to deliver from the first or the second warehouse.
Meanwhile, I keep track of the return time
*/


#include <iostream>
#include <vector>
#include <algorithm>

struct Order {
    int a;
    int b;
    int id;
};

struct DP {
    int time;
    int aReturn;
    int bReturn;
};

int main() {
    int N;
    std::cin >> N;
    std::vector<Order> orders(N + 1, {0, 0, -1});
    for (int i = 1; i <= N; i++) {
        std::cin >> orders[i].a >> orders[i].b;
    }

    std::vector<DP> dp(N + 1);
    dp[0] = {0, 0, 0};
    for (int i = 1; i <= N; i++) {
        if (dp[i - 1].aReturn + orders[i].a < dp[i - 1].bReturn + orders[i].b) {
            dp[i].time = std::max(dp[i - 1].aReturn + orders[i].a, );
            dp[i].aReturn = dp[i]
        } else {

        }
    }


    

    return 0;
}