/*
Undirected graph
with loops and multiple edges
It is necessary to construct the connected component containing the first vertex

Given
N M - number of vertices and edges
In the next M lines, edges are listed -> pairs of numbers defining the vertex numbers

Output the vertices from the connected component containing vertex 1 and their count

*/

#include <vector>
#include <iostream>


using Graph = std::vector<std::vector<int>>;


void dfs(const Graph& graph, std::vector<bool>& visited, int node) {
    visited[node] = true;
    for (int i = 0; i < graph[node].size(); i++) {
        if (!visited[graph[node][i]]) {
            dfs(graph, visited, graph[node][i]);
        }
    }
}

int main() {
    int N, M;
    std::cin >> N >> M;
    Graph graph(N + 1, std::vector<int>());

    for (int i = 0; i < M; i++) {
        int f, s;
        std::cin >> f >> s;
        graph[f].push_back(s);
        graph[s].push_back(f);
    }

    std::vector<bool> visited(N + 1, false);
    dfs(graph, visited, 1);

    int nodeCnt = 0;
    for (int i = 1; i <= N; i++) {
        nodeCnt += visited[i];
    }

    std::cout << nodeCnt << '\n';
    for (int i = 1; i <= N; i++) {
        if (visited[i]) {
            std::cout << i << " ";
        }
    }


    return 0;
}