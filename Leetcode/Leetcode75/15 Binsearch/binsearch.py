def lower_bound(values, val):
    """
    return first element index >= val
    """
    l = 0
    r = len(values)

    while l < r:
        m = (l + r) // 2    # closer to l can become l
        if val > values[m]:
            l = m + 1
        else:
            r = m
    
    return l

def upper_bound(values, val):
    """
        return first index of element > val
    """
    l = 0
    r = len(values)
    while l < r:
        m = (l + r) // 2
        if val >= values[m]:
            l = m + 1
        else:
            r = m
    return l

import unittest

# Your functions (lower_bound and upper_bound) go here


class TestBinarySearchFunctions(unittest.TestCase):
    def test_lower_bound(self):
        values = [1, 2, 3, 3, 4, 4, 4, 5, 6, 9, 20]
        
        # Test cases for lower_bound function
        self.assertEqual(lower_bound(values, 0), 0)  # Value less than all elements
        self.assertEqual(lower_bound(values, 1), 0)  # Value equal to first element
        self.assertEqual(lower_bound(values, 2), 1)  # Value in the middle
        self.assertEqual(lower_bound(values, 4), 4)  # Value with duplicates
        self.assertEqual(lower_bound(values, 8), 9)  # not existing value
        self.assertEqual(lower_bound(values, 21), len(values))  # Value greater than all elements
        
        # Add more test cases as needed
        
    def test_upper_bound(self):
        
        # Test cases for upper_bound function
        values = [1, 2, 3, 3, 4, 4, 4, 5, 6, 9, 20]
        
        # Test cases for upper_bound function
        self.assertEqual(upper_bound(values, 0), 0)  # Value less than all elements
        self.assertEqual(upper_bound(values, 1), 1)  # Value equal to first element
        self.assertEqual(upper_bound(values, 2), 2)  # Value in the middle
        self.assertEqual(upper_bound(values, 4), 7)  # Value with duplicates
        self.assertEqual(upper_bound(values, 8), 9)  # Value with duplicates
        self.assertEqual(upper_bound(values, 20), len(values))  # Value greater than all elements
        
        
        # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()