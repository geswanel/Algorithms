/**
 * @file lift.cpp
 * @author geswanel (geswanel@gmail.com)
 * @brief F. lift task solution
 * 
 * There is a building with 'n' floors where 'a_i' people are present on each floor.
 * The elevator can move 'k' people at a time.
 * The elevator starts on the ground floor (floor 0) where the parking lot is located.
 * Employees need to be transported from different floors to the parking lot.
 * The elevator moves at a rate of one floor per second.
 * Find the minimum time required to transport all employees to the parking lot.
 */
#include <iostream>
#include <vector>

using namespace std;

size_t travel(vector<size_t>& floors, size_t k) {
    size_t travels = floors.back() / k;
    floors.back() %= k;
    size_t ans = 2 * (travels + (floors.back() != 0)) * floors.size();
    
    //cout << travels << " times on " << floors.size() << " remained " << floors.back() << "\n";

    if (floors.back() != 0) {
        size_t places = k;
        while (places > 0 && !floors.empty()) {
            if (places > floors.back()) {
                places -= floors.back();
                floors.pop_back();
            } else {
                floors.back() -= places;
                places = 0;
            }
        }
    }

    return ans;
}

size_t lift(vector<size_t>& floors, const size_t k) {
    size_t time = 0;
    while (!floors.empty()) {
        if (floors.back() == 0) {
            floors.pop_back();
        } else {
            time += travel(floors, k);
        }
    }

    return time;
}

int main() {
    size_t k = 0, n = 0;
    cin >> k >> n;
    vector<size_t> floors(n);
    for (auto& floor : floors) {
        cin >> floor;
    }

    size_t time = lift(floors, k);

    cout << time << "\n";

    return 0;
}