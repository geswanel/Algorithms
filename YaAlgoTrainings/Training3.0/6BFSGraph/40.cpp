/*
Subway

N stations
M lines
Pi on the line
ai1 ai2 ... aipi stations

Solution:
Build a graph where each vertex represents a line, and each edge represents a transfer possibility.
Then perform depth-first search.
+ If a vertex is the start of multiple lines, there are multiple starting points, and the same applies to the ends.
*/


#include <iostream>
#include <vector>
#include <queue>
#include <climits>

int main() {
    int N;
    std::cin >> N;
    std::vector<std::vector<int>> nodeToLines(N + 1, std::vector<int>());
    int M;
    std::cin >> M;

    std::vector<std::vector<int>> lines(M + 1, std::vector<int>());
    for (int line = 1; line <= M; line++) {
        int pi;
        std::cin >> pi;
        for (int i = 0; i < pi; i++) {
            int node;
            std::cin >> node;

            lines[line].push_back(node);
            nodeToLines[node].push_back(line);
        }
    }

    std::vector<std::vector<int>> graph(M + 1, std::vector<int>());
    for (int line = 1; line <= M; line++) {
        for (const int& station : lines[line]) {
            for (const int& nodeLine : nodeToLines[station]) {
                if (nodeLine != line) {
                    graph[line].push_back(nodeLine);
                }
            }
        }
    }

    int start, finish;
    std::cin >> start >> finish;
    std::vector<int> destinations(M + 1, -1);
    std::queue<int> lineQueue;
    for (const int& line : nodeToLines[start]) {
        destinations[line] = 0;
        lineQueue.push(line);
    }

    while (!lineQueue.empty()) {
        int curLine = lineQueue.front();
        int curStep = destinations[curLine];
        for (int i = 0; i < graph[curLine].size(); i++) {
            if (destinations[graph[curLine][i]] == -1 || destinations[graph[curLine][i]] > curStep + 1) {
                destinations[graph[curLine][i]] = curStep + 1;
                lineQueue.push(graph[curLine][i]);
            }
        }

        lineQueue.pop();
    }

    int minSteps = -1;
    for (const int line : nodeToLines[finish]) {
        if (destinations[line] != -1 && (destinations[line] < minSteps || minSteps == -1)) {
            minSteps = destinations[line];
        }
    }

    std::cout << minSteps;

    return 0;
}