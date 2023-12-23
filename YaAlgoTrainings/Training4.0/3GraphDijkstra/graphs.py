import unittest
from heapq import heappush, heappop

# A B
def min_dest(graph, S, F):
    """
    Find min distance from S to F.

    Args:
        graph: adjacency matrix (indices from 0 to V - 1)
        S: index of start (from 1 to V)
        F: index of finish (from 1 to V)
    
    Return:
        min distance and path from S to F or -1, None if there is no path between them
    """
    V = len(graph)
    visited = [False] * (V + 1)
    dist = [-1] * (V + 1)
    dist[S] = 0
    prev = [-1] * (V + 1)

    def find_min(visited: list[bool], dist: list[int]):
        min_id = 0
        min_path = -1
        for i in range(1, len(visited)):
            if not visited[i] and dist[i] != -1 and (min_path == -1 or dist[i] < min_path):
                min_id = i
                min_path = dist[i]
        
        return min_id

    while (min_id := find_min(visited=visited, dist=dist)) > 0:
        # print("min_id", min_id, "visited", visited, "dist", dist)
        visited[min_id] = True
        for i in range(1, V + 1):
            if graph[min_id - 1][i - 1] > 0 and not visited[i]:
                new_dist = dist[min_id] + graph[min_id - 1][i - 1]
                if new_dist < dist[i] or dist[i] == -1:
                    dist[i] = new_dist
                    prev[i] = min_id
    
    def get_path(prev, S, F):
        prev_node = F
        path = []
        while prev_node != -1:
            path.append(prev_node)
            prev_node = prev[prev_node]
        path.reverse()

        if path[0] == S and path[-1] == F:
            return path

    # print(dist)
    return dist[F], get_path(prev, S, F)


# C
def fast_dijksra(graph, V, S, F):
    """
    Find min and path distance from S to F.

    Args:
        graph: adjacency vector (indices from 1). Element in vector is tuple(to, dist)
        S: index of start (from 1 to V)
        F: index of finish (from 1 to V)
    
    Return:
        min distance and path from S to F or -1, None if there is no path between them

    Functions:
        find_min implemented using priority_queue for fast finding!
    """
    visited = [False] * (V + 1)
    dist = [-1] * (V + 1)
    dist[S] = 0
    prev = [-1] * (V + 1)
    heap = [(0, S)]

    def find_min(visited: list[bool], heap: list[tuple[int, int]]):
        while len(heap) > 0:
            dist, id = heappop(heap)
            if not visited[id]:
                return id
        
        return 0

    while (min_id := find_min(visited=visited, heap=heap)) > 0:
        # print("min_id", min_id, "visited", visited, "heap", heap)
        visited[min_id] = True
        for to, l in graph[min_id]:
            if not visited[to]:
                new_dist = dist[min_id] + l
                if new_dist < dist[to] or dist[to] == -1:
                    dist[to] = new_dist
                    prev[to] = min_id
                    heappush(heap, (new_dist, to))
    
    def get_path(prev, S, F):
        prev_node = F
        path = []
        while prev_node != -1:
            path.append(prev_node)
            prev_node = prev[prev_node]
        path.reverse()

        if path[0] == S and path[-1] == F:
            return path

    # print(dist)
    return dist[F], get_path(prev, S, F)


def buses(graph, V, s, f):
    """
    implement dijkstra with condition (time of departure)
    """
    INF_TIME = 10001
    visited = [False] * (V + 1)
    t = [INF_TIME] * (V + 1)
    t[s] = 0
    heap = [(0, s)]

    def find_min(visited, heap):
        while len(heap) > 0:
            _, id = heappop(heap)
            if not visited[id]:
                return id

        return 0
    
    while (min_id := find_min(visited, heap)) > 0:
        visited[min_id] = True
        for dtime, arrival, artime in graph[min_id]:
            if dtime >= t[min_id] and artime < t[arrival]:
                t[arrival] = artime
                heappush(heap, (artime, arrival))
    
    return -1 if t[f] == INF_TIME else t[f]


class DijkstraTest(unittest.TestCase):
    def test_dijkstra(self):
        N, S, F = 3, 2, 1
        graph = [[0, 1, 1],
                [4, 0, 1],
                [2, 1, 0]]
        self.assertEqual(min_dest(graph, S, F), (3, [2, 3, 1]))

        N, S, F = 4, 1, 4
        graph = [[0, 5, 8, -1],
                [5, 0, 9, 2],
                [8, 9, 0, 6],
                [-1, 2, 6, 0]]
        self.assertEqual(min_dest(graph, S, F), (7, [1, 2, 4]))


        N, S, F = 4, 1, 4
        graph = [[0, -1, -1, -1],
                [-1, 0, -1, -1],
                [-1, -1, 0, -1],
                [-1, -1, -1, 0]]
        
        self.assertEqual(min_dest(graph, S, F), (-1, None))
    
    def test_dijkstra_adjacency_list(self):
        N, S, F = 3, 2, 1
        graph = [[],
                 [(2, 1), (3, 1)],
                 [(1, 4), (3, 1)],
                 [(1, 2), (2, 1)]]
        self.assertEqual(fast_dijksra(graph, N, S, F), (3, [2, 3, 1]))

        N, S, F = 4, 1, 4
        graph = [[],
                 [(2, 5), (3, 8)],
                 [(1, 5), (3, 9), (4, 2)],
                 [(1, 8), (2, 9), (4, 6)],
                 [(2, 2), (3, 6)]]
        self.assertEqual(fast_dijksra(graph, N, S, F), (7, [1, 2, 4]))


        N, S, F = 4, 1, 4
        graph = [[], [], [], [], []]
        
        self.assertEqual(fast_dijksra(graph, N, S, F), (-1, None))


class Solution:
    def dijkstra_sol():
        N, S, F = (int(x) for x in input().split())
        graph = [[int(x) for x in input().split()] for _ in range(N)]
        dist, _ = min_dest(graph, S, F)
        print(dist)
    
    def dijkstra_path_sol():
        N, S, F = (int(x) for x in input().split())
        graph = [[int(x) for x in input().split()] for _ in range(N)]
        _, path = min_dest(graph, S, F)
        if path is None:
            print(-1)
        else:
            print(" ".join(str(node) for node in path))
    
    def fast_dijkstra():
        N, K = (int(x) for x in input().split())
        graph = [[] for _ in range(N + 1)]
        for _ in range(K):
            fr, to, l = (int(x) for x in input().split())
            graph[fr].append((to, l))
            graph[to].append((fr, l))

        #print(graph)

        A, B = (int(x) for x in input().split())
        dist, _ = fast_dijksra(graph, N, A, B)

        print(dist)
    
    def buses():
        N = int(input())
        s, f = (int(x) for x in input().split())
        R = int(input())
        graph = [[] for _ in range(N + 1)]
        for _ in range(R):
            dep, dt, ar, art = (int(x) for x in input().split())
            graph[dep].append((dt, ar, art))

        time = buses(graph, N, s, f)

        print(time)




if __name__ == "__main__":
    #unittest.main()
    Solution.buses()



