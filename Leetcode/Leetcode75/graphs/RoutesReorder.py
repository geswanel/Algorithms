from typing import List

"""
n 5 * 1e4 cities
n - 1 roads - each city have either two roads or 1 for edge cities

connection = [ai, bi] where ai bi road from city a to city b

1. Brute force - n^2
2. Make a graph with roads and go from 0 to other roads O(n)
graph contains pair (toCity, isFromCur)
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, True))
            graph[b].append((a, False))
        
        visited = [False] * n
        st = [0]
        ans = 0
        while len(st) > 0:
            node = st.pop()
            visited[node] = True
            for to, fromNode in graph[node]:
                if not visited[to]:
                    st.append(to)
                    ans += fromNode
        
        return ans
