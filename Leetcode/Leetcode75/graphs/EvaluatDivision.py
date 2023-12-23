from typing import List, Dict

"""
equation[i] = [Ai, Bi]
values[i] = Ai / Bi
queries[i] = [Cj, Dj]
return Cj / Dj or -1.0 if cannot be determined

Create graph where weight of edge from a to b is a / b
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], 
                     queries: List[List[str]]) -> List[float]:
        graph = dict()
        for id, eq in enumerate(equations):
            a, b = eq
            graph[a] = graph.get(a, []) + [(b, values[id])]
            graph[b] = graph.get(b, []) + [(a, 1 / values[id])]
        
        answers = []
        
        for c, d in queries:
            if c not in graph.keys() or d not in graph.keys():
                answers.append(-1.0)
            elif c == d:
                answers.append(1.0)
            else:
                ans = self.calculate(graph, c, d)
                answers.append(ans if ans else -1.0)
        
        return answers
    
    def calculate(self, graph, c, d):
        ans = None
        visited = {key: False for key in graph.keys()}
        def dfs(graph, visited, start, finish, val):
            if start == finish:
                nonlocal ans
                ans = val
                return

            visited[start] = True
            
            for to, weight in graph[start]:
                if not visited[to]:
                    dfs(graph, visited, to, finish, val * weight)
        
        dfs(graph, visited, c, d, 1.0)

        return ans

print(Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))