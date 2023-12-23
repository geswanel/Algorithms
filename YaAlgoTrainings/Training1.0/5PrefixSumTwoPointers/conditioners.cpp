/*
install air conditioners in each class.

the higher the class, the more powerful the air conditioner


all classes are numbered from 1 to n
For each class with number i, a power of ai is required >= 
m different models of air conditioners that can be purchased. The power and cost are known

The program calculates the minimum cost

n - number of classes
then n integers ai - minimum power
m - number of offered air conditioners
m lines bj cj power and price

1 <= m n <= 50000
1 <= ai bj cj <= 1000

output - the minimum cost
at least one choice exists


Solution naively
For each class, search for the minimally possible price of a suitable air conditioner - N^2
Variant - sort

Since powers and prices range from 1 to 1000
create 2 vectors of length 1000
for the first vector - index - required power - value - number of such classes
for the second vector - index - price - value - maximum power available at the price.
Then move 2 pointers through these vectors
on the left in the second vector will always be the most accessible offer with the maximum power.
*/


#include <vector>
#include <iostream>

int main() {
    std::vector<int> classes(1001, 0);
    std::vector<int> prices(1001, 0);

    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int a;
        std::cin >> a;
        classes[a]++;
    }

    int m;
    std::cin >> m;
    for (int i = 0; i < m; i++) {
        int b, c;
        std::cin >> b >> c;
        if (b > prices[c]) {
            prices[c] = b;  
        }
    }

    int finalCost = 0;
    int classPtr = 1; 
    int pricePtr = 1;
    while (classPtr < classes.size() && pricePtr < prices.size()) {
        if (classes[classPtr] == 0) {
            classPtr++;
        }

        if (prices[pricePtr] == 0) {
            pricePtr++;
        }

        if (classPtr <= prices[pricePtr]) {
            finalCost += pricePtr * classes[classPtr]; 
            classes[classPtr] = 0;
        } else {
            pricePtr++;
        }
    }
    
    std::cout << finalCost;

    return 0;
}