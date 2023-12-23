/*
K sets of tasks
1 row of desks

Each desk (except possibly the last one) accommodates 2 students

Numbers are in order - right relative to the teacher is the 1st variant, left is the 2nd, the first from the second desk is the 3rd, and so on. After K, it's 1 again.

On the last desk, if there is only one student, they use the 1st variant.

The first student sits at a certain desk.
The second wants to sit as close as possible to the desired variant.
If there is an option to sit in front or behind, they sit in front.

/2 specifies the desk
%2 specifies the seat behind the desk

Input:
N - number of students
K - number of variants
Desk, seat (1 is the right seat, 2 is the left seat)

%2 = 0 - seat 1 (right of the teacher)
%2 = 1 - seat 2 (left of the teacher)
/2 returns the row

The code row * 2 + rowPlace - 1 - then it aligns with the description above

Code of the first sitting student code = 2 - because row 1, place 1

Code of the last sitting student code = N + 2 - 1    (if N = 1, it should match the first)
*/



#include <iostream>

struct SitPlace {
    SitPlace(int code, int totalStudents) {
        isValid = 2 <= code && code <= 2 + totalStudents - 1;
        row = code / 2;
        rowPlace = code % 2;
    }

    int row;
    int rowPlace;
    bool isValid;

    int calculateCode() const {
        return row * 2 + rowPlace - 1;
    }

    bool operator<=(const SitPlace& sp) const {
        return calculateCode() <= sp.calculateCode();
    }
};

int main() {
    int totalStudents, totalVariants;
    std::cin >> totalStudents >> totalVariants;

    int sitRow, sitRowPlace;
    std::cin >> sitRow >> sitRowPlace;
    int firstStudentCode = sitRow * 2 + sitRowPlace - 1;

    SitPlace frontSit(firstStudentCode - totalVariants, totalStudents);
    SitPlace backSit(firstStudentCode + totalVariants, totalStudents);
    if (!frontSit.isValid && !backSit.isValid) {
        std::cout << -1;
    } else {
        if (!backSit.isValid || frontSit.isValid && sitRow - frontSit.row < backSit.row - sitRow) {
            std::cout << frontSit.row << " " << (frontSit.rowPlace + 1);
        } else {
            std::cout << backSit.row << " " << (backSit.rowPlace + 1);
        }
    }

    return 0;
}