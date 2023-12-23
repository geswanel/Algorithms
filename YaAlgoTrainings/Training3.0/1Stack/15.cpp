/*
Cities from 0 to N-1
West on the left, East on the right (0 1 2 ... N-1)

Everyone moves to the east until they find a city where the cost of living is less than in their hometown
(problem of finding a smaller value to the right)

Solution:
1. Use a stack, traverse the array, and push elements onto the stack
   - if the current element is less than the element at the top of the stack, start popping from the stack, and the position of the current element becomes the smaller one to the right
   - Otherwise, push the element onto the stack
2. Thus, we always have an increasing sequence in the stack
*/

#include "../../utils/Stack.h"
#include <iostream>
#include <vector>

struct City {
	int value;
	int id;
};

std::vector<int> rightLessElement(const std::vector<int>& values) {
	std::vector<int> result(values.size());

	Stack<City> citiesStack;
	for (int i = 0; i < values.size(); i++) {
		while(citiesStack.size() > 0 && citiesStack.back().value > values[i]) {
			City city = citiesStack.back();
			citiesStack.pop();
			result[city.id] = i;
		}

		citiesStack.push(City{values[i], i});
	}

	while (citiesStack.size() > 0) {
		City city = citiesStack.back();
		citiesStack.pop();
		result[city.id] = -1;
	}

	return result;
}

int main() {
	int N;
	std::cin >> N;
	std::vector<int> costOfLiving(N);
	for (int i = 0; i < N; i++) {
		std::cin >> costOfLiving[i];
	}
	
	std::vector<int> newPlaceOfLiving = rightLessElement(costOfLiving);

	for (int i = 0; i < newPlaceOfLiving.size(); i++) {
		std::cout << newPlaceOfLiving[i] << ' ';
	}

	return 0;
}