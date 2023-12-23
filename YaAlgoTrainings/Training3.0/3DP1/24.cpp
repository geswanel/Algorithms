/*
Buying tickets for N people in a queue
Each person in line can buy 1-3 tickets (1-2 for those behind and 1 for themselves)
Time of purchase Ai Bi Ci, respectively for 1, 2, and 3 tickets

Let K people have already bought tickets in the minimum time

Adding the (K + 1)-th person - they can buy tickets for themselves
   - They can buy tickets from the K-th and (K - 1)-th buyers.
   - We need to choose the minimum of these 3 times + the time it took for the others to buy

N <= 5000
Ai Bi Ci <= 3600

max 3600 * 5000 - there will be no overflow for int
*/


#include <iostream>
#include <vector>
#include <algorithm>

struct PayTime {
    int A;
    int B;
    int C;
};

int min(const int A, const int B, const int C) {
    return std::min(std::min(A, B), C);
}

int minQueueTime(const std::vector<PayTime>& payTimes) {
    std::vector<int> dp(payTimes.size() + 3);
    dp[0] = payTimes[0].A;
    dp[1] = std::min(dp[0] + payTimes[1].A, payTimes[0].B);
    dp[2] = min(dp[1] + payTimes[2].A, dp[0] + payTimes[1].B, payTimes[0].C);
    for (int i = 3; i < payTimes.size(); i++) {
        dp[i] = min(dp[i - 1] + payTimes[i].A, 
                    dp[i - 2] + payTimes[i - 1].B, 
                    dp[i - 3] + payTimes[i - 2].C);
    }
    return dp[payTimes.size() - 1];
}


int main () {
    int totalCustomers;
    std::cin >> totalCustomers;
    std::vector<PayTime> payTimes(totalCustomers);
    for(int i = 0; i < totalCustomers; i++) {
        PayTime& pt = payTimes[i];
        std::cin >> pt.A >> pt.B >> pt.C;
    }

    std::cout << minQueueTime(payTimes);

    return 0;
}