# Training 4.0 Lecture notes

<font size=4>Topics</font>
1. [Sorting algorithms](#sorting-algorithms)
2. [Hashing strings](#hashing-strings)
3. [Dijkstra algorithm](#dijkstra-algorithm)
4. [Brute force optimizations](#brute-force-optimizations)


## Sorting algorithms
- Sorting algorithms
    - quicksort
        - partition
            - hoar partition
            - 3 pointers partition
        - DQ
    - merging sort
        - DQ
        - merge sorted
    - radix
        - each digit counting sort
- Stability of sort
    - "equal" elements in the same order
- Min complexity of sort = O(n log (n))
    - Number of questions and encoding


## Hashing strings
- Hashing polynoms
    - Calculating values in some points
- string chars = polynom coefficients
    - prime module
    - Substring comparison
        - polynoms difference
    - Substring in string
    - Prefix&Suffix comparison
    - Bzip2


## Dijkstra algorithm
- Dijkstra Algorithm => shortest path
    - Start from the best and update vertices
- Problem examples
    - Second path
        - Yen
        - Delete each edge one by one on main path
    - Widest path
    - vertices and edges on shortest path
        - reverse graph edges
        - solve from finish to start
        - check sums
    - 1 free flight
        - reverse graph edges
        - brute force - make every edge free and check
    - buses - condition consideration


## Brute force optimizations
- Queens brute force
    - rows
    - cols
    - diagonals
- Courier (voyager) optimizations
    - Subset dinamic programming


## Questionnaire and Assignment
1. How correctly return values from recursive function (bricks, contest)
2. Resolve Dijkstra with Binary search(contest)
3. Implement Dijkstra for basic weighted graph
4. Implement sorting algorithms
5. Implement hashing in C++ and Python