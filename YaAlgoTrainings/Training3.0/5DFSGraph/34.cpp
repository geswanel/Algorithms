/*
Topological sorting
Directed graph

Solution:
We will mark the visited vertex with gray color (1), and if it has already been processed, then with black (2).

If during depth-first search we encounter a gray vertex, it means there is a cycle and no topological sorting exists.
*/

#include <iostream>
#include <vector>
#include <algorithm>

using Graph = std::vector<std::vector<int>>;

const int COLORLESS = 0;
const int GRAY = 1;
const int BLACK = 2;

bool dfs(const Graph& graph, std::vector<int>& colors, std::vector<int>& topology, int node) {
    bool isGraphTopologyCorrect = true;
    colors[node] = GRAY;
    for (int i = 0; i < graph[node].size(); i++) {
        int nodeId = graph[node][i];
        if (colors[nodeId] == COLORLESS) {
            if (!dfs(graph, colors, topology, nodeId)) {
                isGraphTopologyCorrect = false;
            }
        } else if (colors[nodeId] == GRAY) {
            isGraphTopologyCorrect = false;
        }
    }

    colors[node] = BLACK;
    topology.push_back(node);
    return isGraphTopologyCorrect;
}

int main() {
    int V, E;
    std::cin >> V >> E;
    
    Graph graph(V + 1, std::vector<int>());
    for(int i = 0; i < E; i++) {
        int f, s;
        std::cin >> f >> s;
        graph[f].push_back(s);  
    }

    std::vector<int> colors(V + 1, COLORLESS);
    std::vector<int> topology;

    bool isGraphTopologyCorrect = true;
    for (int i = 1; i <= V; i++) {
        if (colors[i] == COLORLESS) {
            if(!dfs(graph, colors, topology, i)) {
                isGraphTopologyCorrect = false;
            }
        }
    }

    if (isGraphTopologyCorrect) {
        std::reverse(topology.begin(), topology.end());
        for (int i = 0; i < topology.size(); i++) {
            std::cout << topology[i] << ' ';
        }
    } else {
        std::cout << -1;
    }

    return 0;
}