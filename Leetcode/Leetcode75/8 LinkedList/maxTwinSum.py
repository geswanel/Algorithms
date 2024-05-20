from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
size n even ~ 1e5

twin nodes i and n - i - 1
n = 4 then 0 and 3 is twins

1. put all numbers into list and check
2. find out a size, put half in stack and next half pop from stack
3. How to use linked list here? => let's try reverse last half of list
    reverse first half and then go through last half
"""

class Solution:    
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        prev = None
        nextNode = head.next
        while node is not None:
            node = node.next.next
            head.next = prev

            prev = head
            head = nextNode
            nextNode = head.next
        
        maxTwinSum = 0
        while head is not None:
            twinSum = head.val + prev.val
            if twinSum > maxTwinSum:
                maxTwinSum = twinSum
            
            head = head.next
            prev = prev.next
            
        
        return maxTwinSum

        # n = 0
        # node = head
        # while node is not None:
        #     n += 1
        #     node = node.next
        # st = []
        # maxTwinSum = 0
        # for i in range(n):
        #     if i < n // 2:
        #         st.append(head.val)
        #     else:
        #         twinSum = st.pop() + head.val
        #         if twinSum > maxTwinSum:
        #             maxTwinSum = twinSum
            
        #     head = head.next
        
        # return maxTwinSum


        # 1
        # numbers = []
        # while head is not None:
        #     numbers.append(head.val)
        #     head = head.next
        
        # maxTwinSum = 0
        # for i in range(len(numbers) // 2):
        #     twinSum = numbers[i] + numbers[len(numbers) - 1 - i]
        #     if twinSum > maxTwinSum:
        #         maxTwinSum = twinSum
        
        # return maxTwinSum
        
        