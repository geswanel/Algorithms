from random import randint


def partition(array, x, predicate=None, l=None, r=None):
    """
    Divide array on two segments based on predicate.

    Args:
        array (list): array of values
        x (any): support value for predicate - divider
        predicate: comparator of 2 values (array value and x)
        l: beginning of the array (included)
        r: end of the array (not included)
    
    Returns:
        int: End (not included) of the left range
    """
    if predicate is None:
        predicate = lambda lhs, rhs: lhs < rhs
    if l is None:
        l = 0
    if r is None:
        r = len(array)
    
    r -= 1
    while l < r:
        while l < r and predicate(array[l], x):
            l += 1
        while l < r and not predicate(array[r], x):
            r -= 1
        
        if l != r:
            # now predicate(l, x) false and predicate(r, x) True
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
    
    return l + 1 if len(array) > 0 and predicate(array[l], x) else l

def partition3p(array, pivot, predicate=None, l=None, r=None):
    """
        e g n
        1) n = less => gr = a[g]; a[g] = a[e] => a[e] = a[n], a[n] = gr, e, g,n ++
        2) n = equal => swap(a[g], a[n]) g++ n++
        3) n = greater => n++
    """
    if predicate is None:
        predicate = lambda lhs, rhs: lhs < rhs
    if l is None:
        l = 0
    if r is None:
        r = len(array)
    
    e = g = n = l
    while n < r:
        if predicate(array[n], pivot):
            n_tmp = array[n]
            array[n] = array[g]
            array[g] = array[e]
            array[e] = n_tmp
            e += 1
            g += 1
        elif not predicate(pivot, array[n]):    # f.e. not < and not > => equal
            array[g], array[n] = array[n], array[g]
            g += 1

        n += 1
    
    return e, g


def qsort3(array, predicate=None, l=None, r=None):
    if predicate is None:
        predicate = lambda lhs, rhs: lhs < rhs
    if l is None:
        l = 0
    if r is None:
        r = len(array)
    
    if r - l <= 1:
        return
    
    def get_pivot(array, l, r):
        if r - l <= 5:
            return array[randint(l, r - 1)]
        p1 = randint(l, r - 1)
        p2 = randint(l, r - 1)
        p3 = randint(l, r - 1)
        return array[p1] + array[p2] + array[p3] - min(array[p1], array[p2], array[p3]) - \
            max(array[p1], array[p2], array[p3])
    
    pivot = get_pivot(array, l, r)
    pivot_pos, gr_pos = partition3p(array, pivot, predicate, l, r)

    qsort3(array, predicate, l, pivot_pos)
    qsort3(array, predicate, gr_pos, r)



def qsort(array, predicate=None, l=None, r=None):
    if predicate is None:
        predicate = lambda lhs, rhs: lhs < rhs
    if l is None:
        l = 0
    if r is None:
        r = len(array)
    
    if r - l <= 1:
        return
    
    x = array[randint(l, r - 1)]
    l_end = partition(array, x, predicate, l, r)
    if array[l_end] == x:
        l_end += 1

    qsort(array, predicate, l, l_end)
    qsort(array, predicate, l_end, r)


def merge(arr1, l1, r1, arr2, l2, r2, buffer):
    """
    merge 2 arrays. r1 and r2 not included
    """
    while l1 < r1 and l2 < r2:
        if arr1[l1] <= arr2[l2]:
            buffer.append(arr1[l1])
            l1 += 1
        else:
            buffer.append(arr2[l2])
            l2 += 1
    
    if l1 == r1:
        buffer += arr2[l2:r2]
    else:
        buffer += arr1[l1:r1]


