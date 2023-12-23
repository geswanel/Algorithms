/*
N students <= 10^9
Desks from 0 to N-1, each student at a desk
Without observation, opens the phone and searches for answers
M teachers observe the students
Teacher i sees students at desks bi to ei inclusive
You need to calculate the number of students who will search for answers

Input N M
bi ei - M lines
*/

#include <iostream>
#include <vector>
#include <algorithm>


const int START_STATUS = -1;
const int FINISH_STATUS = 1;

struct TeacherObservationEvent {
    int place;  
    int status;    
};

bool operator<(const TeacherObservationEvent& t1, const TeacherObservationEvent& t2) {
    return t1.place < t2.place || (t1.place == t2.place && t1.status < t2.status);
}

int main() {
    int N, M;
    std::cin >> N >> M;
    
    std::vector<TeacherObservationEvent> events(2 * M);
    for (int i = 0; i < 2 * M; i += 2) {
        int start, finish;
        std::cin >> start >> finish;
        events[i] = {start, START_STATUS};
        events[i + 1] = {finish, FINISH_STATUS};
    }

    sort(events.begin(), events.end());

    int observed = 0;   
    int studentsSearched = 0;
    int prevPlace = 0;
    for (const auto& event : events) {
        if (event.status == START_STATUS) {
            studentsSearched += (observed == 0) * (event.place - prevPlace);
            observed++;
        } else {
            observed--;
            prevPlace = event.place + 1;
        }
    }
    studentsSearched += N - prevPlace;

    std::cout << studentsSearched;

    return 0;
}