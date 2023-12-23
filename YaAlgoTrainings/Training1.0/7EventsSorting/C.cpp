/*
N students in a row
x coordinates of students
2 students can talk if the distance between them is less than or equal to D

Given N D
X1 .. XN
Need to output
maximum number of options
option for each student

Solution
Beginning event - student coordinate X - end X + D
The counter increases at the beginning and decreases at the end
counter - option number
Since including D, first entry with assignment of option, then exit with release
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <set>

using Status = int;

const Status START_POINT = -1;
const Status END_POINT = 1;

struct StudentEvent {
    int coord;
    Status status;
};

bool operator<(const StudentEvent& s1, const StudentEvent& s2) {
    return s1.coord < s2.coord || (s1.coord == s2.coord && s1.status < s2.status);
}


int main() {
    int N, D;
    std::cin >> N >> D;

    std::vector<int> studentsCoords(N); 
    std::vector<StudentEvent> events(2 * N);
    for (int i = 0; i < 2 * N; i += 2) {
        int coord;
        std::cin >> coord;
        events[i] = StudentEvent{coord, START_POINT};
        events[i + 1] = StudentEvent{coord + D, END_POINT};
        studentsCoords[i / 2] = coord;
    }

    sort(events.begin(), events.end());

    std::unordered_map<int, int> coordTovariant;
    std::set<int> freeVariants;
    int maxVariants = 0;
    for (const auto& event : events) {
        if (event.status == START_POINT) {
            if (freeVariants.empty()) {
                coordTovariant[event.coord] = ++maxVariants;
            } else {
                coordTovariant[event.coord] = *freeVariants.begin();
                freeVariants.erase(freeVariants.begin());
            }
        } else {
            freeVariants.insert(coordTovariant[event.coord - D]);
        }
    }

    std::cout << maxVariants << '\n';

    for (const auto& coord : studentsCoords) {
        std::cout << coordTovariant[coord] << " ";
    }
    return 0;
}