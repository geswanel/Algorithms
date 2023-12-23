#include <vector>

/**
 * @brief Left binary search.
 * 
 * Returns the index of the first good element.
 * What does it mean? For example, if we have an array sorted according to some condition, such that all elements to the left are bad and all elements to the right are good
 * (for example, all elements to the left are less than x and all elements to the right are greater than or equal to x)
 * There are 2 pointers l and r. Initially l is at the beginning and r is at the end
 * If the point between them is good, r is shifted
 * if the point is bad, l is shifted by +1 more, so that it falls on a good one if needed.
 * Then when l and r converge, we get the first good point, or if there is no such point, we will be at the end (separate check after exiting the function)
 * 
 * @return int index of the first "good" element. If there is no such element, return size of array
 */

template<typename T>
int lBinSearch(const std::vector<T>& elements, const T& value, bool (*checkFunc)(const T&, const T&)) {
    int l = 0;
    int r = elements.size();
    while (l < r) {
        int m = (l + r) / 2;
        if (checkFunc(value, elements[m])) {
            r = m;
        } else {
            l = m + 1;
        }
    }
    return l;
}

/**
 * @brief Right binary search.
 * 
 * Returns the last good element if all elements to the left are good and all elements to the right are bad.
 * (for example, if all elements to the left are less than or equal, and all elements to the right are greater)
 * If all elements are bad, it returns -1.
 * 
 * @tparam T 
 * @param elements 
 * @param value 
 * @param checkFunc 
 * @return int 
 */

template<typename T>
int rBinSearch(const std::vector<T>& elements, const T& value, bool (*checkFunc)(const T&, const T&)) {
    int l = -1;
    int r = elements.size() - 1;
    while (l < r) {
        int m = (l + r + 1) / 2;
        if (checkFunc(value, elements[m])) {
            l = m;
        } else {
            r = m - 1;
        }
    }
    return l;
}

/**
 * @brief lBinSearch return first good element.
 * 
 * 
 * 
 * @tparam T type of elements
 * @tparam P type of parameters (f.e. struct with parameters)
 * @param elements vector of elements 
 * @param params parameters that used for search
 * @param checkFunc function that check element using parameters
 * @return int index of element
 */
template<typename T, typename P>
int lBinSearch(const std::vector<T> & elements, const P& params, bool (*checkFunc)(const T&, const P&)) {
    int l = 0;
    int r = elements.size();
    while (l < r) {
        int m = (l + r) / 2;
        if (checkFunc(elements[m], params)) {
            r = m;
        } else {
            l = m + 1;
        }
    }
    return l;
}

/**
 * @brief lBinSearch return first good element.
 * 
 * 
 * 
 * @tparam T type of elements
 * @tparam P type of parameters (f.e. struct with parameters)
 * @param elements vector of elements 
 * @param params parameters that used for search
 * @param checkFunc function that check element using parameters
 * @return int index of element
 */
template<typename T, typename P>
int rBinSearch(const std::vector<T> & elements, const P& params, bool (*checkFunc)(const T&, const P&)) {
    int l = -1;
    int r = elements.size() - 1;
    while (l < r) {
        int m = (l + r + 1) / 2;
        if (checkFunc(elements[m], params)) {
            l = m;
        } else {
            r = m - 1;
        }
    }
    return l;
}

template<typename P>
int lBinSearch(int l, int r, const P& params, bool (*checkFunc)(const int, const P&)) {
    while (l < r) {
        int m = (l + r) / 2;
        if (checkFunc(m, params)) {
            r = m;
        } else {
            l = m + 1;
        }
    }
    return l;
}

template<typename P>
int rBinSearch(int l, int r, const P& params, bool (*checkFunc)(const int, const P&)) {
    while (l < r) {
        int m = (l + r + 1) / 2;
        if (checkFunc(m, params)) {
            l = m;
        } else {
            r = m - 1;
        }
    }
    return l;
}