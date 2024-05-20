#include "settings.h"

/*
nums1 and nums2
have subsequence of indices
(nums1[i0] + ... + nums1[ik-1]) * min(nums2[i0] + ... + nums2[ik-1])

1. Brute Force O(Cnk * k)
2. We need to maximize min and at the same time minimize maximum
- sort pairs (el2, el1)
First k elements gives max min of nums2 subsequence
then we delete min in nums1 subseq and add next
O(n) for this and O(n lo gn)

It means we keep going to have max minimum of nums 2 and than we can increase nums1 sum
*/

class Solution {
public:
    using PQElem = tuple<int, int, int>;
    using PQ = priority_queue<PQElem, vector<PQElem>, less<PQElem>>;
    using Elem = pair<int, int>;

    vector<Elem> sortElements(const vector<int>& nums1, const vector<int>& nums2, const int size) {
        vector<Elem> elements;
        for (int i = 0; i < size; ++i) {
            elements.push_back({nums2[i], nums1[i]});
        }

        sort(elements.begin(), elements.end(), 
            [](const Elem& lhs, const Elem& rhs) { return lhs > rhs; });
        
        return elements;
    }

    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        const int n = nums1.size();
        vector<Elem> elements = sortElements(nums1, nums2, n);
        
        PQ pq;
        int nums1Sum = 0;
        int i = 0;
        while (i < k) {
            nums1Sum += elements[i][1];
            pq.push({elements[i][1], elements[i][0], i});
            ++i;
        }

        long long maxScore = nums2[i - 1] * (long long) nums1Sum;
        while (i < n) {
            auto [n1, n2, i] = pq.top();
            pq.pop();
            pq.push({nums1[i], nums2[i], i});

            nums1Sum += nums1[i] - n1;
            ++i;
        }
    }
};