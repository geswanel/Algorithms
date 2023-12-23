# Training 1.0 Lecture notes

<font size=4>Topics</font>
1. [Complexity, Testing, Edge cases](#complexity-testing-edge-cases)
2. [Linear search](#linear-search)
3. [set](#set)
4. [Map or Dict | Counting sort | Optimization](#map-or-dict--counting-sort--optimization)
5. [Prefix sum | Two pointers](#prefix-sum--two-pointers)
6. [Binary search](#binary-search)
7. [Event sorting](#event-sorting)
8. [Tree](#tree)


## Complexity, Testing, Edge cases
- Complexity = asymptotic number of operations or required memory depending on input size
- Testing
    - Consider common cases and **edge** cases
    - Solve tests by hands to understand problem
    - Step by step debugging with particular data
    - Stress tests


## Linear search
- Iterating over sequence elements: O(N)
    - Double iterating
- Problems
    - PitCraft - water between walls
    - RLE
    - Rabin Karp algorithm


## Set
- ADT set = contains element or not
    - add
    - erase
    - contains
- Implementation
    - hash table = ***python.set*** or ***cpp.unordered_set***
        - array of arrays where index is a result of hash function
        - hash function: Obj -> R
            - N buckets
            - ~ k collisions
            - uniform distribution
        - no order
        - contains O(k)
        - erase O(k)
        - k ~ 1 => O(1) search, erase, add
            - \+ amortized complexity


## Map or dict | counting sort | Optimization
- Counting sort
    - Number of elements ~ N >> possible values ~ K
    - Count number of occurrences using dict (cpp.map, py.dict)
    - Print result
- Map | Dict = Key:Value
    - Set of keys with binded values
- Optimization
    - Finished better Ideal


## Prefix sum | Two pointers
- Prefix Sum = sum of segment from 0 to k < N
    - subsequence sum
    - segments with zero sum
- Two Pointers
    - Merge algorithm in mergin sort


## Binary search
- The condition has a jump
    - In sorted array, every value from left < x and from right >= x
    - Bitwise binary with prefix bits
- Divide the segment in half at each step
- cpp.lower_bound, cpp.upper_bound
- ternary search algorithm
    - binary search by derivative


## Event sorting
- Formulation
    - events by time
        - F.e. when a user was on site
    - something happens at the beginning and at the end
    - something has to be calculated
    - Note: Differentiate and analyze simultaneous events
- Example
    - Event = IN or OUT on website
        - Max number of users on the website
        - Avg time when somebody used the website
    - Events on circle (schedule in a day)
        - two iterations
        

## Tree
- Memory manager
- Binary Search Tree
- Non-binary trees
- Huffman tree
- Note and Questions
    - AVL trees
    - Red Black trees
    - Cartesian tree


## Questionnaire and Assignment
1. Understanding how data structures are built helps to evaluate
    - Code basic ADT
        - cpp: vector
        - cpp: deque
        - cpp&py: list
        - cpp&py: tree
        - cpp: set
        - cpp: unordered_set
    - Structure of hash tables (py.dict, py.set, cpp.unordered_set, cpp.unordered_map)
    - Structure of Red-Black trees (cpp.set, cpp.map)
    - Others
2. Code memory manager
3. Code binary search functions
    - cpp and py: lower_bound, upper_bound, binary_search