/**
 * Air conditioning
 * Parameters
 * 	- Desired temperature
 *  - mode
 * 		- freeze - decrease to desired or turn off
 * 		- heat - same but increase
 * 		- auto - heat or freeze depending on temperature
 * 		- fan - do nothing
 * 1 hour is enough to get desired temperature
 * 
 * INPUT: Troom, Tcond, Mode
 * OUTPUT: temperature in an hour
 */
#include <iostream>
#include <string>


int main() {
	int troom = 0, tcond = 0;
	std::cin >> troom >> tcond;
	std::string mode;
	std::cin >> mode;

	if (mode == "auto" ||
		mode == "freeze" && tcond <= troom ||
			mode == "heat" && tcond >= troom) {
		troom = tcond;
	}

	std::cout << troom;

	return 0;
}