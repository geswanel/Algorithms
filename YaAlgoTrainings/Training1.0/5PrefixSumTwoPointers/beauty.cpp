/*
N trees, K types

All trees want to be cut down
All remaining trees must form a continuous segment of the original
At least one of each of the K types must be present
Find the shortest segment

Input N, K
N numbers - color of the i-th tree

Coordinates of the left and right segments

2 pointers - ends of the segment
If all trees are present, there is no need to move the right pointer, as it is already the minimum -> move the left
If not, move the right and

How to count colors? so as not to be O(N^2)
unordered map - key - color - value - how many in the segment.
When moving the left pointer - the value decreases by 1, and if 0, then the key is removed from the map
when moving the right, the value is added as well as the key.
Then if the size of the structure = K - then all types of trees are present

*/


#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
    int N, K;
    std::cin >> N >> K;
    std::vector<int> woods(N);
    for (int i = 0; i < N; i++) {
        std::cin >> woods[i];
    }

    
    int l = 0;
    int r = 0;
    int resultL = 0;
    int resultR = N;
    int minSize = N;
    std::unordered_map<int, int> woodsCnt;

    while (l < N && r <= N) {
        if (woodsCnt.size() < K && r != N) {
            if (!woodsCnt.count(woods[r])) {
                woodsCnt[woods[r]] = 0;
            }
            
            woodsCnt[woods[r]]++;
            r++;
        } else if (woodsCnt.size() == K) {
            if (r - l < minSize) {
                minSize = r - l;
                resultL = l + 1;
                resultR = r;
            }

            if ((--woodsCnt[woods[l]]) == 0) {
                woodsCnt.erase(woods[l]);
            }
            l++;
        }
    }
    
    std::cout << resultL << " " << resultR;



    return 0;
}