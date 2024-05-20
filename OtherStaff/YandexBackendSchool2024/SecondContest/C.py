"""
Description:
N nodes and M optic lines between pairs of them. (Graph)
Data can be tranfered in both directions (not oriented)
<= 1 line between 2 nodes
For each line time in ns to transfer is known (weight of edge)

K offers to build new lines
    - Each: from U to V with time T will cost C.
    - If U and V have line => no offer
P requests
    - Time from A to B <= T

What offers should be accepted to satisfy all requests?
Min cost of the most expensive offer.


INPUT:
N M - nodes 1e2 and lines 1e4 (vertices and edges)
U V T - lines between nodes node index from 1 to N

K - number of offers ~ 1e4
U V T C - descriptions of offer
    
P - number of requests ~ 1e3
A B T - description of request
OUTPUT

Solution:
1. Brute 
for each offer check all requests
1e4 * 1e3
+ dijkstra to check if request is ok 1e4
Too long
2. How to check for O(1) for 1 request

Optimization
Dijkstra from A answers question
    Min way to get to any node => hence min way to get to A from any node

For a request A B T
Perfrom dijkstra from A da and dijkstra from B db
    Save node weights (min time to get to A and min times to get to B)
for an offer U V T C
    da[U] + db[V] + T => time to get from A to B with new line
    check if this line makes better

So 2 dikjstra to save nodes O(2 * n^2)
for each offer K
    for each request P
        check for O(1) if it's okay

So I can understand fast enough what offers satisfy each requests?
How to choose what to build?
Because we need to minimize just cost of the most expensive line
    Just choose min line for each request

Wrong solution => Several lines can be build for one request

Solution:
1. Create graph with all possible edges(lines) and for edge save
    - time, cost, offerid
2. For each request O(P) 1e3
    - binsearch over max cost of the most expensive line O(logC) ~ log(1e9) ~ 9
        - inside binsearch => dijkstra with checking O(N^2)
        if it's possible to satisfy time bound
    - For cost => identify path and what offers will be chosen
N^2 * P * logC = 1e7 * log2(1e4 * 1e4 * 10) ~ 3 * 1e8
"""

class Edge:
    def __init__(self, time, cost=0, offerId=0):
        self.time = time
        self.cost = cost
        self.offerId = offerId


MAX_TIME = int(2 * 1e9)

def nextToProcess(V, nodeWeights, visited):
    min_time = MAX_TIME
    next = 0
    for i in range(1, V + 1):
        if not visited[i] and nodeWeights[i] < min_time:
            min_time = nodeWeights[i]
            next = i
    
    return next

def dijkstra(V: int, graph: dict, s: int, f: int, maxCost: int):
    # init nodeWeights + visited nodes for algo
    nodeWeights = [MAX_TIME] * (V + 1)
    getFrom = [-1] * (V + 1)
    nodeWeights[s] = 0
    visited = [False] * (V + 1)
    visited[0] = True
    # Dijkstra => from min weight not visited node go to all possible not visited
    # and update time to achieve
    while (fr := nextToProcess(V, nodeWeights, visited)) > 0:
        visited[fr] = True

        routes = graph.get(fr, dict())
        for to, edge in routes.items():
            if not visited[to] and edge.cost <= maxCost:
                if nodeWeights[fr] + edge.time < nodeWeights[to]:
                    nodeWeights[to] = nodeWeights[fr] + edge.time
                    getFrom[to] = fr

    return nodeWeights, getFrom

def retrieveOffers(V, graph, nodeWeights, getFrom, s, f):
    ans = []
    if getFrom[f] == -1:
        return ans
    
    print("dijkstra", nodeWeights, getFrom)
    to = f
    while (fr := getFrom[to]) != -1:
        edge = graph[fr][to]
        if edge.offerId > 0:
            ans.append(edge.offerId)
        to = fr
    
    return ans

def satSingleReq(V, graph, req):
    s, f, time = req
    minCost = 1
    maxCost = int(1e9) + 1
    while minCost < maxCost:
        midCost = (minCost + maxCost) // 2
        nodeWeights, _ = dijkstra(V, graph, s, f, midCost)
        if nodeWeights[f] > time:
            minCost = midCost + 1
        else:
            maxCost = midCost
    
    nodeWeights, getFrom = dijkstra(V, graph, s, f, minCost)
    offers = retrieveOffers(V, graph, nodeWeights, getFrom, s, f)

    return offers
        

def satisfyRequests(V, E, graph, P, requests):
    unsatisfied = []
    for req in requests:
        A, B, T = req
        nodeWeights, _ = dijkstra(V, graph, A, B, 0)
        if nodeWeights[B] > T:
            unsatisfied.append(req)
        
    
    if len(unsatisfied) == 0:
        return [0]
    
    offers = set()
    for req in unsatisfied:
        reqOffers = satSingleReq(V, graph, req)
        offers.update(reqOffers)
    
    return sorted(offers)


def main():
    V, E = [int(x) for x in input().split()]
    graph = dict()  # adjnacency dict
    for _ in range(E):
        U, V, T = [int(x) for x in input().split()]
        if U not in graph:
            graph[U] = dict()
        if V not in graph:
            graph[V] = dict()
        
        graph[V][U] = graph[U][V] = Edge(T)
    
    K = int(input())
    for offerId in range(1, K + 1):
        U, V, T, C = [int(x) for x in input().split()]
        if U not in graph:
            graph[U] = dict()
        if V not in graph:
            graph[V] = dict()
        
        graph[V][U] = graph[U][V] = Edge(T, C, offerId)
    
    P = int(input())
    requests = []
    for _ in range(P):
        A, B, T = [int(x) for x in input().split()]
        requests.append((A, B, T))
    
    ans = satisfyRequests(V, E, graph, P, requests)
    if len(ans) == 0:
        print(-1)
    elif ans[0] == 0:
        print(0)
    else:
        print(len(ans))
        print(" ".join(str(x) for x in ans))


if __name__ == "__main__":
    main()