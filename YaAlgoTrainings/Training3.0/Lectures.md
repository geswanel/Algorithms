# Training 3.0 Lecture notes

<font size=4>Topics</font>
1. [Stack](#stack)
2. [Queue | Deque | Priority queue](#queue--deque--priority-queue)
3. [DP 1D](#dp-1d-2d)
4. [DP 2D](#dp-1d-2d)
5. [Graph DFS](#graph-dfs)
6. [Graph BFS](#graph-bfs)


## Stack
- ADT stack
    - **push** on top
    - **pop** from top
    - LIFO
    - Based on vector or list
- Examples
    - bracket sequence
    - postfix notation
- **Recursion**
    - *manual implementation of memory stack*


## Queue | Deque | Priority queue
- ADT queue
    - **push** at the end
    - **pop** from the start
    - FIFO
    - Based on deque or circle buffer
- ADT deque
    - push_front
    - pop_front
    - push_back
    - pop_back
    - Based on const size array blocks
- ADT heap or priority_queue
    - **add** element
        - from bottom to top comparing with parent and swapping
    - **pop** minimum or maximum element
        - Change minimum with the last element
        - from top to bottom check conditions and swapping
    - Based on binary tree
        - Properties
            - Element < its descedant
            - Filled layer by layer
        - Can be stored in array (i => 2i + 1, 2i + 2)
    - Examples
        - LRU cash


## DP 1D 2D
- Storing previous results and use it
    - Find recurrence relation
    - Base of dp
- Examples 1D
    - Fib
    - stairway
- Examples 2D
    - largest common subsequence


## Graph DFS
- Graph - vertices and edges (V, E)
    - Not oriented, not weighted
- Storing
    - Adjacency matrix
    - Adjacency list
- DFS - Depth First Search
    - Mark visited vertices
    - Go to the first possible vertix
    - Implementation
        - Recursion
        - Stack
- Usage
    - Connectivity checking
    - Searching for loops


## Graph BFS
- [Graph, How to store, Basic principles](#graph-bfs)
- BFS
    - level by level
    - Implementation
        - queue or vector
- Weighted graphs
    - Dijkstra


## Questionnaire and Assignment
1. Code ADT
    - stack
    - queue, deque
    - heapq
2. Replace recursion with stack for fibonacci
3. Implement BFS and DFS for graphs
 