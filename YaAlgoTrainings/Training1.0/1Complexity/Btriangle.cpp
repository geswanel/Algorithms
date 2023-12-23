/**
 * Is it possible to build triangle a, b, c sides
 */

#include <iostream>


int main() {
	int a = 0, b = 0, c = 0;
	std::cin >> a >> b >> c;
	bool res = (a < b + c) && (b < a + c) && (c < a + b);;

	std::cout << (res ? "YES" : "NO");
	return 0;
}