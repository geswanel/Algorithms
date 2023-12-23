/*
Find the shortest path in an undirected graph between two vertices

N vertices
Then the adjacency matrix
Followed by the numbers of the starting and ending vertices

L - the length of the shortest path
*/

#include <iostream>
#include <vector>
#include <queue>


using Graph = std::vector<std::vector<int>>;

const int CANT_REACH = -1;

void bfs(const Graph& graph, const int startNode, std::vector<int>& distances) {
    std::queue<int> nodesQueue;

    distances[startNode] = 0;
    nodesQueue.push(startNode);
    
    int step = 0;
    while (nodesQueue.size() > 0) {
        int curNodeId = nodesQueue.front();
        int curDistance = distances[curNodeId];

        for (int i = 0; i < graph[curNodeId].size(); i++) {
            int nextNodeId = graph[curNodeId][i];
            if (distances[nextNodeId] == CANT_REACH || distances[nextNodeId] > curDistance + 1) {
                distances[nextNodeId] = curDistance + 1;
                nodesQueue.push(nextNodeId);
            }
        }

        nodesQueue.pop();
    }
}

int main() {
    int N;
    std::cin >> N;

    Graph graph(N + 1, std::vector<int>());

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            int aij;
            std::cin >> aij;
            if (aij == 1) {
                graph[i].push_back(j);
            }
        }
    }

    int start, finish;
    std::cin >> start >> finish;

    std::vector<int> distances(N + 1, CANT_REACH);
    bfs(graph, start, distances);

    std::cout << distances[finish];
    return 0;
}