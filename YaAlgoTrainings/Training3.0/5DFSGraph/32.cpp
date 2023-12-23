/*
Calculate and determine the connected components in an undirected graph
*/


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

void dfs(const Graph& g, std::vector<bool>& visited, int node, std::vector<int>& connected) {
    visited[node] = true;
    connected.push_back(node);
    for (int i = 0; i < g[node].size(); i++) {
        if (!visited[g[node][i]]) {
            dfs(g, visited, g[node][i], connected);
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
    std::vector<std::vector<int>> connectedChunks;

    for (int i = 1; i <= N; i++) {
        if (!visited[i]) {
            connectedChunks.push_back(std::vector<int>());
            dfs(graph, visited, i, connectedChunks.back());
        }
    }

    std::cout << connectedChunks.size() << '\n';
    for (int i = 0; i < connectedChunks.size(); i++) {
        std::cout << connectedChunks[i].size() << '\n';
        for (int j = 0; j < connectedChunks[i].size(); j++) {
            std::cout << connectedChunks[i][j] << ' ';
        }
        std::cout << '\n';
    }



    return 0;
}