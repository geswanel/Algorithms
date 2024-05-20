"""
    Graph DFS - using recursion

    Graph BFS - using queue level by level

    Somehow need to understand that already were in node!
"""


def dfs(graph: list[list[int]], start: int, visited=None):
        if visited is None:
            visited = [False] * len(graph)
        
        visited[start] = True
        for node in graph[start]:
            if not visited[node]:
                dfs(graph=graph, start=node, visited=visited)
        
        return visited


class SolutionGraphDFS:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        ans = dfs(rooms, 0)
        #print(ans)
        return False not in ans
    
    def dfs_with_vflag(self, graph: list[list[int]], start: int, visited: list, v_flag: any):
        visited[start] = v_flag
        for v_id in range(len(graph[start])):
            if graph[start][v_id] == 1 and visited[v_id] != v_flag:
                self.dfs_with_vflag(graph, v_id, visited, v_flag)
    
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        cur_prov = 0
        visited_prov = [-1] * len(isConnected)
        try:
            while (prov_start := visited_prov.index(-1)) >= 0:
                self.dfs_with_vflag(isConnected, prov_start, visited_prov, cur_prov)
                cur_prov += 1
        except ValueError as ve:
            return cur_prov

            


class TestGraphDFS:
    def test_canVisitAllRooms(self):
        sol = SolutionGraphDFS()
        rooms = [[1],[2],[3],[]]
        print(sol.canVisitAllRooms(rooms))

        rooms = [[1,3],[3,0,1],[2],[0]]
        print(sol.canVisitAllRooms(rooms))

    def test_findCircleNum(self):
        sol = SolutionGraphDFS()
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        print(sol.findCircleNum(isConnected=isConnected) == 2)

        isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        print(sol.findCircleNum(isConnected=isConnected) == 3)

        isConnected = [[1,1,1],[1,1,1],[1,1,1]]
        print(sol.findCircleNum(isConnected=isConnected) == 1)

from collections import deque

def bfs(matrix: list[list[str]], start: list[int]):
    q = deque()
    q.append(start)
    steps = [[2] * len(matrix[0]) for _ in range(len(matrix))]
    steps[start[0]][start[1]] = 0
    while len(q) > 0:
        cur_cell = q.popleft()
        row = cur_cell[0]
        col = cur_cell[1]


class SolutionGraphBFS:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        possible_steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
        m, n = len(maze), len(maze[0])
        steps = [[m * n for _ in range(n)] for _ in range(m)]
        steps[entrance[0]][entrance[1]] = 0
        q = deque()
        q.append(entrance)

        ans = -1
        isExit = lambda r, c: [r, c] != entrance and (r == 0 or c == 0 or r == m - 1 or c == n - 1)
        canStep = lambda r, c: 0 <= r < m and 0 <= c < n and maze[r][c] == '.'
        while len(q) > 0:
            row, col = q.popleft()
            if isExit(row, col) and (ans == -1 or steps[row][col] < ans):
                ans = steps[row][col]
            
            for st_r, st_c in possible_steps:
                next_r, next_c = row + st_r, col + st_c
                if canStep(next_r, next_c) and steps[row][col] + 1 < steps[next_r][next_c]:
                    steps[next_r][next_c] = steps[row][col] + 1
                    q.append([next_r, next_c])
        # print(m, n)
        # print("\n".join(str(s) for s in steps))
        return ans
            

class TestGraphBFS:
    def test_nearestExit(self):
        sol = SolutionGraphBFS()
        maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
        entrance = [1,2]
        print(sol.nearestExit(maze, entrance))

        maze = [["+","+","+"],[".",".","."],["+","+","+"]]
        entrance = [1,0]
        print(sol.nearestExit(maze, entrance))

        maze = [[".","+"]]
        entrance = [0,0]
        print(sol.nearestExit(maze, entrance))


          

test = TestGraphBFS()
test.test_nearestExit()