import heapq

heap = []

N = int(input())
for _ in range(N):
    val = int(input())
    heapq.heappush(heap, val)


while len(heap) > 0:
    item = heapq.heappop(heap)
    print(item, end=" ")