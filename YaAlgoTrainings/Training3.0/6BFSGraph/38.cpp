/*
NxM
Q fleas
Feeding is possible at the feeder (one of the cells on the field is known)
Fleas move like a knight in chess
The length of the path is the number of flea jumps
Determine the minimum sums of path lengths to the feeder, or if gathering is not possible then report

Input
N M S T Q
NxM board
S T feeder
Q fleas
then coordinates of fleas


Solution: We will move backward from the feeder like a knight until we fill all possible cells. We will store the length of the path.
If we haven't reached any flea's position, then they cannot gather.
Otherwise, we sum the values at the flea's coordinates.
*/

#include <iostream>
#include <vector>
#include <climits>
#include <queue>


struct Point {
    int row;
    int col;
};

const int POSSIBLE_STEPS = 8;
const long long NOT_REACH = LLONG_MAX;

const int rowStep[POSSIBLE_STEPS] = {2, 2, 1, 1, -1, -1, -2, -2};
const int colStep[POSSIBLE_STEPS] = {1, -1, 2, -2, 2, -2, 1, -1};

bool inBorder(const int rows, const int cols, const int row, const int col) {
    return 1 <= row && row <= rows && 1 <= col && col <= cols;
}



void fillBorder(std::vector<std::vector<long long>>& border, const int N, const int M, const int S, const int T) {
    border[S][T] = 0;
    std::queue<Point> pointsQueue;
    pointsQueue.push({S, T});
    while (!pointsQueue.empty()) {
        Point curPoint = pointsQueue.front();
        long long curSteps = border[curPoint.row][curPoint.col];

        for (int i = 0; i < POSSIBLE_STEPS; i++) {
            Point nextPoint = {curPoint.row +rowStep[i], curPoint.col + colStep[i]};
            if (inBorder(N, M, nextPoint.row, nextPoint.col) 
                && (border[nextPoint.row][nextPoint.col] == NOT_REACH || border[nextPoint.row][nextPoint.col] > curSteps + 1)) {
                
                border[nextPoint.row][nextPoint.col] = curSteps + 1;
                pointsQueue.push(nextPoint);
            }
        }

        pointsQueue.pop();
    }
}

int main() {
    int N, M;
    std::cin >> N >> M;
    std::vector<std::vector<long long>> border(N + 1, std::vector<long long>(M + 1, NOT_REACH));
    int S, T;
    std::cin >> S >> T;
    fillBorder(border, N, M, S, T);

    int Q;
    std::cin >> Q;
    long long minSteps = 0; 
    for (int i = 0; i < Q; i++) {
        int row, col;
        std::cin >> row >> col;
        if (border[row][col] == NOT_REACH) {
            minSteps = -1;
            break;
        }
        minSteps += border[row][col];
    }

    std::cout << minSteps;

    return 0;
}