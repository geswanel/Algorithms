/*
Check for cycles in an undirected graph

The check is performed by depth-first search.

During traversal, we color vertices gray when visiting them, and black when leaving them.
- If a vertex is colored black, it means that all vertices after it have been processed, and there is no way to reach it again.
- If it is gray, it means that we have encountered a cycle, and we need to backtrack by returning from the recursion.
    - We will remember the vertex from which the cycle starts and write the vertices into an array until we encounter the same vertex again.

The graph is represented by an adjacency matrix.
*/



#include <iostream>
#include <vector>


using Graph = std::vector<std::vector<int>>;

const int COLORLESS = 0;
const int GRAY = 1;
const int BLACK = 2;

const int NOCIRCLE = -1;
const int CIRCLE = -2;


int dfs(const Graph& graph, const int nodeId, std::vector<int>& colors, std::vector<int>& circle, int prevNode) {
    colors[nodeId] = GRAY;
    for (int i = 0; i < graph[nodeId].size(); i++) {
        int nextNodeId = graph[nodeId][i];

        if (colors[nextNodeId] == COLORLESS) {
            int circleStart = dfs(graph, nextNodeId, colors, circle, nodeId);
            
            if (circleStart == CIRCLE) {
                return CIRCLE;
            }

            if (circleStart > 0) { 
                if (nodeId != circleStart) {
                    circle.push_back(nodeId);
                    return circleStart;
                } else {
                    return CIRCLE;
                }
            }
        } else if (colors[nextNodeId] == GRAY && nextNodeId != prevNode) {
            int circleStart = nextNodeId;
            circle.push_back(nextNodeId);
            circle.push_back(nodeId);
            return circleStart;
        }
    }

    colors[nodeId] = BLACK;
    return NOCIRCLE;
}

int main() {
    int n;
    std::cin >> n;
    Graph graph(n + 1, std::vector<int>());
    for (int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            int aij;
            std::cin >> aij;
            if (aij == 1) {
                graph[i].push_back(j);
                graph[j].push_back(i);
            }
        }
    }

    std::vector<int> colors(n + 1, COLORLESS);
    std::vector<int> circle;

    for (int i = 1; i <= n; i++) {
        if (colors[i] == COLORLESS) {
            dfs(graph, i, colors, circle, -1);
            if (circle.size() > 0) {
                break;
            }
        }
    }

    if (circle.size() > 0) {
        std::cout << "YES\n" << circle.size() << '\n';
        for (int i = 0; i < circle.size(); i++) {
            std::cout << circle[i] << ' ';
        }
    } else {
        std::cout << "NO";
    }

    return 0;
}