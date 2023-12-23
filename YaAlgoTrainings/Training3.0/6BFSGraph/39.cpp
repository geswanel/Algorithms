/*
3D array

Find the minimum path to the surface
Transition is possible if both cubes are free and have a common face

Input
N
Then N lines of N characters for each level starting from the top
Any cell on the top level is an exit
There is always an exit
*/

#include <iostream>
#include <vector>
#include <queue>
#include <climits>


using Cave3D = std::vector<std::vector<std::vector<int>>>;

const int NOT_REACHED = -1;
const int BLOCKED = -2;

struct Point {
    int h;
    int l;
    int w;
};

const int POSSIBLE_STEPS = 6;
const int hstep[POSSIBLE_STEPS] = {1, -1, 0, 0, 0, 0};
const int lstep[POSSIBLE_STEPS] = {0, 0, 1, -1, 0, 0};
const int wstep[POSSIBLE_STEPS] = {0, 0, 0, 0, 1, -1};

bool inBorder(int val, int borderMax, int borderMin = 0) {
    return borderMin <= val && val < borderMax;
}

int bfs(Cave3D& cave, const Point start) {
    std::queue<Point> pointQueue;
    cave[start.h][start.l][start.w] = 0;
    pointQueue.push(start);
    while (!pointQueue.empty()) {
        Point curPoint = pointQueue.front();
        int curStep = cave[curPoint.h][curPoint.l][curPoint.w];
        for (int i = 0; i < POSSIBLE_STEPS; i++) {
            Point nextPoint = {curPoint.h + hstep[i], curPoint.l + lstep[i], curPoint.w + wstep[i]};
            if (inBorder(nextPoint.h, cave.size()) && inBorder(nextPoint.l, cave.size()) && inBorder(nextPoint.w, cave.size()) 
                && (cave[nextPoint.h][nextPoint.l][nextPoint.w] == NOT_REACHED 
                    || cave[nextPoint.h][nextPoint.l][nextPoint.w] > curStep + 1 && cave[nextPoint.h][nextPoint.l][nextPoint.w] != BLOCKED)) {
                
                cave[nextPoint.h][nextPoint.l][nextPoint.w] = curStep + 1;
                pointQueue.push(nextPoint);
            }
        }

        pointQueue.pop();
    }

    
    int minSteps = INT_MAX;
    for (int l = 0; l < cave.size(); l++) {
        for (int w = 0; w < cave.size(); w++) {
            if (cave[0][l][w] != BLOCKED && cave[0][l][w] != NOT_REACHED && cave[0][l][w] < minSteps) {
                minSteps = cave[0][l][w];
            }
        }
    }

    return minSteps;
}

int main() {
    int N;
    std::cin >> N;
    Cave3D cave(N, std::vector<std::vector<int>>(N, std::vector<int>(N)));
    Point start;
    for (int h = 0; h < N; h++) {
        for (int l = 0; l < N; l++) {
            for (int w = 0; w < N; w++) {
                while (std::cin.peek() != '#' && std::cin.peek() != '.' && std::cin.peek() != 'S') {
                    std::cin.ignore(1);
                }
                char code = std::cin.get();
                switch (code)
                {
                case '#':
                    cave[h][l][w] = BLOCKED;
                    break;
                case '.':
                    cave[h][l][w] = NOT_REACHED;
                    break;
                case 'S':
                    cave[h][l][w] = 0;
                    start = {h, l, w};
                    break;
                }
            }
        }
    }

    std::cout << bfs(cave, start);

    return 0;
}