"""
Brute force
N ~ 1e4
"""
def maxBenefit(cost, N, K):
    ans = 0
    for i in range(N):
        for j in range(i + 1, min(N, i + 1 + K)):
            if cost[j] - cost[i] > ans:
                ans = cost[j] - cost[i]
    
    return ans


def main():
    N, K = map(int, input().split())
    cost = list(map(int, input().split()))
    
    print(maxBenefit(cost, N, K))


if __name__ == "__main__":
    main()