def merge_sort(array, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(array)
    
    if (r - l) <= 1:
        return

    m = (l + r) // 2
    merge_sort(array, l, m)
    merge_sort(array, m, r)
    buffer = []
    merge(array, l, m, array, m, r, buffer)
    array[l:r] = buffer
    buffer.clear()


def radix_buckets_print(buckets: dict, phase: int):
    print("**********")
    print(f"Phase {phase}")
    for i in range(10):
        buc = str(i)
        print(f"Bucket {buc}: {'empty' if buc not in buckets.keys() else ', '.join(buckets[buc])}")


def radix_sort(arr, debug=False):
    """
    Sorting strings in arr:
    Args:
        arr (list[str]): list of strigs where arr[i] is [0-9] str with same length
    """
    if arr is None or not isinstance(arr, list) or len(arr) == 0:
        print(arr is None)
        print(isinstance(arr, list))
        raise ValueError
    
    phases = len(arr[0])
    for ph in range(phases):    # ph - pos of char from the end of str
        buckets = dict()
        for s in arr:
            buckets[s[-ph - 1]] = buckets.get(s[-ph -1], []) + [s]
        
        if debug:
            radix_buckets_print(buckets, ph + 1)
            
        arr_id = 0
        for bucket in sorted(buckets.keys()):
            for s in buckets[bucket]:
                arr[arr_id] = s
                arr_id += 1


import unittest


class Test(unittest.TestCase):
    def test_merg_sort(self):
        arr = [1, 5, 2, 4, 3]
        merge_sort(arr)
        self.assertListEqual(arr, sorted(arr))

        arr = []
        merge_sort(arr)
        self.assertListEqual(arr, sorted(arr))

        arr = [1]
        merge_sort(arr)
        self.assertListEqual(arr, sorted(arr))

        arr = [1, 2]
        merge_sort(arr)
        self.assertListEqual(arr, sorted(arr))

        arr = [2, 1]
        merge_sort(arr)
        self.assertListEqual(arr, sorted(arr))

    def test_merge(self):
        arr1 = [1, 3, 5, 5, 9]
        arr2 = [2, 5, 6]
        buffer = []
        merge(arr1, 0, len(arr1), arr2, 0, len(arr2), buffer)
        self.assertListEqual(buffer, [1, 2, 3, 5, 5, 5, 6, 9])

        arr1 = [0]
        arr2 = []
        buffer = []
        merge(arr1, 0, len(arr1), arr2, 0, len(arr2), buffer)
        self.assertListEqual(buffer, [0])

        arr1 = []
        arr2 = [0]
        buffer = []
        merge(arr1, 0, len(arr1), arr2, 0, len(arr2), buffer)
        self.assertListEqual(buffer, [0])

    def test_partition(self):
        def check_partition(arr, pivot_pos, pivot):
            for i in range(len(arr)):
                if i < pivot_pos and arr[i] >= pivot:
                    return False
                elif i == pivot_pos and arr[i] != pivot:
                    return False
                elif i > pivot_pos and arr[i] < pivot:
                    return False
            return True
        #print(elements)
        # array -> x -> result
        # empty array -> any x -> 0 0
        self.assertEqual(partition3p([], 0), (0, 0))
        # 1 2 -> 2 -> 1 1
        self.assertEqual(partition3p([1, 2], 2), (1, 2))
        # 1 -> 1 -> 0 1
        self.assertEqual(partition3p([1], 1), (0, 1))
        # 1 -> 2 -> 1 0
        self.assertEqual(partition3p([1], 2), (1, 1))
        # 1 3 5 -> 3 -> 1 2
        ar = [3, 5, 1]
        self.assertEqual(partition3p(ar, 3), (1, 2))
        #print(ar)

        ar = [5, 2]
        self.assertEqual(partition3p(ar, 3), (1, 1))
        #print(ar)
        # 1 3 5 -> 4 -> 2 1
        self.assertEqual(partition3p([1, 3, 5], 4), (2, 2))
        # 1 3 5 -> 2 -> 1 2
        self.assertEqual(partition3p([1, 3, 5], 2), (1, 1))

        arr = [55, -29, -55, 66, 77, 81]
        pivot = 81
        before_arr = arr[:]
        pivot_pos, _ = partition3p(arr, pivot)
        self.assertEqual(pivot_pos, 5)
        self.assertListEqual(sorted(before_arr), sorted(arr))

        arr = [55, -29, -55, 66, 77, 81]
        pivot = 66
        before_arr = arr[:]
        pivot_pos, _ = partition3p(arr, pivot)
        self.assertEqual(pivot_pos, 3)
        self.assertListEqual(sorted(before_arr), sorted(arr))
        self.assertTrue(check_partition(arr, pivot_pos, pivot))

        arr = [55, -29, -55, 66, 77, 81]
        pivot = 55
        before_arr = arr[:]
        pivot_pos, _ = partition3p(arr, pivot)
        self.assertEqual(pivot_pos, 2)
        self.assertListEqual(sorted(before_arr), sorted(arr))
        self.assertTrue(check_partition(arr, pivot_pos, pivot))

        arr = [79, -87, -7, -92, -66, 56, -71, 16, -56, -90]
        before_arr = arr
        pivot = -71
        pivot_pos, _ = partition3p(arr, pivot)
        self.assertEqual(pivot_pos, 3)
        self.assertListEqual(sorted(before_arr), sorted(arr))
        self.assertTrue(check_partition(arr, pivot_pos, pivot))
    
    def test_qsort(self):
        arr = []
        qsort3(arr)
        self.assertListEqual(arr, sorted(arr))

        arr = [1, 2]
        qsort3(arr)
        self.assertListEqual(arr, sorted(arr))

        arr = [2, 1]
        qsort3(arr)
        self.assertListEqual(arr, sorted(arr))

        arr = [1]
        qsort3(arr)
        self.assertListEqual(arr, sorted(arr))

        arr = [2, 1, 3]
        qsort3(arr)
        self.assertListEqual(arr, sorted(arr))

        arr = [2, 1, 1, 1, 3]
        qsort3(arr)
        self.assertListEqual(arr, sorted(arr))

        arr = [79, -87, -7, -92, -66, 56, -71, 16, -56, -90]
        qsort3(arr)
        self.assertListEqual(arr, sorted(arr))

        # for _ in range(20):
        #     size = randint(0, 10)
        #     array = [randint(-100, 100) for _ in range(size)]
        #     print(array)
        #     qsort3(array)
        #     self.assertListEqual(array, sorted(array))



class Solutions:
    def partition_sol(self):
        N = int(input())
        elements = [int(x) for x in input().split()]
        x = int(input())
        end = partition(elements, x)
        print(end)
        print(len(elements) - end)
    
    def qsort_sol(self):
        N = int(input())
        arr = [int(x) for x in input().split()]
        qsort3(arr)
        print(" ".join(str(x) for x in arr))
    
    def merge_sol():
        N = int(input())
        arr1 = [int(x) for x in input().split()]
        M = int(input())
        arr2 = [int(x) for x in input().split()]
        buffer = []
        merge(arr1, 0, len(arr1), arr2, 0, len(arr2), buffer)
        print(" ".join(str(num) for num in buffer))
    
    def merge_sort_sol():
        N = int(input())
        arr = [int(x) for x in input().split()]
        merge_sort(arr)
        print(" ".join(str(x) for x in arr))
    
    def radix_sort_sol():
        n = int(input())
        arr = [input() for _ in range(n)]
        print("Initial array:")
        print(", ".join(arr))
        radix_sort(arr, True)
        print("**********")
        print("Sorted array:")
        print(", ".join(arr))


if __name__ == "__main__":
    unittest.main()
    #Solutions.qsort_sol()