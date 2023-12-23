def not_segment_min(arr, requests):
    for l, r in requests:
        m = None
        not_min = None
        for i in range(l, r + 1):
            if m is None:
                m = arr[i]
            elif arr[i] < m:
                not_min = m
                m = arr[i]
            elif arr[i] > m:
                not_min = arr[i]
        
        print("NOT FOUND" if not_min is None else not_min)


def a():
    N, M = (int(x) for x in input().split())
    arr = [int(x) for x in input().split()]
    requests = []
    for _ in range(M):
        req = tuple(int(x) for x in input().split())
        requests.append(req)

    not_segment_min(arr, requests)

from math import gcd

def rational_sum(lhs: tuple[int], rhs: tuple[int]) -> tuple[int]:
    lnum, lden = lhs
    rnum, rden = rhs

    num = lnum * rden + rnum * lden
    den = rden * lden

    while (nod := gcd(num, den)) != 1:
        num //= nod
        den //= nod
    
    return num, den

def b():
    lnum, lden, rnum, rden = (int(x) for x in input().split())
    num, den = rational_sum((lnum, lden), (rnum, rden))
    print(num, den)


from math import sqrt, acos

def shortest_lc_path(fpoint: tuple[int], spoint:tuple[int]):
    """
    1. from fpoint to spoint needed to cover the distance between circles on which points located
    2. and cover the angle distance between two points

    When 1 is always the same (||f| - |s||)
    The 2 is minimal when moving along the smallest circle

    then dist = ||f| - |s|| + angle * min(|f|, |s|)
    Wrong! It's not min dist
    """
    fx, fy = fpoint
    sx, sy = spoint
    fmod2 = (fx ** 2 + fy ** 2)
    smod2 = (sx ** 2 + sy ** 2)
    # (a, b) = |a||b|cosa
    scalar = fx * sx + fy * sy
    angle = acos(scalar / (sqrt(fmod2) * sqrt(smod2)))

    dist = round(abs(sqrt(fmod2) - sqrt(smod2)) + angle * sqrt(min(fmod2, smod2)), 6)

    return dist


def c():
    xa, ya, xb, yb = (int(x) for x in input().split())
    print(shortest_lc_path((xa, ya), (xb, yb)))


def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    def get_chars_cnt(s):
        char_cnt = dict()
        for ch in s:
            char_cnt[ch] = char_cnt.get(ch, 0) + 1
        
        return char_cnt

    return get_chars_cnt(s1) == get_chars_cnt(s2)

def d():
    s1 = input()
    s2 = input()
    print("YES" if anagram(s1, s2) else "NO")


def avg_disconnect(arr):
    prefix = [0]
    for i in range(0, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    
    disconnect = []
    last_id = len(prefix) - 1
    for i in range(0, len(arr)):
        disconnect.append(arr[i] * i - prefix[i] + \
                          (prefix[-1] - prefix[i + 1] - arr[i] * (last_id - i - 1)))
    
    return disconnect

def e():
    n = int(input())
    arr = [int(x) for x in input().split()]
    disc = avg_disconnect(arr)
    print(" ".join(str(d) for d in disc))


def lift_time(floors: list, l_cap: int):
    cur_cap = 0
    time = 0
    while len(floors) > 0:
        while len(floors) > 0 and floors[-1] == 0:
            floors.pop()
        
        if cur_cap == 0:
            cur_cap = l_cap
        
        time += len(floors) * 2
        
        while len(floors) > 0 and cur_cap >= floors[-1]:
            cur_cap -= floors[-1]
            floors.pop()
        else:
            if len(floors) > 0:
                floors[-1] -= cur_cap
                cur_cap = 0
    
    return time
        

def f():
    k = int(input())
    n = int(input())
    floors = []
    for _ in range(n):
        floors.append(int(input()))
    
    print(lift_time(floors, k))

if __name__ == "__main__":
    f()