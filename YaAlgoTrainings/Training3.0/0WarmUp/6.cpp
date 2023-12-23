/*
M sectors of waiting
from ai to bi - the section of setting up the next axis

If there are intersections with previously created ones, the previous ones are overwritten

Determine the number of working systems based on the given data

Input:
M - sectors
N - sections    <= 1000
N pairs ai bi

Output:
the number of working systems

Solution:

1. Naive solution: check for intersection with all previous ones - N^2 -> 1,000,000, feasible within 1 second

2. Solution using event sorting

Event - start end axis and its index

Sort them and iterate through O(N) - 1000
- Start: entered axis, saved its index. Exit, reset the index
- If entered another axis, and its index is greater, it's not valid. If the index is smaller, the current one is not valid, so discard it and save the index of the current valid one.
- Wait for exit only from the current valid block, and after exit, add to the counter

Input < Output

*/


#include <iostream>
#include <vector>
#include <algorithm>

using Status = int;
const Status START = -1;
const Status END = 1;

struct OSEvent {
	int id;
	int section;
	Status status;
};

bool operator<(const OSEvent& os1, const OSEvent& os2) {
	return os1.section < os2.section || os1.section == os2.section && os1.status < os2.status;
}

int main() {
	int M, N;
	std::cin >> M >> N;
	std::vector<OSEvent> events;
	for (int i = 0; i < N; i++) {
		int first, last;
		std::cin >> first >> last;
		events.push_back(OSEvent{i, first, START});
		events.push_back(OSEvent{i, last, END});
	}
	sort(events.begin(), events.end());

	int validOS = 0;
	int curMaxId = -1;
	for (const auto& event : events) {
		if (event.status == START) {
			if (event.id > curMaxId) {
				curMaxId = event.id;
			}
		} else {
			if (event.id == curMaxId) {
				validOS++;
				curMaxId = -1;
			} else if (event.id > curMaxId) {
				curMaxId = -1;
			}
		}
	}

	std::cout << validOS;

	return 0;
}


/*
#include <unordered_set>

struct OS {
	int firstSection;
	int lastSection;

	bool intersection(const OS& os) const {
		return os.firstSection <= firstSection && firstSection <= os.lastSection ||
			os.firstSection <= lastSection && lastSection <= os.lastSection || 
			firstSection <= os.firstSection && os.firstSection <= lastSection ||
			firstSection <= os.lastSection && os.lastSection <= lastSection;
	}

	struct HashFunction {
		size_t operator()(const OS& os) const {
			size_t fHash = std::hash<int>()(os.firstSection);
			size_t lHash = std::hash<int>()(os.lastSection) << 1;
			return fHash ^ lHash;
		}
	};
};

bool operator==(const OS& os1, const OS& os2) {
	return os1.firstSection == os2.firstSection && os1.lastSection == os2.lastSection;
}


int main() {
	int M;
	std::cin >> M;
	int N;
	std::cin >> N;
	std::unordered_set<OS, OS::HashFunction> validOS;
	for (int i = 0; i < N; i++) {
		OS newOs;
		std::cin >> newOs.firstSection >> newOs.lastSection;
		for (auto it = validOS.begin(); it != validOS.end();) {
			if (newOs.intersection(*it)) {
				it = validOS.erase(it);
			} else {
				++it;
			}
		}
		validOS.insert(newOs);
	}

	std::cout << validOS.size();

	return 0;
}

*/