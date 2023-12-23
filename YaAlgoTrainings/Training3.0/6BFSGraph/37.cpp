/*
Find the minimum path between two vertices in an undirected graph

N
Adjacency matrix
Start End

Same as in the previous task, but also keep track of previous vertices.
*/

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>


using Graph = std::vector<std::vector<int>>;

struct GraphNode {
    int minDist;
    int prevNode;
};

const int CANT_REACH = -1;


std::vector<int> bfs(const Graph& graph, const int startNode, const int finishNode, std::vector<GraphNode>& distances) {
    std::queue<int> nodesQueue;

    distances[startNode] = {0, -1};
    nodesQueue.push(startNode);
    
    while (nodesQueue.size() > 0) {
        int curNodeId = nodesQueue.front();
        int curDistance = distances[curNodeId].minDist;

        for (int i = 0; i < graph[curNodeId].size(); i++) {
            int nextNodeId = graph[curNodeId][i];
            if (distances[nextNodeId].minDist == CANT_REACH || distances[nextNodeId].minDist > curDistance + 1) {
                distances[nextNodeId] = {curDistance + 1, curNodeId};
                nodesQueue.push(nextNodeId);
            }
        }

        nodesQueue.pop();
    }

    std::vector<int> result;
    if (distances[finishNode].minDist != 0 && distances[finishNode].minDist != -1) {
        int curNode = finishNode;
        result.push_back(finishNode);
        do {
            curNode = distances[curNode].prevNode;
            result.push_back(curNode);
        } while (distances[curNode].prevNode != -1);

        std::reverse(result.begin(), result.end());
    }

    return result;
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

    std::vector<GraphNode> distances(N + 1, {CANT_REACH, -1});
    std::vector<int> route(bfs(graph, start, finish, distances));

    std::cout << distances[finish].minDist << '\n';
    for (const int& node : route) {
        std::cout << node << ' ';
    }
    return 0;
}