from structlinks import LinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class List:
    def __init__(self, data: list):
        self.head = None if len(data) == 0 else ListNode(data[0])
        
        curNode = self.head
        for i in range(1, len(data)):
            curNode.next = ListNode(data[i])
            curNode = curNode.next
    
    def __str__(self):
        curNode = self.head
        linkedList = []
        while curNode is not None:
            linkedList.append(curNode.val)
            curNode = curNode.next
            
        
        return "->".join(str(x) for x in linkedList)


class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        size = 0
        node = head
        while node is not None:
            size += 1
            node = node.next
        
        pos = size // 2
        to_delete = head
        prev = None
        while pos > 0:
            pos -= 1
            prev = to_delete
            to_delete = to_delete.next
        
        if prev is not None:
            prev.next = to_delete.next
        to_delete.next = None

        return None if to_delete is head else head
    
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        prev_node = None
        cur_node = head
        next_node = head.next
        while next_node is not None:    # None<-1<-3  5->None
            cur_node.next = prev_node   # None<-1<-2
            prev_node = cur_node
            cur_node = next_node
            next_node = cur_node.next
        cur_node.next = prev_node

        return cur_node
    
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        evenHead = head.next
        curOdd, curEven = head, head.next
        
        def addAndMove(node: ListNode, nextNode: ListNode):
            node.next = nextNode
            return nextNode

        i = 3
        curNode = head.next.next
        while curNode is not None:
            if i % 2 == 1:
                curOdd = addAndMove(curOdd, curNode)
            else:
                curEven = addAndMove(curEven, curNode)
            
            i += 1
            curNode = curNode.next
        
        
        curOdd.next = evenHead
        curEven.next = None
        return head


import unittest

class LinkedListTest(unittest.TestCase):
    sol = Solution()

    def testOddEvenList(self):
        l = List([1, 2, 3, 4, 5])
        self.sol.oddEvenList(l.head)
        print(l)
        self.assertEqual(str(l), "1->3->5->2->4")
        
if __name__ == "__main__":
    # unittest.main()
    l = List([1, 2, 3, 4, 5])
    Solution().oddEvenList(l.head)
    print(l)

    l = List([1, 2, 3])
    Solution().oddEvenList(l.head)
    print(l)

    l = List([1])
    Solution().oddEvenList(l.head)
    print(l)