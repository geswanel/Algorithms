/*
A tunnel is being dug under the city to speed up delivery.
A freight train stops near the logistics centers.

At the station:
    - Wagons with a specific product can be attached to the end.
    - A certain number of wagons can be uncoupled from its end.
    - A revision can be carried out - the number of wagons with a specific product.

Process the operations:
N - operations on the train < 100,000
N lines with descriptions
add wagons product - Wagons < 10^9. Product - string
delete wagons - up to the length of the train
get product - determine the number of wagons with the specified product

Wagons will be stored in a stack. The stack's value will be the number of wagons + the product name.

We will also store an unordered_map with products and the number of wagons, and we'll keep track of the size as well.
*/

#include <iostream>
#include <stack>
#include <unordered_map>
#include <string>


struct SubTrain {
    int totalCarriages;
    std::string goods;
};

int main() {
    int N;
    std::cin >> N;

    std::stack<SubTrain> train;
    std::unordered_map<std::string, long long> goodsMap;

    for (int i = 0; i < N; i++) {
        std::string command;
        std::cin >> command;
        if (command == "add") {
            train.push(SubTrain{});
            SubTrain& curSubTrain = train.top();
            std::cin >> curSubTrain.totalCarriages >> curSubTrain.goods;
            if (goodsMap.count(curSubTrain.goods) == 0) {
                goodsMap[curSubTrain.goods] = 0;    
            }
            goodsMap[curSubTrain.goods] += curSubTrain.totalCarriages;
        } else if (command == "delete") {
            long long toDelete;
            std::cin >> toDelete;
            while (toDelete > 0) {
                SubTrain& topTrain = train.top();
                if (toDelete >= topTrain.totalCarriages) {
                    toDelete -= topTrain.totalCarriages;
                    goodsMap[topTrain.goods] -= topTrain.totalCarriages;
                    train.pop();
                } else {
                    topTrain.totalCarriages -= toDelete;
                    goodsMap[topTrain.goods] -= toDelete;
                    toDelete = 0;
                }
            }
        } else if (command == "get") {
            std::string goodName;
            std::cin >> goodName;
            std::cout << (goodsMap.count(goodName) ? goodsMap[goodName] : 0) << "\n";
        }
    }

    return 0;
}