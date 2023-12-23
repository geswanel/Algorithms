/*
N cash registers
Each cash register operates for a certain period of time
How long do all cash registers operate simultaneously

Input N
Then N lines with 4 numbers each
ho mo hc mc - opening and closing time (hours minutes)
Operating time [ho:mo, hc:mc)

If the opening time coincides with the closing time - the cash register operates around the clock
If the first time is greater than the second, then the cash register operates through midnight

The task is to output the total time (per day)

Task for events on a circle.
First pass, ignore the closing times of certain cash registers, count only the openings.
And so on

*/


#include <iostream>
#include <unordered_set>
#include <vector>
#include <algorithm>

struct Time {
    int h;
    int m;
};



bool operator<(const Time& t1, const Time& t2) {
    return t1.h < t2.h || t1.h == t2.h && t1.m < t2.m;
}

bool operator==(const Time& t1, const Time& t2) {
    return t1.h == t2.h && t1.m == t2.m;
}

int operator-(const Time& t1, const Time& t2) {
    Time tmp1 = t1;
    if (t1 < t2) { 
        tmp1.h += 24;
    }

    return (tmp1.h - t2.h) * 60 + tmp1.m - t2.m;
}

std::istream& operator>>(std::istream& in, Time& t) {
    in >> t.h >> t.m;
    return in;
}

using Status = int;
const Status OPEN = 1;
const Status CLOSE = -1;

struct ScheduleEvent {
    int id;
    Time t;
    Status s;
};

bool operator<(const ScheduleEvent& se1, const ScheduleEvent& se2) {
    return se1.t < se2.t || se1.t == se2.t && se1.s < se2.s; 
}

//void debug(const ScheduleEvent& e, const std::unordered_set<int>& openId, const Time& startTime, const int& result);

int main() {
    int N;
    std::cin >> N;

    std::vector<ScheduleEvent> events(2 * N);
    for (int i = 0; i < N; i++) {
        Time open, close;
        std::cin >> open >> close;
        events[2 * i] = ScheduleEvent{i, open, OPEN};
        events[2 * i + 1] = ScheduleEvent{i, close, CLOSE};
    }

    sort(events.begin(), events.end());

    std::unordered_set<int> openId;
    for (int i = 0; i < events.size(); i++) {   
        ScheduleEvent& event = events[i];

        if (event.s == OPEN) {
            openId.insert(event.id);
        } else if (openId.count(event.id)) {    
            openId.erase(event.id);
        }
    }

    int allOpenedTime = 0;
    Time startTime = {0, 0};
    for (int i = 0; i < events.size(); i++) {   
        ScheduleEvent& event = events[i];

        if (event.s == OPEN) {
            openId.insert(event.id);
            if (openId.size() == N) {
                startTime = event.t;
            }
        } else {   
            if (openId.size() == N) {
                if (startTime == event.t) {
                    startTime.h += 24;
                }
                allOpenedTime += event.t - startTime;
            }
            openId.erase(event.id);
        }
    }

    if (openId.size() == N) {  
        allOpenedTime += Time{0, 0} - startTime;
    }

    std::cout << allOpenedTime;
    

    return 0;
}

/*
3
1 0 23 0
12 0 12 0
22 0 2 0

sorted
- 0 1:0 open
- 2 2:0 close
- 1 12:0 close
- 1 12:0 open
- 2 22:0 open
- 0 23:0 close

1 
openId {1, 2}
2 
- openId{0, 1, 2} startTime = 1:0 result = 0
- openId{0, 1} startTime = 1:0 result = 60
- openId{0} startTime = 1:0 result = 60
- openId{0, 1} startTime = 1:0 result = 60
- openId{0, 1, 2} startTime = 22:0 result = 60
- openId{1, 2} startTime = 22:0 result = 120
*/

void debug(const ScheduleEvent& e, const std::unordered_set<int>& openId, const Time& startTime, const int& result) {
    std::cout << "\nevent = {id = " << e.id << "; time = " << e.t.h << ":" << e.t.m << "; " << (e.s == OPEN ? "open" : "close")
        <<  "};  openId {";
    for (const auto& id : openId) {
        std::cout << id << ",";
    }
    std::cout << "} startTime = " << startTime.h << ":" << startTime.m << " result = " << result << '\n';
}