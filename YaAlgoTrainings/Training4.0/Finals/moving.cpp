/*
Wmax = 1e7 * 100 g + 3T
Needed to move max weight meeting the deadline 24 hours

Graph Dijkstra?

N, M - vertices and edges
ai, bi, ti, wi - edge description (from, to, time in minutes, maxweight in gramms)
ai bi [1, N]
Need to move from 1 to N

Just max weight - dijkstra - choose vertix with max weight and traverse to next vertices
How to check time?

Idea - store 3 values => cannot come up with how to update them

Idea - somehow use reverse traversal.

Idea from GPT and chat - Use binary search to check if weight can be transfered on time.

*/

#include <iostream>
#include <vector>

using namespace std;

struct Vertix {
    int to;
    int weight;
    int time;
};

using Graph = vector<vector<Vertix>>;

const int TRUCK_WEIGHT = 3*1e6;
const int MUG_WEIGHT = 100;
const int MAX_TIME = 24 * 60;

int wMugs(const int weight) {
    return (weight - TRUCK_WEIGHT) / MUG_WEIGHT;
}

size_t findMin(const vector<bool>& visited, const vector<int>& time) {
    size_t minId = 0;
    for (size_t i = 1; i != visited.size(); ++i) {
        if (!visited[i] && time[i] < time[minId]) {
            minId = i;
        }
    }

    return minId;
}

bool canDeliver(const Graph& graph, int start, int finish, int mugs) {
    vector<bool> visited(graph.size(), false);
    vector<int> time(graph.size(), MAX_TIME + 1);
    time[start] = 0;
    size_t minId = 0;
    while ((minId = findMin(visited, time)) > 0) {
        visited[minId] = true;
        for (const Vertix& v : graph[minId]) {
            if (!visited[v.to] && wMugs(v.weight) >= mugs && time[v.to] > time[minId] + v.time) {
                time[v.to] = time[minId] + v.time;
            }
        }
    }

    return time[finish] <= MAX_TIME;
}

int maxMugs(const Graph& graph, int start, int finish) {
    int l = 0;
    int r = 1e7;
    while (l < r) {
        int m = (l + r + 1) / 2;
        if (canDeliver(graph, start, finish, m)) {
            l = m;
        } else {
            r = m - 1;
        }
    }

    return l;
}

int main() {
    size_t N, M;
    cin >> N >> M;
    Graph graph(N + 1);
    for (size_t i = 0; i != M; ++i) {
        int from, to, time, weight;
        cin >> from >> to >> time >> weight;
        graph[from].push_back({to, weight, time});
        graph[to].push_back({from, weight, time});
    }

    int mugs = maxMugs(graph, 1, N);

    cout << mugs;
    return 0;
}