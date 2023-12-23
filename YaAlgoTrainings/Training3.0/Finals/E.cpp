/*
Field H x W

Can rotate in 8 directions
Want the minimum number of rotations to get from one point to another
Some cells are impassable
Initially, the tractor lies and needs to be turned somewhere.


H W up to 1e3
H rows . free X occupied

sx sy starting position
tx ty ending position

In each cell, we store the minimum number of rotations required to reach it and in which direction we went.
We iterate over all 1s and their neighbors, then over all 2s and their neighbors, and so on.
Keep track of 1s and 2s.
*/


#include <iostream>
#include <queue>
#include <vector>
#include <unordered_set>


const int BLOCKED = -2;
const int NOT_REACHED = -1;

struct Point {
    int row;
    int col;
};


struct Direction {
    int rowStep;
    int colStep;
    
    struct HashFunction {
        size_t operator()(const Direction& d) const {
        size_t xHash = std::hash<int>()(d.rowStep);
        size_t yHash = std::hash<int>()(d.colStep) << 1;
        return xHash ^ yHash;
        }
    };
};

std::ostream& operator<<(std::ostream& out, const Direction& p) {
    out << '(' << p.rowStep << ',' << p.colStep << ')';
    return out;
}

bool operator==(const Direction& d1, const Direction& d2) {
    return d1.rowStep == d2.rowStep && d1.colStep == d2.colStep;
}

const int POSSIBLE_DIRECTIONS = 8;
const Direction posDirections[POSSIBLE_DIRECTIONS] = {{1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}};

bool check(std::vector<std::queue<Point>>& pointsQueues) {
    for (const auto& q : pointsQueues) {
        if (!q.empty()) {
            return true;
        }
    }

    return false;
}


int main() {
    int H, W;
    std::cin >> H >> W;
    std::vector<std::vector<int>> field(H, std::vector<int>(W, NOT_REACHED));
    std::vector<std::vector<std::unordered_set<Direction, Direction::HashFunction>>> 
        directions(H, std::vector<std::unordered_set<Direction, Direction::HashFunction>>(W));
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            char code = std::cin.get();
            while (code != 'X' && code != '.') {
                code = std::cin.get();
            }
            if (code == 'X') {
                field[i][j] = BLOCKED;
            }
        }
    }

    int sx, sy;
    std::cin >> sx >> sy;
    int sCol = sx - 1;
    int sRow = H - sy;

    int fx, fy;
    std::cin >> fx >> fy;
    int fCol = fx - 1;
    int fRow = H - fy;

    // Solution
    /*
        In the field array, we store the minimum number of rotations required to reach each vertex.
        In the directions array, we store the direction from which we arrived at each vertex.
        If the direction during traversal matches the direction stored in the block, we keep the same number as is 
            (if it's less than what's already in the block and the block was reached)
        Otherwise, we update it to curMin + 1 (if it's less than what's already in the block)
        Then we put it into a vector<queue<int>> - a vector with vertices, where id is the number of rotations, and the vertex inside is the one reached with this number of rotations.
    */
    field[sRow][sCol] = 0;
    directions[sRow][sCol].insert({0, 0});
    int curMin = 0;
    std::vector<std::queue<Point>> pointsQueues;
    pointsQueues.push_back(std::queue<Point>());
    pointsQueues[0].push({sRow, sCol});
    while (check(pointsQueues)) {
        if (pointsQueues[curMin].empty()) {
            curMin++;
        }
        Point curPoint = pointsQueues[curMin].front();
        if (field[curPoint.row][curPoint.col] == curMin) {
            std::unordered_set<Direction, Direction::HashFunction>& curDirs = directions[curPoint.row][curPoint.col];
            
            for (int i = 0; i < POSSIBLE_DIRECTIONS; i++) {
                Direction nextDir = posDirections[i];
                int nextRow = curPoint.row + nextDir.rowStep;
                int nextCol = curPoint.col + nextDir.colStep;

                if (0 <= nextRow && nextRow < H && 0 <= nextCol && nextCol < W && field[nextRow][nextCol] != BLOCKED) {
                    if (curDirs.count(nextDir) == 1 && (field[nextRow][nextCol] == NOT_REACHED || curMin <= field[nextRow][nextCol])) {
                        if (field[nextRow][nextCol] == NOT_REACHED || curMin < field[nextRow][nextCol]) {
                            directions[nextRow][nextCol].clear();
                            pointsQueues[curMin].push({nextRow, nextCol});
                        }

                        field[nextRow][nextCol] = curMin;
                        directions[nextRow][nextCol].insert(nextDir);
                    } else if (curDirs.count(nextDir) == 0 && (field[nextRow][nextCol] == NOT_REACHED || curMin + 1 <= field[nextRow][nextCol])) {
                        if (field[nextRow][nextCol] == NOT_REACHED || curMin + 1 < field[nextRow][nextCol]) {
                            directions[nextRow][nextCol].clear();    
                            if (pointsQueues.size() <= curMin + 1) {
                                pointsQueues.push_back(std::queue<Point>());
                            }
                            pointsQueues[curMin + 1].push({nextRow, nextCol});
                        }
                        field[nextRow][nextCol] = curMin + 1;
                        directions[nextRow][nextCol].insert(nextDir);
                        
      
                    }
                }
            }

        }

        pointsQueues[curMin].pop();
    }

    std::cout << field[fRow][fCol];
    return 0;
}

