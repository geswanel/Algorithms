/*
n segments
m points
determine how many segments the point belongs to

Event - start of segment, end of segment, point
First the start of the segment, then we count how many in total, then the end
-1 0 1
Store the number of segments

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using Status = int;

const Status SECTION_START = -1;
const Status DOT = 0;
const Status SECTION_FINISH = 1;

struct LineEvent {
    int coord;
    Status status;
};


bool operator<(const LineEvent& e1, const LineEvent& e2) {
    return e1.coord < e2.coord || (e1.coord == e2.coord && e1.status < e2.status);
}

int main() {
    int N, M;
    std::cin >> N >> M;

    std::vector<LineEvent> events(2 * N + M);
    for (int i = 0; i < 2 * N; i += 2) {
        int a, b;
        std::cin >> a >> b;
        events[i] = LineEvent{a, a <= b ? SECTION_START : SECTION_FINISH};
        events[i + 1] = LineEvent{b, b >= a ? SECTION_FINISH : SECTION_START};
    }

    std::vector<int> coordOfDots(M);
    for (int i = 2 * N; i < 2 * N + M; i++) {
        int dotCoord;
        std::cin >> dotCoord;
        events[i] = LineEvent{dotCoord, DOT};
        coordOfDots[i - 2 * N] = dotCoord;
    }

    sort(events.begin(), events.end());

    int sectionCnt = 0;
    std::unordered_map<int, int> dotIntersections;
    for (const auto& event : events) {
        switch (event.status)
        {
        case SECTION_START:
            sectionCnt++;
            break;
        case SECTION_FINISH:
            sectionCnt--;
            break;
        case DOT:
            dotIntersections[event.coord] = sectionCnt;
            break;
        }
    }

    for (const auto& coord : coordOfDots) {
        std::cout << dotIntersections[coord] << " ";
    }
    return 0;
}