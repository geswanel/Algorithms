/*
Twice a working day
Information about the time a customer arrives and leaves

When to start advertising so that as many users as possible listen from start to finish
The video lasts 5 time units
Transmissions should not overlap

+ The number of different people who listened

N customers <= 2000
then a pair of N numbers, arrival and departure times
Departure time > arrival time

Output 3 numbers
the number of customers who listened to the entire video
and the moments when the broadcast should start in ascending order

Solution:
1) There is no point in keeping track of people who were there for less than 5 time units
2) The broadcast can start at any time
At the moment the broadcast is turned on, we save the number of people
We start the broadcast either when the next person enters or when the previous segment ends
Why?
- If you just start at a random time, you can roll back to before the next customer enters, then more will listen because
all exits from the store have shifted to the right, but the entrances did not intersect
- But it may be the case that the segment from the previous entrance intersects with the current one, then you can start from the end of the previous one to account for intersections

Event - arrival and departure of a person.
The maximum number of people is not necessarily maximum and the one after it, so you need
1. We go through the events, if the person has just entered, we start counting how many people, we save the unordered_set with the ids of the people and
quantity.
2. After that, we sort the array of possible broadcasts and go through it, checking the intersection of time and intersections of sets of people.

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using Status = int;
const Status IN = -1;
const Status OUT = 1;

const int DURATION = 5;

struct CustomerEvent {
    int time;
    Status status;
    int id;
};

bool operator<(const CustomerEvent& e1, const CustomerEvent& e2) {
    return e1.time < e2.time || e1.time == e2.time && e1.status < e2.status;
}

struct Adverb {
    int start; 
    int end;
    std::unordered_set<int> watchersId;
};

bool operator<(const Adverb& a1, const Adverb& a2) {
    return a1.watchersId.size() < a2.watchersId.size();
};

bool intersect(const Adverb& a1, const Adverb& a2) {
    return a1.start < a2.start && a2.start < a1.end || a1.start < a2.end && a2.end < a1.end;
};

int countWatchers(const Adverb& a1, const Adverb& a2) {
    int result = a1.watchersId.size();
    for (const auto& id : a2.watchersId) {
        if (a1.watchersId.count(id) == 0){
            result++;
        }
    }
    return result;
}




int main() {
    int N;
    std::cin >> N;

    std::vector<CustomerEvent> events;
    for (int i = 0; i < N; i++) {
        int in, out;
        std::cin >> in >> out;
        
        events.push_back(CustomerEvent{in, IN, i});
        events.push_back(CustomerEvent{out, OUT, i});
    }
    sort(events.begin(), events.end());

    std::vector<Adverb> adverbs;
    std::unordered_set<int> watchersId;
    int prevEnd = 0;
    for (int i = 0; i < events.size(); i++) {
        if (events[i].status == IN) {
            watchersId.insert(events[i].id);

            

            Adverb curStartAd = {events[i].time, events[i].time + DURATION, watchersId};
            for (int j = i; j < events.size() && events[j].time < curStartAd.end; j++) {
                if (events[j].status == OUT) {
                    curStartAd.watchersId.erase(events[j].id);
                }
            }
            adverbs.push_back(curStartAd);

            if (prevEnd > curStartAd.start) {
                Adverb notIntersAd = {prevEnd, prevEnd + DURATION, watchersId};
                for (int j = i + 1; j < events.size() && events[j].time < notIntersAd.end; j++) {
                    if (events[j].status == IN && events[j].time < notIntersAd.start) {
                        
                    }
                }
            }


            prevEnd = curStartAd.end;
        } else {
            watchersId.erase(events[i].id);
        }
    }

    sort(adverbs.rbegin(), adverbs.rend());

    for (const auto& ad : adverbs) {
        std::cout << "{" << ad.start << " " << ad.end << " " << ad.watchersId.size() << "}\n";
    }


    int maxWatchers = 0;
    int firstAdStart = 0;
    int secondAdStart = 0;
    //O(N^2)
    for (int i = 0; i < adverbs.size(); i++) {
        for (int j = i + 1; j < adverbs.size(); j++) {
            if (!intersect(adverbs[i], adverbs[j]) && (adverbs[i].watchersId.size() + adverbs[j].watchersId.size() > maxWatchers)) {
                int watchers = countWatchers(adverbs[i], adverbs[j]);
                if (watchers > maxWatchers) {
                    firstAdStart = adverbs[i].start;
                    secondAdStart = adverbs[j].start;
                    maxWatchers = watchers;
                }
            }
        }
    }

    if (maxWatchers == 0) {
        maxWatchers = adverbs[0].watchersId.size();
        firstAdStart = adverbs[0].start;
        secondAdStart = firstAdStart + 5;
    }
    
    std::cout << maxWatchers << " " << (firstAdStart < secondAdStart ? firstAdStart : secondAdStart) << " " << (firstAdStart < secondAdStart ? secondAdStart : firstAdStart);

    return 0;
}
