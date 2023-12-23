/*
Grades from 2 to 5 as integers
Final grade - rounded arithmetic mean
Everyone wants to get at least a 4

someone
a twos b threes c fours
Wants to get some fives to make the grade at least 4
What is the minimum number of fives to get?
left binary search. If they get too many, then everything is ok.

a b c -> get the minimum number of fives
*/

#include "binary2.h"
#include <iostream>

using GradeType = unsigned long long;

struct Grades {
    GradeType a;
    GradeType b;
    GradeType c;
};

std::istream& operator>>(std::istream& in, Grades& grades) {
    in >> grades.a >> grades.b >> grades.c;
    return in;
}

bool checkEnoughFives(const GradeType& fives, const Grades& grades) {
    GradeType gradeSumm = 2 * grades.a + 3 * grades.b + 4 * grades.c + 5 * fives;
    GradeType gradeCnt = grades.a + grades.b + grades.c + fives;
    return gradeSumm >= (gradeCnt * 3 + gradeCnt / 2 + gradeCnt % 2);
}

int main() {
    Grades grades;
    std::cin >> grades;
    GradeType fiveCnt = lBinSearch<GradeType, Grades>((GradeType)0, grades.a + grades.b, grades, checkEnoughFives);
    std::cout << fiveCnt;

    return 0;
}