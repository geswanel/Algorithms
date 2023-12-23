/*
Number of unique numbers in a list of numbers
*/
#include <iostream>
#include <unordered_set>

int main() {
    std::unordered_set<int> nums;
    
    while (std::cin.peek() != '\n') {
        int num;
        std::cin >> num;
        nums.insert(num);
    } 

    std::cout << nums.size();

    return 0;
}