/*
SNTP - Simple Network Time Protocol
Protocol:
1. Client sends the client's time at moment A
2. Server receives at moment B (accurate) and sends back B
3. Client receives response C (according to the client's clock) -> from A, B, and C, and knowing that the round-trip path is the same, we obtain the time
(round according to arithmetic rules)

The time between sending and receiving is less than 24 hours

Input:
A B C
hh:mm:ss

Round the time according to arithmetic rules
*/


#include <iostream>
#include <iomanip>

class Time {
	public:
		Time() {
			Time(0);
		}

		Time(int s) {
			ss = s;
			mm = hh = 0;
			checkFormat();
		}

		Time(int h, int m, int s) {
			hh = h;
			mm = m;
			ss = s;

			checkFormat();
		}

		int sec() const {
			return (hh * 60 + mm) * 60 + ss;
		}
		

		friend std::ostream& operator<<(std::ostream& out, const Time& t);
		friend std::istream& operator>>(std::istream& in, Time& t);

	private:
		int hh;
		int mm;
		int ss;

		void checkFormat() {
			if (ss >= 60) {
				mm += ss / 60;
				ss %= 60;
			}

			if (mm >= 60) {
				hh += mm / 60;
				mm %= 60;
			}

			if (hh >= 24) {
				hh %= 24;
			}
		}
};

std::istream& operator>>(std::istream& in, Time& t) {
	in >> t.hh;
	in.ignore(1);
	in >> t.mm;
	in.ignore(1);
	in >> t.ss;

	t.checkFormat();

	return in;
}

std::ostream& operator<<(std::ostream& out, const Time& t) {
	out << std::setw(2) << std::setfill('0') << t.hh << ":" 
		<< std::setw(2) << t.mm << ":" 
		<< std::setw(2)<< t.ss;
	return out;
}

//t1 - t2
Time operator-(const Time& t1, const Time& t2) {
	int sec = t1.sec() - t2.sec();
	if (sec < 0) {
		sec += 24 * 60 * 60;
	}
	return Time(sec);
}


int main() {
	Time A, B, C;
	std::cin >> A >> B >> C;
	int waitTime = (C - A).sec();
	int delay = waitTime / 2 + waitTime % 2;
	
	Time newTime(B.sec() + delay);

	std::cout << newTime;

	return 0;
}