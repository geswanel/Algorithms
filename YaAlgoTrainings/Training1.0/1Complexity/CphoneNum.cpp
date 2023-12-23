/**
 * Phone number format
 * +7<code><number> - 11 digits
 * 8<code><number - 11 digits
 * <number> - 7 digits
 * WHERE
 * <number> - 7 digits
 * <code> - 3 digits or 3 digits in brackets
 * 
 * default code 495
 * 
 * - can be between any 2 numbers
 * 
 * INPUT: 
 * phone
 * 3 existed phone numbers line by line
 * OUTPUT: phone in existed (YES or NO)
 */

#include <iostream>
#include <string>
#include <vector>

std::string clearPhone(const std::string& phone) {
	std::string cleared;
	for (const char& c : phone) {
		if (isdigit(c)) {
			cleared.push_back(c);
		}
	}

	if (cleared.size() == 7) {
		cleared = "495" + cleared;
	} else if (cleared.size() == 11) {
		cleared.erase(cleared.begin());
	}

	return cleared;
}

int main() {
	std::string phone;
	std::cin >> phone;

	phone = clearPhone(phone);
	for (int i = 0; i != 3; ++i) {
		std::string existedPhone;
		std::cin >> existedPhone;
		if (phone == clearPhone(existedPhone)) {
			std::cout << "YES\n";
		} else {
			std::cout << "NO\n";
		}
	}

	return 0;
}

