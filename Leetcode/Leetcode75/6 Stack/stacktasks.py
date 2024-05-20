class Stack:
    def __init__(self):
        self.data = list()
    
    def push(self, val):
        self.data.append(val)
    
    def pop(self):
        return self.data.pop()
    
    def top(self):
        return self.data[-1]

class Solution:
    def removeStars(self, s: str) -> str:
        stack = list()
        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)
    
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = [asteroids[0]]
        for astr in asteroids[1:]:
            if astr < 0:
                # explode every asteroid < astr
                while len(stack) > 0 and stack[-1] > 0 and abs(astr) > stack[-1]:
                    stack.pop()
                # next asteroid >= astr or there aren't any asteroids or every asteroid goes left
                if len(stack) > 0 and stack[-1] > 0:
                    if abs(astr) == stack[-1]:
                        stack.pop()
                else:
                    stack.append(astr)
            else:
                stack.append(astr)
        
        return stack
    
    def decodeString(self, s: str) -> str:
        pass

        

import unittest

class StackTests(unittest.TestCase):
    def test_decodeString(self):
        pass


if __name__ == "__main__":
    main()