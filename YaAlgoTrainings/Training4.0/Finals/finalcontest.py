def find_cx(x):
    gen1_id = gen2_id = 0
    gen1 = lambda id: gen1_id * gen1_id
    gen2 = lambda id: gen2_id * gen2_id * gen2_id
    i = 0
    for i in range(x):
        gen1_val = gen1(gen1_id)
        gen2_val = gen2(gen2_id)
        if gen1_val == gen2_val:
            gen1_id += 1
            gen2_id += 1
        elif gen1_val < gen2_val:
            gen1_id += 1
        else:
            gen2_id += 1
    
    return min(gen1(gen1_id), gen2(gen2_id))


def a():
    x = int(input())
    print(find_cx(x))

### B
MOD = int(1e9) + 7

def create_hash(s: str, x):
    n = len(s)
    s = ' ' + s
    hash = [0] * (n + 1)
    x_pow = [0] * (n + 1)
    x_pow[0] = 1
    for i in range(1, n + 1):
        hash[i] = (hash[i - 1] * x + ord(s[i])) % MOD
        x_pow[i] = x_pow[i - 1] * x % MOD
    
    return hash, x_pow

def is_equal(hash1, x_pow, hash2, start1, start2, slen):
    return (hash1[start1 + slen] + hash2[start2] * x_pow[slen]) % MOD == \
        (hash2[start2 + slen] + hash1[start1] * x_pow[slen]) % MOD

def z_function_reversed(s):
    hash_straight, x_pow1 = create_hash(s, 3)
    hash_reversed, _ = create_hash(s[::-1], 3)
    hash_straight2, x_pow2 = create_hash(s, 7)
    hash_reversed2, _ = create_hash(s[::-1], 7)

    n = len(s)
    z = [0] * n
    for i in range(n):
        l, r = 0, n - i # bin search index of end of substring

        while l < r:
            m = (l + r + 1) // 2
            if is_equal(hash_straight, x_pow1, hash_reversed, 0, i, m) and \
                    is_equal(hash_straight2, x_pow2, hash_reversed2, 0, i, m):
                l = m
            else:
                r = m - 1

        z[-i-1] = l
    
    return z

def b():
    N = int(input())
    s = input()
    print(" ".join(str(x) for x in z_function_reversed(s)))

import unittest
class Test(unittest.TestCase):
    def test_b(self):
        s = "BBABB"
        ans = [1, 2, 0, 1, 5]
        self.assertListEqual(z_function_reversed(s), ans)

        s = "burannarubabyrrybaglipspiritmatankollokvzumbboyus"
        ans = [int(x) for x in "1 0 0 0 0 0 0 0 0 10 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0".split()]
        self.assertListEqual(z_function_reversed(s), ans)

        s = ""
        ans = []
        self.assertListEqual(z_function_reversed(s), ans)

        s = "a"
        ans = [1]
        self.assertListEqual(z_function_reversed(s), ans)

        s = "abcbabbcabacaccbacbcacbba"
        ans = [1, 0, 0, 0, 5, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 2]
        self.assertListEqual(z_function_reversed(s), ans)


from heapq import heappop, heappush

def max_weight_min_time(graph, V, S, F):
    MAX_WEIGHT = int(1e7) * 100 + 3 * int(1e6)
    MAX_TIME = 24 * 60
    visited = [False] * (V + 1)
    w_t = [[] for _ in range(V + 1)]
    w_t[S].append((MAX_WEIGHT, 0))

    def find_next(visited: list[bool], w_t: list[int]):
        next_id = 0
        max_w_min_t = (0, MAX_TIME)
        for i in range(1, len(visited)):
            if not visited[i]:
                for w, t in w_t[i]:
                    if (w, t) < max_w_min_t:
                        max_w_min_t = (w, t)
                        next_id = i
        
        return next_id

    def put(w_t, to, new_weight, new_time):
        if new_time <= MAX_TIME:
            if len(w_t[to]) == 0:
                w_t[to].append((new_weight, new_time))
            else:
                pass

    while (cur := find_next(visited=visited, w_t=w_t)) > 0:
        visited[cur] = True
        for to, t_road, w_road in graph[cur]:
            if not visited[to]:
                for w_cur, t_cur in w_t[cur]:
                    # weight and time after trip from cur to to
                    new_time = t_cur + t_road
                    new_weight = min(w_cur, w_road)
                    put(w_t, to, new_time, new_weight)

    return w_t[F]


def c():
    N, M = (int(x) for x in input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        fr, to, time, weight = (int(x) for x in input().split())
        graph[fr] = (to, time, weight)
        graph[to] = (fr, time, weight)
    
    max_weight_min_time(graph, N, 1, N)


def put_bricks(a, N, M):
    def put_brick(a, N, M, cnt, id, blen):
        if blen > N:
            return
        elif blen == N:
            return (sum(cnt), cnt[:])

        if id == M:
            return
        
        min_ans = (2 * M + 1, [])
        for i in range(3):
            cnt[id] = i
            ans = put_brick(a, N, M, cnt, id + 1, blen + a[id] * cnt[id])

            if ans is not None and ans[0] < min_ans[0]:
                min_ans = ans
        
        return min_ans

    cnt = [0] * M    
    
    ans = put_brick(a, N, M, cnt, 0, 0)

    return ans




def d():
    N, M = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    if sum(a) * 2 < N:
        print(-1)
    else:
        K, cnt = put_bricks(a, N, M)
        if K > 2 * M:
            print(0)
        else:
            print(K)
            for i in range(M):
                while cnt[i] > 0:
                    print(a[i], end=" ")
                    cnt[i] -= 1



if __name__ == "__main__":
    d()