"""
mxn grid
0 - empty
1 - fresh orange
2 - rotting orange
Every minute, any fresh orange that 
    is 4-directionally adjacent to a rotten orange becomes rotten.

Return time when all become rotten or -1

"""

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenQ = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rottenQ.append((i, j))
        
        time = 0
        while rottenQ:
            newRottenQ = []
            for i, j in rottenQ:
                newRottenQ += self.rottenAdjacent(grid, m, n, i, j)
            
            print(rottenQ, time)
            time += 1
            rottenQ.clear()
            rottenQ = newRottenQ
        time -= time > 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return time
    
    def rottenAdjacent(self, grid, m, n, i, j):
        rott = []
        for adi, adj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= adi < m and 0 <= adj < n and grid[adi][adj] == 1:
                grid[adi][adj] = 2
                rott.append((adi, adj))
        
        return rott


Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])