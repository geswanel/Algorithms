/*
Color graph into 2 colors
*/


#include <iostream>
#include <vector>



using Graph = std::vector<std::vector<int>>;

bool dfs(const Graph& graph, std::vector<int>& colors, int node, int color) {
    bool isGraphPaintedCorrectly = true;
    colors[node] = color;
    for (int i = 0; i < graph[node].size(); i++) {
        int nodeId = graph[node][i];
        if (colors[nodeId] == 0) {
            if (!dfs(graph, colors, nodeId, 3 - color)) {
                isGraphPaintedCorrectly = false;
            }
        } else if (colors[nodeId] == color) {
            isGraphPaintedCorrectly = false;
        }
    }


    return isGraphPaintedCorrectly;
}

int main() {
    int V, E;
    std::cin >> V >> E;
    
    Graph graph(V + 1, std::vector<int>());
    for(int i = 0; i < E; i++) {
        int f, s;
        std::cin >> f >> s;
        graph[f].push_back(s);
        graph[s].push_back(f);
    }

    std::vector<int> colors(V + 1, 0);

    bool isGraphPaintedCorrectly = true;
    for (int i = 1; i <= V; i++) {
        if (colors[i] == 0) {
            if(!dfs(graph, colors, i, 1)) {
                isGraphPaintedCorrectly = false;
            }
        }
    }

    std::cout << (isGraphPaintedCorrectly ? "YES" : "NO");



    return 0;
}