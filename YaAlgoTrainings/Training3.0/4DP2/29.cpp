/*
N days of lunch
If it costs more than 100 rubles, you get a free coupon

We have lunch for all N days and want to minimize spending

Solution:
Dynamic programming with two parameters: days and coupons.

- The day number defines the row, and the column number defines the number of coupons.
- dp[i][j] - the minimum spent amount on the i-th day, given that there are j coupons available, excluding the lunch on the i-th day. The answer will be in day N + 1.
- In this case, there are fewer coupons than the day number (i.e., j < i), where i is the day number => i = [1, N + 1]; j = [0, N - 1]
- We can reach dp[i][j] from:
    1. dp[i - 1][j + 1] by using a coupon
    2. dp[i - 1][j] if the lunch costs <= 100 rubles on the (i - 1)-th day
    3. dp[i - 1][j - 1] if the lunch costs > 100 rubles on the (i - 1)-th day
    - In cases 2 and 3, we need to add the cost of lunch to the sum, and in case 3, we compare these two sums to find the minimum.
- However, there are exceptions:
    - If j = 0, i.e., no coupons are available at the moment, then we can reach here by:
        1. using a coupon: dp[i - 1][j + 1]
        2. if the lunch costs < 100, then buying lunch: dp[i - 1][j]
        - This means if it's not possible to have exactly 1 coupon in the previous day and lunch costs > 100 rubles, we cannot reach this cell.
- Cells that cannot be reached will have a value of MAX_COST = 30000 - the maximum possible cost of all lunches. Since we are minimizing, 
    we will never get this value in the answer.
- Initially, on day 1, there are 0 coupons and the sum is 0.
    - Then on the second day, we iterate over possible coupon values (0 or 1).

- Solution:
    - We iterate over the cells we can reach and update the cells for the next day, minimizing the sum if we go from the current cell with the sum that already exists there. Initially, everything is initialized to MAX_COST.
*/


#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

const int MAX_COST = 30000;
const int COUPON_COST = 100;

int main() {
    int totalDays;
    std::cin >> totalDays;

    std::vector<int> costOfLunch(totalDays);
    for(int i = 0; i < totalDays; i++) {
        std::cin >> costOfLunch[i];
    }

    std::vector<std::vector<int>> dp(totalDays + 1, std::vector<int>(totalDays + 1, MAX_COST));
    dp[0][0] = 0;

    for (int day = 1; day <= totalDays; day++) {
        for (int coupons = 0; coupons < day; coupons++) {
            const int& curCost = dp[day - 1][coupons];
            if (curCost < MAX_COST) {
                if (costOfLunch[day - 1] > COUPON_COST) {
                    dp[day][coupons + 1] = std::min(dp[day][coupons + 1], curCost + costOfLunch[day - 1]);
                } else {
                    dp[day][coupons] = std::min(dp[day][coupons], curCost + costOfLunch[day - 1]);
                }

                if (coupons > 0) {
                    dp[day][coupons - 1] = std::min(dp[day][coupons - 1], curCost);
                }
            }
        }
    }

    int minCost = MAX_COST;
    int maxCoupons = 0;
    for (int coupons = 0; coupons <= totalDays; coupons++) {
        if (dp[totalDays][coupons] <= minCost) {
            maxCoupons = coupons;
            minCost = dp[totalDays][coupons];
        }
    }
    int coupons = maxCoupons;
    int day = totalDays;   
    std::vector<int> couponDays;
    while (day > 0) {
        int curCost = dp[day][coupons]; 
        int lunchCost = costOfLunch[day - 1];   
        if (curCost == dp[day - 1][coupons + 1]) {
            couponDays.push_back(day);
            coupons++;
        } else if(lunchCost > COUPON_COST) {
            coupons--;
        }

        day--;
    }

    std::reverse(couponDays.begin(), couponDays.end());

    std::cout << minCost << '\n' << maxCoupons << " " << couponDays.size() << '\n';
    for (int i = 0; i < couponDays.size(); i++) {
        std::cout << couponDays[i] << '\n';
    }
    
    return 0;
}