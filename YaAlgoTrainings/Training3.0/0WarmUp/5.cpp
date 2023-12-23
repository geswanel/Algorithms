/*
The goodness of a string is the number of positions from 1 to L - 1 such that the next letter is the next in the alphabet.

Determine the maximum goodness.

Given:
N - letters (from 1 to N) (in alphabetical order)
Then, ci - the number of identical letters i

How to achieve the maximum possible goodness?
A brute-force solution would require 26 * 10^9 operations - iterate through the array with the number of letters from 'a' to 'a' + N, counting the goodness while removing letters. It's logical to place letters from left to right for maximum goodness. How to make it faster?

1) Find the minimum number of identical letters, then arrange the string based on this minimum. For example, a - 3, b - 4, c - 2. If the minimum is 2, then arrange the string as 'abcabc' (2 times).
   Finding the minimum: O(26) + counting: O(26), so complexity is O(26^2).
2) It's possible to improve it by counting faster, but why bother?
   Find the minimum, and then, while counting, keep track of the minimum. Then, it's O(26 * 2).

*/

#include <iostream>
#include <vector>


std::ostream& operator<<(std::ostream& out, std::vector<int>& vec) {
	out << "vec{";
	for (const auto& v : vec) {
		out << v << ", ";
	}
	out << "}";
	return out;
}

int main() {
	int N;
	std::cin >> N;
	
	std::vector<int> charCnt(N);
	int minCnt = 1e9;
	for (int i = 0; i < N; i++) {
		std::cin >> charCnt[i];
		if (charCnt[i] < minCnt) {
			minCnt = charCnt[i];
		}
	}
	
	int totalZeros = 0;
	int newMinCnt;
	long long goodOfString = 0;
	while (totalZeros != N) {	
		//std::cout << "Start circle: " << charCnt << " minCnt = " << minCnt << '\n';
		totalZeros = 0;
		newMinCnt = 1e9;

		for (int i = 0; i < N - 1; i++) {
			if (charCnt[i] > 0) {
				charCnt[i] -= minCnt;
				if (charCnt[i + 1] > 0) {
					goodOfString += minCnt;
				}

				if (charCnt[i] < newMinCnt && charCnt[i] > 0) {
					newMinCnt = charCnt[i];
				}
			} else {
				totalZeros++;
			}
		}
		
		if (charCnt[N - 1] > 0) {
			charCnt[N - 1] -= minCnt;
			if (charCnt[N - 1] < newMinCnt) {
				newMinCnt = charCnt[N - 1];
			}
		} else {
			totalZeros++;
		}

		minCnt = newMinCnt;
		//std::cout << "Start circle: " << charCnt << " minCnt = " << minCnt << " goodOfString = " << goodOfString << '\n';
	}

	std::cout << goodOfString;
	

	return 0;
}