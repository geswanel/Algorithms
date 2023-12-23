def make_permutations(used: list[False], ans:list[list[int]], perm=None):
    if perm is None:
        perm = []
    
    if len(perm) == len(used):
        ans.append(perm[:])
        return
    
    for i in range(len(used)):
        if not used[i]:
            used[i] = True
            perm.append(i + 1)
            make_permutations(used, ans, perm)
            perm.pop()
            used[i] = False
            

def permutations(N):
    ans = []
    used = [False] * N
    make_permutations(used, ans)
    return ans


def queens(N):
    can_take = lambda pos1, pos2: pos1[0] == pos2[0] or pos1[1] == pos2[1] or \
        abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])
    def put_queen(N: int, queen_num: int, positions: list, cols: list[bool], \
                  diag1:list[bool], diag2: list[bool]):
        if queen_num == N + 1:
            for i in range(N):
                for j in range(i + 1, N):
                    if can_take(positions[i], positions[j]):
                        return 0
            return 1
        
        cnt = 0
        for col in range(1, N + 1):
            if (queen_num, col) not in positions and \
                    cols[col] and diag1[queen_num + col - 2] and diag2[queen_num - col + N - 1]:
                positions.append((queen_num, col))
                cols[col] = False
                diag1[queen_num + col - 2] = diag2[queen_num - col + N - 1] = False
                cnt += put_queen(N, queen_num + 1, positions, cols, diag1, diag2)
                diag1[queen_num + col - 2] = diag2[queen_num - col + N - 1] = True
                cols[col] = True
                positions.pop()
        
        return cnt

    positions = []  # (row, col) array of positions
    # on diagonal i + 1 j + 1 or i + 1 j - 1 =>
    # i - j or i + j determines diagonals. i + j from 2 to 2N => i + j - 2 is one index
    # i - j from - N + 1 to N - 1 => i - j + (N - 1)
    diag2 = [True] * (2 * N - 1)    
    diag1 = [True] * (2 * N - 1)    
    cols = [True] * (N + 1)
    return put_queen(N, 1, positions, cols, diag1, diag2)


def max_slice(graph, N):
    def get_slice(gen, i):
        return (gen & (1 << i)) >> i
    
    def get_slices(gen, N):
        slices = []
        for i in range(N):
            slices.append(get_slice(gen, i) + 1)
        return slices

    max_edge = max((max(edges) for edges in graph))
    def remained_edges(N, i, j=None):
        if j is None:
            return (N - i - 1) * (N - i) // 2
        else:
            return (N - i - 2) * (N - i - 1) // 2 + (N - j - 1)

    gen = 2
    MAX_GEN = 2 ** N

    max_sum = max_sum_gen = 0
    while gen < MAX_GEN:
        sum = 0
        for i in range(N):  # each vertices
            slice_id = get_slice(gen, i)
            if sum + max_edge * remained_edges(N, i) < max_sum:
                break
            for j in range(i + 1, N):   # any vertices that not processed
                if get_slice(gen, j) != slice_id and graph[i][j] > 0:
                    sum += graph[i][j]
        
        if sum > max_sum:
            max_sum = sum
            max_sum_gen = gen
        
        gen += 2
    
    return max_sum, get_slices(max_sum_gen, N)

import unittest

class BruteForceTest(unittest.TestCase):
    def test_permutations(self):
        N = 1
        ans = permutations(N)
        self.assertListEqual(ans, [[1]])

        N = 2
        ans = permutations(N)
        self.assertListEqual(ans, [[1, 2], [2, 1]])

        N = 3
        ans = permutations(N)
        self.assertListEqual(ans, [[1, 2, 3],
                                    [1, 3, 2],
                                    [2, 1, 3],
                                    [2, 3, 1],
                                    [3, 1, 2],
                                    [3, 2, 1]])


class BruteSolution:
    def permutation_sol():
        N = int(input())
        ans = permutations(N)
        for perm in ans:
            print("".join(str(x) for x in perm))
    
    def queens_sol():
        N = int(input())
        print(queens(N))
    
    def max_slice_sol():
        N = int(input())
        graph = [[int(x) for x in input().split()] for _ in range(N)]
        sums, slices = max_slice(graph, N)
        print(sums)
        print(" ".join(str(x) for x in slices))

if __name__ == "__main__":
    #unittest.main()
    BruteSolution.max_slice_sol()