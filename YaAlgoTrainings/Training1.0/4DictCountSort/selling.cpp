/*
Database with records Customer Product Quantity
Customer and Product are strings without spaces
Create a list of all customers, with each customer having a list of all products with their respective quantities
Output in the format:
Customer:
Product1 Quantity1
Product2 Quantity2

Ordered lexicographically => using a regular map
*/

#include <map>
#include <iostream>
#include <fstream>

int main() {
    std::ifstream input("input.txt", std::ifstream::in);
    
    std::map<std::string, std::map<std::string, long long>> database;


    while (input) {
        std::string customer, product;
        long long count;
        if (input >> customer >> product >> count) {
            database[customer][product] += count;
        }
    }

    input.close();
    
    for (const auto& dbRow : database) {
        std::cout << dbRow.first << ":\n";
        for (const auto& prod : dbRow.second) {
            std::cout << prod.first << ' ' << prod.second << '\n';
        }
    }
    return 0;
}