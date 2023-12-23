/*
Given a string

All possible variants can be composed without some letters at the beginning and end

Find the count of each type of letter in all possible strings

Given:
String consisting of lowercase Latin letters <= N = 100,000 = 1e5 characters
1 second constraint ~ 1e9 operations
64 Mb constraint - 64 * 1000_000 bytes

Output:
Letter: count of occurrences

Letters in alphabetical order.

Solution:
Let i and j be the number of letters removed from the beginning and end. i + j < N always! (otherwise the string is empty)

1. Brute-force solution - iteration. Traverse all i then all j < N - i and then count letters in the string. O(N^3) 1e15

2. An array of prefix sums can be created, where the sum = dictionary {letter-repetitions} from the part of the string from 0 to k.
Counting the sum takes O(N) + calculating the answer (iteration i j and calculation in O(1) from the sum) O(N^2) 1e10, too slow!

3. For each letter in the word, we can understand how many times it occurred
   - Indexes in the string from 0 to N - 1
       - If the index of the next letter is i, then we can remove i characters at the beginning (from 0 to i - 1). So in total i + 1 possibilities (because we can choose not to remove characters)
       - At the end, we can remove N - i - 1 characters => N - i possibilities

*/

#include <iostream>
#include <map>

using T = unsigned long long;

std::ostream& operator<<(std::ostream& out, const std::map<char, T>& charCnt) {
	for (const auto& ch : charCnt) {
		out << ch.first << ": " << ch.second << '\n';
	}
	return out;
}


int main() {

	std::map<char, T> charCnt;

	std::string line;
	std::cin >> line;
	T N = line.size();
	for (T i = 0; i < N; i++) {
		if (charCnt.count(line[i]) == 0) {
			charCnt[line[i]] = 0;
		}
		charCnt[line[i]] += (i + 1) * (N - i);
	}

	std::cout << charCnt;

	return 0;
}