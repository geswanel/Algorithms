from typing import List

"""
nxn matrix n ~ 200

return the number of pairs (row, col) so row == col

1. Brute Force
n^3

2. Let's hash rows and cols
hash(row) = sum in row
"""

from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowHash = Counter(tuple(row) for row in grid)
        
        ans = 0
        for i in range(n):
            col = tuple(grid[x][i] for x in range(n))
            ans += rowHash[col]
        
        return ans

Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]])